function wrapTables(): void {
  const tables = document.querySelectorAll<HTMLTableElement>(
    ".bd-article table, .document table",
  );

  tables.forEach((table) => {
    if (table.parentElement?.classList.contains("table-wrapper")) return;

    const wrapper = document.createElement("div");
    wrapper.className = "table-wrapper";

    table.parentNode?.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });
}

function initExternalLinks(): void {
  const links = document.querySelectorAll<HTMLAnchorElement>('a[href^="http"]');

  links.forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) return;

    const isExternal = !href.includes(window.location.hostname);
    if (!isExternal) return;

    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
  });
}

function syncThemeAwareImages(): void {
  const isDarkTheme = document.documentElement.dataset.theme === "dark";
  const images = document.querySelectorAll<HTMLImageElement>(
    "img[data-src-light], img[data-src-dark]",
  );

  images.forEach((image) => {
    const nextSrc = isDarkTheme
      ? image.dataset.srcDark ?? image.dataset.srcLight ?? null
      : image.dataset.srcLight ?? image.dataset.srcDark ?? null;

    if (!nextSrc || image.getAttribute("src") === nextSrc) return;

    image.setAttribute("src", nextSrc);
  });
}

function initThemeAwareImages(): void {
  syncThemeAwareImages();

  const observer = new MutationObserver((mutations) => {
    const changedTheme = mutations.some(
      (mutation) =>
        mutation.type === "attributes" &&
        mutation.attributeName === "data-theme" &&
        mutation.target === document.documentElement,
    );

    if (changedTheme) {
      syncThemeAwareImages();
    }
  });

  observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"],
  });
}

function initApp(): void {
  wrapTables();
  initExternalLinks();
  initThemeAwareImages();
  document.querySelector<HTMLAnchorElement>(".notfound-back a")?.addEventListener(
    "click",
    (event) => {
      event.preventDefault();
      history.back();
    },
  );
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initApp, { once: true });
} else {
  initApp();
}
