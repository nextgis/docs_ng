#!/usr/bin/env python3
"""Import Sphinx search records and publish verified Typesense indexes."""

import argparse
import json
import os
import re
import sys
import tempfile
import uuid
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SEARCH_PARAMETERS = {
    "query_by": "heading,title,content",
    "query_by_weights": "10,5,1",
    "num_typos": 2,
    "drop_tokens_threshold": 0,
    "highlight_fields": "content",
    "highlight_affix_num_tokens": 8,
}


class SearchError(RuntimeError):
    """A safe diagnostic suitable for build logs, without credentials or bodies."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code


def alias_for(language):
    if language not in ("ru", "en"):
        raise SearchError("Language must be ru or en")
    # Keep the existing local PoC's nextgis_docs_ru/en physical collections intact.
    return "nextgis_docs_search_" + language


def validate_collection(collection, language):
    prefix = alias_for(language) + "_"
    if not isinstance(collection, str) or not collection.startswith(prefix):
        raise SearchError("Collection must start with " + prefix)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", collection[len(prefix) :]):
        raise SearchError("Collection must have a nonempty alphanumeric build suffix")
    return collection


def validate_url(value, endpoint=False):
    if not isinstance(value, str) or not value:
        raise SearchError("URL must be a nonempty string")
    try:
        parts = urlsplit(value)
    except ValueError:
        raise SearchError("URL is malformed") from None
    if parts.username or parts.password or parts.query or parts.fragment:
        raise SearchError("URL must not contain credentials, a query or a fragment")
    if parts.scheme:
        if parts.scheme not in ("http", "https") or not parts.netloc:
            raise SearchError("URL must use HTTP or HTTPS")
    elif endpoint or parts.netloc or not value.startswith("/"):
        raise SearchError("URL must be an HTTP endpoint or an absolute site path")
    return value.rstrip("/")


def validate_records(records, language):
    alias_for(language)
    if not records:
        raise SearchError("Refusing to prepare an empty documentation index")
    ids = set()
    for number, record in enumerate(records, 1):
        if not isinstance(record, dict):
            raise SearchError(f"Record {number} must be a JSON object")
        for field in ("id", "title", "heading", "content", "url", "path", "language"):
            value = record.get(field)
            if not isinstance(value, str) or (field != "content" and not value.strip()):
                raise SearchError(f"Record {number} has an invalid {field}")
        if "section" in record and not isinstance(record["section"], str):
            raise SearchError(f"Record {number} has an invalid section")
        if record["language"] != language:
            raise SearchError(f"Record {number} has a different language")
        if record["id"] in ids:
            raise SearchError(f"Record {number} has a duplicate id")
        ids.add(record["id"])
        try:
            parts = urlsplit(record["url"])
        except ValueError:
            raise SearchError(f"Record {number} has an invalid URL") from None
        if (
            parts.scheme not in ("", "http", "https")
            or parts.username
            or parts.password
        ):
            raise SearchError(f"Record {number} has an invalid URL")
        if (parts.scheme and not parts.netloc) or (
            not parts.scheme and (parts.netloc or not record["url"].startswith("/"))
        ):
            raise SearchError(f"Record {number} has an invalid URL")
    return records


def read_records(path, language):
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except ValueError:
            raise SearchError(f"Malformed JSON on input line {number}") from None
    return validate_records(records, language)


def write_file(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=str(path.parent),
            delete=False,
        ) as output:
            temporary = Path(output.name)
            output.write(text)
        os.replace(str(temporary), str(path))
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def schema_for(collection, language):
    validate_collection(collection, language)
    return {
        "name": collection,
        "fields": [
            {"name": name, "type": "string", "locale": language, "stem": True}
            for name in ("heading", "title", "content")
        ]
        + [
            {"name": name, "type": "string", "index": False}
            for name in ("url", "path", "language")
        ]
        + [{"name": "section", "type": "string", "index": False, "optional": True}],
        "token_separators": ["-", "_"],
        "metadata": {"nextgis_docs_search": {"language": language, "published": False}},
    }


class TypesenseClient:
    def __init__(self, host, api_key, timeout=30):
        self.host = validate_url(host, endpoint=True)
        if not api_key:
            raise SearchError("Set TYPESENSE_API_KEY for server commands")
        if timeout <= 0:
            raise SearchError("Timeout must be positive")
        self.api_key = api_key
        self.timeout = timeout

    def request(self, method, path, payload=None, content_type="application/json"):
        data = payload
        if isinstance(payload, dict):
            data = json.dumps(payload).encode("utf-8")
        headers = {"X-TYPESENSE-API-KEY": self.api_key, "Content-Type": content_type}
        request = Request(self.host + path, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return response.read().decode("utf-8")
        except HTTPError as error:
            raise SearchError(
                f"Typesense {method} {path} failed (HTTP {error.code})",
                status_code=error.code,
            ) from None
        except (URLError, OSError, UnicodeError):
            raise SearchError(
                f"Cannot read Typesense response for {method} {path}"
            ) from None

    def json(self, method, path, payload=None, expected_type=dict):
        try:
            result = json.loads(self.request(method, path, payload))
        except ValueError:
            raise SearchError("Typesense returned malformed JSON") from None
        if not isinstance(result, expected_type):
            raise SearchError("Typesense returned an unexpected JSON response")
        return result


def verify_collection(client, collection, language, count):
    metadata = client.json("GET", "/collections/" + quote(collection, safe=""))
    if (
        metadata.get("name") != collection
        or type(metadata.get("num_documents")) is not int
        or metadata["num_documents"] != count
    ):
        raise SearchError(
            "Stored collection document count does not match the exported index"
        )
    field_list = metadata.get("fields")
    if not isinstance(field_list, list) or any(
        not isinstance(field, dict) for field in field_list
    ):
        raise SearchError("Typesense returned a malformed collection schema")
    fields = {field.get("name"): field for field in field_list}
    for name in ("heading", "title", "content"):
        field = fields.get(name, {})
        if field.get("locale") != language or field.get("stem") is not True:
            raise SearchError("Stored collection language schema does not match")
    return metadata


def collection_aliases(client):
    aliases = client.json("GET", "/aliases").get("aliases")
    if not isinstance(aliases, list) or any(
        not isinstance(alias, dict)
        or not isinstance(alias.get("name"), str)
        or not isinstance(alias.get("collection_name"), str)
        for alias in aliases
    ):
        raise SearchError("Typesense returned malformed collection aliases")
    return {alias["name"]: alias["collection_name"] for alias in aliases}


def cleanup_collections(client, language, current, previous, collections):
    if any(not isinstance(collection, dict) for collection in collections):
        raise SearchError("Typesense returned malformed collections")
    for collection in collections:
        name = collection.get("name")
        metadata = collection.get("metadata", {})
        publication = (
            metadata.get("nextgis_docs_search", {})
            if isinstance(metadata, dict)
            else {}
        )
        if (
            not isinstance(name, str)
            or not name.startswith(alias_for(language) + "_")
            or not isinstance(publication, dict)
            or publication.get("language") != language
            or publication.get("published") is not True
            or name in (current, previous)
        ):
            continue
        validate_collection(name, language)
        # Recheck references before each deletion. A later publication makes this
        # build's retention decision obsolete, and other aliases may need a version.
        aliases = collection_aliases(client)
        if aliases.get(alias_for(language)) != current:
            return
        if name not in aliases.values():
            try:
                client.json("DELETE", "/collections/" + quote(name, safe=""))
            except SearchError as error:
                # Another publisher may already have removed this snapshot entry.
                if error.status_code != 404:
                    raise


def prepare_index(client, input_path, language, collection, state_path, base_url=None):
    validate_collection(collection, language)
    if input_path.resolve() == state_path.resolve():
        raise SearchError("Index input and prepared-state paths must be different")
    # A failed rebuild must never leave a previous build's publishable marker.
    if state_path.exists():
        state_path.unlink()
    records = read_records(input_path, language)
    if base_url is not None:
        base_url = validate_url(base_url)
        for record in records:
            if not record["url"].startswith("/"):
                raise SearchError("A base URL requires site-relative search records")
            record["url"] = base_url + record["url"]
    client.json("POST", "/collections", schema_for(collection, language))
    try:
        payload = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in records)
        response = client.request(
            "POST",
            "/collections/"
            + quote(collection, safe="")
            + "/documents/import?action=create",
            payload.encode("utf-8"),
            "text/plain",
        )
        lines = [line for line in response.splitlines() if line.strip()]
        if len(lines) != len(records):
            raise SearchError("Import response count does not match the exported index")
        for number, line in enumerate(lines, 1):
            try:
                result = json.loads(line)
            except ValueError:
                raise SearchError(
                    f"Malformed import response on line {number}"
                ) from None
            if not isinstance(result, dict) or result.get("success") is not True:
                raise SearchError(f"Typesense import rejected document {number}")
        verify_collection(client, collection, language, len(records))
        state = {
            "version": 1,
            "host": client.host,
            "collection": collection,
            "language": language,
            "document_count": len(records),
            "verified": True,
            "prepared_at": datetime.now(UTC).isoformat(),
        }
        write_file(state_path, json.dumps(state, indent=2) + "\n")
    except (SearchError, OSError):
        # Only a collection created by this attempt may be discarded. If creation
        # failed (for example, the name already existed), execution never gets here.
        try:
            if collection not in collection_aliases(client).values():
                client.json("DELETE", "/collections/" + quote(collection, safe=""))
        except SearchError as error:
            print(f"Search cleanup warning: {error}", file=sys.stderr)
        raise
    return state


def publish_index(client, state_path):
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except ValueError:
        raise SearchError("Malformed prepared-state JSON") from None
    if (
        not isinstance(state, dict)
        or state.get("version") != 1
        or state.get("verified") is not True
    ):
        raise SearchError("State does not describe a verified index")
    language = state.get("language")
    collection = validate_collection(state.get("collection"), language)
    count = state.get("document_count")
    if type(count) is not int or count <= 0 or state.get("host") != client.host:
        raise SearchError(
            "State has an invalid count or belongs to another Typesense endpoint"
        )
    metadata = verify_collection(client, collection, language, count)
    alias = alias_for(language)
    # Freeze eligibility before switching. A concurrently published version was
    # still preparing in this snapshot and must survive this build's cleanup.
    try:
        collections = client.json("GET", "/collections", expected_type=list)
    except SearchError as error:
        collections = None
        print(f"Search cleanup warning: {error}", file=sys.stderr)
    current = collection_aliases(client).get(alias)
    if current != collection:
        state["previous_collection"] = current
        # Persist before switching so a retry can still retain the previous index
        # if the alias changed but its response or metadata update failed.
        write_file(state_path, json.dumps(state, indent=2) + "\n")
    previous = state.get("previous_collection")
    if previous is None and current == collection:
        publication = metadata.get("metadata", {}).get("nextgis_docs_search", {})
        previous = publication.get("previous_collection")
    if previous is not None:
        validate_collection(previous, language)
    result = client.json("PUT", "/aliases/" + alias, {"collection_name": collection})
    if result.get("name") != alias or result.get("collection_name") != collection:
        raise SearchError("Typesense returned an unexpected alias response")
    try:
        # Only published versions are eligible for retention cleanup; preparing
        # versions and legacy collections without a marker are left intact.
        collection_metadata = dict(metadata.get("metadata", {}))
        collection_metadata["nextgis_docs_search"] = {
            "language": language,
            "published": True,
            "previous_collection": previous,
        }
        client.json(
            "PATCH",
            "/collections/" + quote(collection, safe=""),
            {"metadata": collection_metadata},
        )
        if collections is not None:
            cleanup_collections(client, language, collection, previous, collections)
    except SearchError as error:
        # HTML and the alias are already published. A failed cleanup must not
        # report that publication failed or roll back a working search index.
        print(f"Search cleanup warning: {error}", file=sys.stderr)
    return state


def browser_config(host, language, key, output=None, endpoint=None, admin_key=None):
    alias = alias_for(language)
    if not isinstance(key, str) or not key:
        raise SearchError("Typesense did not return a search-only key")
    if admin_key and key == admin_key:
        raise SearchError(
            "The browser search key must differ from the administrative key"
        )
    # The browser can use a same-origin reverse proxy such as /typesense, while
    # the importer always connects to an absolute private HTTP endpoint.
    endpoint = validate_url(endpoint or host) or "/"
    config = {
        "endpoint": endpoint,
        "apiKey": key,
        "collection": alias,
        "language": language,
    }
    if output is not None:
        write_file(output, json.dumps(config, indent=2) + "\n")
    return config


def create_search_config(
    client, language, output=None, endpoint=None, existing_key=None
):
    alias = alias_for(language)
    if existing_key:
        key = existing_key
    else:
        response = client.json(
            "POST",
            "/keys",
            {
                "description": f"NextGIS documentation browser search ({language})",
                "actions": ["documents:search"],
                "collections": [alias],
            },
        )
        key = response.get("value")
    return browser_config(client.host, language, key, output, endpoint, client.api_key)


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    commands = result.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser(
        "prepare", help="Import and verify a new physical collection"
    )
    publish = commands.add_parser(
        "publish", help="Switch the language alias after HTML deployment"
    )
    local = commands.add_parser(
        "local", help="Import built Sphinx search records into a local server"
    )
    configure = commands.add_parser(
        "configure", help="Write browser config with a search-only key"
    )
    local.add_argument("build_dir", type=Path)
    prepare.add_argument("--base-url", help="Published documentation site URL")
    for command in (prepare, local, configure):
        command.add_argument("--language", choices=("ru", "en"), required=True)
    for command in (prepare, publish, local, configure):
        command.add_argument(
            "--host", default=os.getenv("TYPESENSE_HOST", "http://127.0.0.1:8108")
        )
        command.add_argument("--timeout", type=float, default=30)
    prepare.add_argument("input", type=Path)
    prepare.add_argument("--collection", required=True)
    prepare.add_argument("--state", type=Path, required=True)
    publish.add_argument("--state", type=Path, required=True)
    local.add_argument("--collection")
    local.add_argument("--config-output", type=Path)
    local.add_argument(
        "--create-search-key",
        action="store_true",
        help="Explicitly print a new search-only key, or save it with --config-output",
    )
    configure.add_argument("--output", type=Path, required=True)
    for command in (local, configure):
        command.add_argument(
            "--search-endpoint",
            default=os.getenv("TYPESENSE_SEARCH_ENDPOINT"),
            help="Public browser endpoint; defaults to the server host",
        )
    return result


def main(argv=None):
    # Local settings come from the project, not the caller's working directory.
    # Explicit process settings from Buildbot remain authoritative.
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    args = parser().parse_args(argv)
    try:
        search_key = os.getenv("TYPESENSE_SEARCH_API_KEY")
        if args.command == "configure" and search_key:
            # A provisioned search-only key lets HTML builds prepare their browser
            # configuration without administrative access to the search server.
            browser_config(
                args.host,
                args.language,
                search_key,
                args.output,
                args.search_endpoint,
                os.getenv("TYPESENSE_API_KEY"),
            )
            print(f"Browser search configuration written to {args.output}")
            return 0
        client = TypesenseClient(
            args.host, os.getenv("TYPESENSE_API_KEY"), args.timeout
        )
        if args.command == "prepare":
            state = prepare_index(
                client,
                args.input,
                args.language,
                args.collection,
                args.state,
                args.base_url,
            )
            print(
                "Verified {} sections in {}".format(
                    state["document_count"], state["collection"]
                )
            )
        elif args.command == "publish":
            state = publish_index(client, args.state)
            print(
                "Published {} sections through {}".format(
                    state["document_count"],
                    alias_for(state["language"]),
                )
            )
        elif args.command == "configure":
            create_search_config(
                client, args.language, args.output, args.search_endpoint
            )
            print(f"Browser search configuration written to {args.output}")
        else:
            collection = (
                args.collection
                or alias_for(args.language) + "_" + uuid.uuid4().hex[:12]
            )
            with tempfile.TemporaryDirectory(prefix="nextgis-search-") as temporary:
                state_path = Path(temporary) / "state.json"
                state = prepare_index(
                    client,
                    args.build_dir / "typesense-docs.jsonl",
                    args.language,
                    collection,
                    state_path,
                )
                publish_index(client, state_path)
            print(
                "Published {} sections through {}".format(
                    state["document_count"], alias_for(args.language)
                )
            )
            if args.config_output is not None or args.create_search_key:
                config = create_search_config(
                    client,
                    args.language,
                    args.config_output,
                    args.search_endpoint,
                    search_key,
                )
                if args.config_output is not None:
                    print(
                        f"Browser search configuration written to {args.config_output}"
                    )
                else:
                    print("Search-only key: " + config["apiKey"])
        return 0
    except (SearchError, OSError) as error:
        # OSError reports local filenames, while server diagnostics are sanitized.
        print(f"Search index error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
