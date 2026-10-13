import hashlib
import json
import os
import tempfile
from pathlib import Path
from urllib.parse import quote, urlsplit

from bs4 import BeautifulSoup
from docutils import nodes
from dotenv import load_dotenv
from sphinx import addnodes
from sphinx.errors import ConfigError
from sphinx.locale import get_translation

PROJECT_ROOT = Path(__file__).resolve().parents[2]
_ = get_translation("sphinx")


def configure_search(app, config):
    settings = {}
    if config.typesense_search_config:
        path = Path(config.typesense_search_config)
        if not path.is_absolute():
            path = Path(app.confdir).parent / path
        try:
            settings = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise ConfigError(f"Cannot read Typesense search config: {path}") from error
        if not isinstance(settings, dict):
            raise ConfigError("Typesense search config must be a JSON object")
        if settings.get("language") != config.language:
            raise ConfigError(
                "Typesense search config language differs from Sphinx language"
            )

    endpoint = config.typesense_search_endpoint or settings.get("endpoint", "")
    key = config.typesense_search_api_key or settings.get("apiKey", "")
    collection = config.typesense_search_collection or settings.get("collection", "")
    if not endpoint and not key:
        config.html_context["typesense_search"] = None
        return
    if (
        not isinstance(endpoint, str)
        or not isinstance(key, str)
        or not endpoint
        or not key
    ):
        raise ConfigError(
            "Typesense search requires an endpoint and a search-only API key"
        )
    if key == os.getenv("TYPESENSE_API_KEY"):
        raise ConfigError(
            "The browser search key must differ from the administrative key"
        )
    if config.language not in ("ru", "en"):
        raise ConfigError("Typesense search supports Sphinx language ru or en")
    parsed = urlsplit(endpoint)
    if (
        not (
            (parsed.scheme in ("http", "https") and parsed.netloc)
            or (endpoint.startswith("/") and not endpoint.startswith("//"))
        )
        or parsed.query
        or parsed.fragment
        or parsed.username
        or parsed.password
    ):
        raise ConfigError(
            "Typesense search endpoint must be an HTTP(S) URL or an absolute path"
        )
    if collection and not isinstance(collection, str):
        raise ConfigError("Typesense search collection must be a string")

    config.html_context["typesense_search"] = {
        "endpoint": endpoint.rstrip("/") or "/",
        "apiKey": key,
        "collection": collection or f"nextgis_docs_search_{config.language}",
        "language": config.language,
    }
    config.html_theme_options["search_as_you_type"] = False


def search_page_context(app, pagename, templatename, context, doctree):
    settings = context.get("typesense_search")
    if not settings:
        return
    context["typesense_search"] = {
        **settings,
        "searchPage": context["pathto"]("search"),
        "labels": {
            "loading": str(_("Searching...")),
            "noResults": str(_("No results found. Try another query.")),
            "error": str(_("Search is unavailable. Please try again.")),
            "results": str(_("Results found: {count}")),
            "more": str(_("View all results")),
            "previous": str(_("Previous page")),
            "next": str(_("Next page")),
            "fallback": str(_("Use offline search")),
        },
    }


def index_path(app, docname):
    return (
        Path(app.doctreedir)
        / "typesense"
        / app.builder.name
        / app.config.language
        / (docname + ".json")
    )


def write_index_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as output:
            temporary = Path(output.name)
            output.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def index_missing_pages(app, env):
    if app.builder.name not in ("html", "dirhtml"):
        return []
    # A pre-existing incremental build may have HTML but no exported records yet.
    return [docname for docname in env.found_docs if not index_path(app, docname).is_file()]


def index_page(app, pagename, templatename, context, doctree):
    if app.builder.name not in ("html", "dirhtml") or doctree is None:
        return
    # Our homepage template replaces the root doctree's body; navigation and
    # helper pages also do not represent searchable documentation articles.
    if (
        pagename in ("index", "sidebar")
        or Path(pagename).name in ("404", "search", "genindex", "py-modindex")
        or "_static" in Path(pagename).parts
    ):
        write_index_file(index_path(app, pagename), "[]")
        return
    uri = app.builder.get_target_uri(pagename)
    path = uri or "index.html"
    title_node = app.env.titles.get(pagename)
    title = title_node.astext() if title_node is not None else pagename
    sections = [("", title, [])]

    def collect(node, content):
        if isinstance(node, (
            nodes.comment, nodes.system_message, nodes.substitution_definition, addnodes.toctree
        )):
            return
        if isinstance(node, nodes.raw):
            if "html" in node.get("format", "").split():
                # Docutils treats raw markup as opaque. Parse only this fragment
                # to retain visible text, never the finished page or its layout.
                fragment = BeautifulSoup(node.astext(), "html.parser")
                for element in fragment.select("script, style, noscript, svg"):
                    element.decompose()
                content.append(fragment.get_text(" ", strip=True))
            return
        if isinstance(node, nodes.Element) and node.get("toctree"):
            return
        if isinstance(node, nodes.section) and node.get("ids"):
            heading = next(
                (child.astext() for child in node.children if isinstance(child, nodes.title)),
                title,
            )
            content = []
            sections.append((node["ids"][0], heading, content))
        if isinstance(node, nodes.title) and isinstance(node.parent, (nodes.section, nodes.document)):
            return
        if isinstance(node, nodes.Text):
            content.append(str(node))
            return
        for child in node.children:
            collect(child, content)

    # This is the resolved tree used by the HTML writer, including includes and
    # HTML-only content. Each text node belongs to its closest section once.
    collect(doctree, sections[0][2])
    records = []
    for anchor, heading, parts in sections:
        content = " ".join(" ".join(parts).split())
        if not content and not anchor:
            continue
        identity = app.config.language + ":" + path + "#" + anchor
        url = "/" + quote(uri, safe="/")
        if anchor:
            url += "#" + quote(anchor, safe="-._~")
        records.append({
            "id": hashlib.sha256(identity.encode("utf-8")).hexdigest()[:24],
            "title": title,
            "heading": heading,
            "content": content,
            "url": url,
            "path": path,
            "language": app.config.language,
        })
    # Writers may run in separate processes; one atomic file per page also keeps
    # unchanged pages available when sphinx-autobuild rewrites only changed ones.
    write_index_file(index_path(app, pagename), json.dumps(records, ensure_ascii=False))


def write_search_index(app, exception):
    # Sphinx assigns the -W exit status after build-finished callbacks run.
    if (
        exception is not None
        or app.statuscode
        or (app._fail_on_warnings and app._warncount)
        or app.builder.name not in ("html", "dirhtml")
    ):
        return
    parents = {
        child: parent
        for parent, children in app.env.toctree_includes.items()
        for child in children
    }
    lines = []
    for docname in sorted(app.env.found_docs):
        ancestors = []
        current = docname
        while current not in ancestors:
            ancestors.append(current)
            if current not in parents:
                break
            current = parents[current]
        # Use Sphinx's parent order; root and sidebar organize products rather
        # than naming one. Resolve this anew so navigation changes affect all pages.
        product = next(
            (name for name in reversed(ancestors) if name not in (app.config.root_doc, "sidebar")),
            None,
        )
        title_node = app.env.titles.get(product)
        section = title_node.astext() if title_node is not None else ""
        records = json.loads(index_path(app, docname).read_text(encoding="utf-8"))
        for record in records:
            record["section"] = section
            lines.append(json.dumps(record, ensure_ascii=False))
    # Only current documents are included, so removed pages cannot survive in
    # the next complete index. Failed builds leave the last successful export.
    write_index_file(Path(app.outdir) / "typesense-docs.jsonl", "\n".join(lines) + "\n")


def setup(app):
    # Load local settings before registering config defaults; CI env takes priority.
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    app.add_config_value(
        "typesense_search_endpoint", os.getenv("TYPESENSE_SEARCH_ENDPOINT", ""), "html"
    )
    app.add_config_value(
        "typesense_search_api_key", os.getenv("TYPESENSE_SEARCH_API_KEY", ""), "html"
    )
    app.add_config_value(
        "typesense_search_collection",
        os.getenv("TYPESENSE_SEARCH_COLLECTION", ""),
        "html",
    )
    app.add_config_value(
        "typesense_search_config", os.getenv("TYPESENSE_SEARCH_CONFIG", ""), "html"
    )
    app.connect("config-inited", configure_search, priority=110)
    app.connect("html-page-context", search_page_context)
    app.connect("html-page-context", index_page)
    app.connect("env-get-updated", index_missing_pages)
    app.connect("build-finished", write_search_index)
    return {
        "version": "1.1",
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
