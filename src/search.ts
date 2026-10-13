interface SearchConfig {
  endpoint: string;
  apiKey: string;
  collection: string;
  searchPage: string;
  language: string;
  labels: {
    loading: string;
    noResults: string;
    error: string;
    results: string;
    more: string;
    previous: string;
    next: string;
    fallback: string;
  };
}

interface SearchHit {
  document: {
    section?: string;
    title?: string;
    heading?: string;
    content?: string;
    url?: string;
    path?: string;
  };
  highlight?: { content?: { snippet?: string } };
  highlights?: Array<{ field: string; snippet?: string }>;
}

interface SearchResponse {
  found: number;
  hits: SearchHit[];
}

const highlightStart = "\uE000";
const highlightEnd = "\uE001";
const pageSize = 10;

function readConfig(): SearchConfig | null {
  const node = document.getElementById("typesense-search-config");
  if (!node?.textContent) return null;
  try {
    const config = JSON.parse(node.textContent) as SearchConfig;
    if (
      typeof config.endpoint !== "string" ||
      typeof config.apiKey !== "string" ||
      typeof config.collection !== "string" ||
      typeof config.searchPage !== "string" ||
      !config.labels
    ) return null;
    return config;
  } catch {
    return null;
  }
}

function searchUrl(config: SearchConfig, query: string, page = 1): URL {
  const url = new URL(config.searchPage, document.baseURI);
  url.searchParams.set("q", query);
  if (page > 1) url.searchParams.set("page", String(page));
  else url.searchParams.delete("page");
  url.searchParams.delete("search");
  return url;
}

function resultUrl(config: SearchConfig, value: unknown): string | null {
  if (typeof value !== "string" || !value) return null;
  try {
    // Exported paths are relative to the documentation root, also from nested pages.
    const url = new URL(value, new URL(config.searchPage, document.baseURI));
    return url.protocol === "https:" || url.protocol === "http:"
      ? url.href
      : null;
  } catch {
    return null;
  }
}

function appendSnippet(node: HTMLElement, snippet: string): void {
  // Typesense adds these delimiters; all corpus text remains inert text.
  let highlighted = false;
  snippet.split(/([\uE000\uE001])/).forEach((part) => {
    if (part === highlightStart) highlighted = true;
    else if (part === highlightEnd) highlighted = false;
    else if (highlighted) {
      const mark = document.createElement("mark");
      mark.textContent = part;
      node.appendChild(mark);
    } else node.appendChild(document.createTextNode(part));
  });
}

function renderHits(container: HTMLElement, hits: SearchHit[], config: SearchConfig): void {
  const list = document.createElement("ul");
  list.className = "typesense-search-list";
  hits.forEach((hit) => {
    const record = hit.document;
    if (!record) return;
    const href = resultUrl(config, record.url || record.path);
    if (!href) return;
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = href;
    link.className = "typesense-search-result";
    const header = document.createElement("span");
    header.className = "typesense-search-header";
    const title = document.createElement("span");
    title.className = "typesense-search-title";
    title.textContent = record.title || record.heading || record.path || href;
    header.appendChild(title);
    if (record.section && record.section !== record.title) {
      const section = document.createElement("span");
      section.className = "typesense-search-section";
      section.textContent = record.section;
      header.appendChild(section);
    }
    link.appendChild(header);
    if (record.heading && record.heading !== record.title) {
      const heading = document.createElement("span");
      heading.className = "typesense-search-heading";
      heading.textContent = record.heading;
      link.appendChild(heading);
    }
    const snippet = hit.highlight?.content?.snippet ||
      hit.highlights?.find((entry) => entry.field === "content")?.snippet;
    const content = typeof snippet === "string"
      ? snippet
      : typeof record.content === "string" ? record.content.slice(0, 240) : "";
    if (content) {
      const context = document.createElement("span");
      context.className = "typesense-search-context";
      appendSnippet(context, content);
      link.appendChild(context);
    }
    item.appendChild(link);
    list.appendChild(item);
  });
  container.appendChild(list);
}

function setStatus(container: HTMLElement, message: string): void {
  container.replaceChildren();
  const status = document.createElement("p");
  status.className = "typesense-search-status";
  status.setAttribute("role", "status");
  status.textContent = message;
  container.appendChild(status);
}

function renderError(container: HTMLElement, config: SearchConfig, query: string): void {
  setStatus(container, config.labels.error);
  const fallback = document.createElement("a");
  const url = searchUrl(config, query);
  url.searchParams.set("search", "local");
  fallback.href = url.href;
  fallback.className = "typesense-search-fallback";
  fallback.textContent = config.labels.fallback;
  container.appendChild(fallback);
}

function resultCount(config: SearchConfig, found: number): string {
  const count = found.toLocaleString(config.language || document.documentElement.lang);
  return config.labels.results.replace("{count}", count);
}

function createSearch(
  config: SearchConfig,
  perPage: number,
  onResult: (response: SearchResponse, query: string, page: number) => void,
  onError: (query: string) => void,
): { run: (query: string, page: number) => Promise<void>; cancel: () => void } {
  let controller: AbortController | null = null;
  let sequence = 0;
  const cancel = (): void => {
    sequence += 1;
    controller?.abort();
    controller = null;
  };
  const run = async (query: string, page: number): Promise<void> => {
    cancel();
    const request = sequence;
    const activeController = new AbortController();
    controller = activeController;
    const timeout = window.setTimeout(() => activeController.abort(), 8000);
    try {
      const endpoint = new URL(config.endpoint.replace(/\/+$/, "") + "/", document.baseURI);
      const url = new URL(
        `collections/${encodeURIComponent(config.collection)}/documents/search`,
        endpoint,
      );
      url.search = new URLSearchParams({
        q: query,
        query_by: "heading,title,content",
        query_by_weights: "10,5,1",
        num_typos: "2",
        drop_tokens_threshold: "0",
        include_fields: "section,title,heading,content,url,path",
        highlight_fields: "content",
        highlight_affix_num_tokens: "8",
        highlight_start_tag: highlightStart,
        highlight_end_tag: highlightEnd,
        page: String(page),
        per_page: String(perPage),
      }).toString();
      const response = await fetch(url, {
        headers: { "X-TYPESENSE-API-KEY": config.apiKey },
        signal: activeController.signal,
      });
      if (!response.ok) throw new Error("Search request failed");
      const result = await response.json() as SearchResponse;
      if (!Array.isArray(result.hits) || !Number.isFinite(result.found) || result.found < 0) {
        throw new Error("Invalid search response");
      }
      if (request === sequence) onResult(result, query, page);
    } catch {
      if (request === sequence) onError(query);
    } finally {
      window.clearTimeout(timeout);
      if (request === sequence) controller = null;
    }
  };
  return { run, cancel };
}

function initPreview(form: HTMLFormElement, config: SearchConfig, index: number): void {
  const input = form.querySelector<HTMLInputElement>('input[name="q"]');
  if (!input) return;
  const preview = document.createElement("div");
  preview.id = `typesense-search-preview-${index}`;
  preview.className = "typesense-search-preview";
  preview.hidden = true;
  form.insertAdjacentElement("afterend", preview);
  input.setAttribute("aria-controls", preview.id);
  input.setAttribute("aria-expanded", "false");
  let timer: number | undefined;
  const show = (): void => {
    preview.hidden = false;
    input.setAttribute("aria-expanded", "true");
  };
  const search = createSearch(config, 5, (response, query) => {
    setStatus(preview, response.found ? resultCount(config, response.found) : config.labels.noResults);
    renderHits(preview, response.hits, config);
    if (response.found) {
      const more = document.createElement("a");
      more.className = "typesense-search-more";
      more.href = searchUrl(config, query).href;
      more.textContent = config.labels.more;
      preview.appendChild(more);
    }
    show();
  }, (query) => {
    renderError(preview, config, query);
    show();
  });
  const clear = (): void => {
    window.clearTimeout(timer);
    search.cancel();
    preview.replaceChildren();
    preview.hidden = true;
    input.setAttribute("aria-expanded", "false");
  };
  input.addEventListener("input", () => {
    clear();
    const query = input.value.trim();
    if (!query || input.matches(":disabled")) return;
    setStatus(preview, config.labels.loading);
    show();
    timer = window.setTimeout(() => void search.run(query, 1), 200);
  });
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = input.value.trim();
    if (query) window.location.assign(searchUrl(config, query));
    else clear();
  });
  const keyboard = (event: KeyboardEvent): void => {
    if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
    const links = Array.from(preview.querySelectorAll<HTMLAnchorElement>("a[href]"));
    if (preview.hidden || !links.length) return;
    const active = links.findIndex((link) => link === document.activeElement);
    event.preventDefault();
    const next = event.key === "ArrowDown"
      ? active + 1
      : active < 0 ? links.length - 1 : active - 1;
    if (next < 0 || next >= links.length) input.focus();
    else links[next].focus();
  };
  input.addEventListener("keydown", keyboard);
  preview.addEventListener("keydown", keyboard);
  const dialog = form.closest<HTMLDialogElement>("#pst-search-dialog");
  dialog?.addEventListener("close", clear);
  preview.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      if (dialog?.open) dialog.close();
      else {
        clear();
        input.focus();
      }
    }
  });
}

function initSearchPage(config: SearchConfig): void {
  const form = document.querySelector<HTMLFormElement>("#typesense-search-form");
  const container = document.getElementById("typesense-search-results");
  const input = form?.querySelector<HTMLInputElement>('input[name="q"]');
  if (!form || !container || !input) return;
  const showPage = (query: string, page: number, push = false): void => {
    input.value = query;
    if (push) history.pushState(null, "", searchUrl(config, query, page));
    if (!query) {
      search.cancel();
      container.replaceChildren();
      container.setAttribute("aria-busy", "false");
      return;
    }
    setStatus(container, config.labels.loading);
    container.setAttribute("aria-busy", "true");
    void search.run(query, page);
  };
  const search = createSearch(config, pageSize, (response, query, page) => {
    const pages = Math.ceil(response.found / pageSize);
    if (pages > 0 && page > pages) {
      history.replaceState(null, "", searchUrl(config, query, pages));
      showPage(query, pages);
      return;
    }
    container.setAttribute("aria-busy", "false");
    setStatus(container, response.found ? resultCount(config, response.found) : config.labels.noResults);
    renderHits(container, response.hits, config);
    if (pages <= 1) return;
    const navigation = document.createElement("div");
    navigation.className = "typesense-search-pagination";
    const addButton = (label: string, target: number, disabled: boolean): void => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "btn btn-outline-primary";
      button.textContent = label;
      button.disabled = disabled;
      button.addEventListener("click", () => {
        showPage(query, target, true);
        input.focus({ preventScroll: true });
        form.scrollIntoView({ block: "start", behavior: "smooth" });
      });
      navigation.appendChild(button);
    };
    addButton(config.labels.previous, page - 1, page <= 1);
    const counter = document.createElement("span");
    counter.className = "typesense-search-page-number";
    counter.textContent = `${page} / ${pages}`;
    navigation.appendChild(counter);
    addButton(config.labels.next, page + 1, page >= pages);
    container.appendChild(navigation);
  }, (query) => {
    container.setAttribute("aria-busy", "false");
    renderError(container, config, query);
  });
  const fromLocation = (): void => {
    const params = new URLSearchParams(window.location.search);
    const rawPage = Number(params.get("page") || 1);
    const page = Number.isSafeInteger(rawPage) && rawPage > 0 ? rawPage : 1;
    showPage((params.get("q") || "").trim(), page);
  };
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    showPage(input.value.trim(), 1, true);
  });
  window.addEventListener("popstate", fromLocation);
  fromLocation();
  input.focus();
}

export function initTypesenseSearch(): void {
  const config = readConfig();
  if (!config) return;
  const local = new URLSearchParams(window.location.search).get("search") === "local";
  const customPage = document.getElementById("typesense-search-page");
  const nativePage = document.getElementById("typesense-native-search");
  if (local) customPage?.remove();
  else if (customPage) customPage.hidden = false;
  if (nativePage) nativePage.hidden = !local;
  if (local) {
    document.querySelectorAll<HTMLFormElement>("form.bd-search").forEach((form) => {
      const field = document.createElement("input");
      field.type = "hidden";
      field.name = "search";
      field.value = "local";
      form.appendChild(field);
    });
    return;
  }
  document.querySelectorAll<HTMLFormElement>("form.bd-search").forEach((form, index) => {
    if (form.id !== "typesense-search-form" && !form.closest("#typesense-native-search")) {
      initPreview(form, config, index);
    }
  });
  initSearchPage(config);
}
