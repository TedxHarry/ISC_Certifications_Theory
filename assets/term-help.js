(() => {
  "use strict";
  const article = document.querySelector(".lesson-content");
  const data = document.querySelector("#term-help-data");
  if (!article || !data || article.dataset.termHelpReady) return;
  let entries;
  try { entries = JSON.parse(data.textContent); } catch { return; }
  if (!Array.isArray(entries)) return;
  const definitions = new Map();
  const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  for (const entry of entries) {
    if (!entry.term || !entry.meaning) continue;
    for (const label of [entry.term, ...(entry.aliases || [])]) {
      definitions.set(label.toLocaleLowerCase("en"), entry);
    }
  }
  if (!definitions.size) return;
  const pattern = new RegExp("(?<![\\p{L}\\p{N}_-])(" +
    [...definitions.keys()].sort((a, b) => b.length - a.length).map(escape).join("|") +
    ")(?![\\p{L}\\p{N}_-])", "giu");
  const walker = document.createTreeWalker(article, 4);
  const nodes = [];
  while (walker.nextNode()) {
    const node = walker.currentNode;
    if (!node.parentElement.closest("p, li, td") ||
        node.parentElement.closest("a, button, code, pre, script, style, h1, h2, h3")) continue;
    nodes.push(node);
  }
  for (const node of nodes) {
    const fragment = document.createDocumentFragment();
    let end = 0;
    for (const match of node.textContent.matchAll(pattern)) {
      // A single ordinary word is ambiguous unless the author marked it as a term.
      // Specific multiword phrases and API role codes can also be recognized in prose.
      const entry = definitions.get(match[0].toLocaleLowerCase("en"));
      if (!node.parentElement.closest("strong") &&
          !/[\s-]/.test(match[0]) && !/^[A-Z_]{3,}$/.test(match[0])) continue;
      fragment.append(document.createTextNode(node.textContent.slice(end, match.index)));
      const button = document.createElement("button");
      button.type = "button";
      button.className = "term-help";
      button.textContent = match[0];
      button.setAttribute("aria-label", match[0] + ". Hold to read its meaning.");
      button.dataset.termMeaning = entry.meaning;
      button.dataset.termName = entry.term;
      fragment.append(button);
      end = match.index + match[0].length;
    }
    if (end) {
      fragment.append(document.createTextNode(node.textContent.slice(end)));
      node.replaceWith(fragment);
    }
  }
  article.dataset.termHelpReady = "true";
  const tip = document.createElement("div");
  tip.id = "term-help-tooltip";
  tip.className = "term-help-tooltip";
  tip.setAttribute("role", "tooltip");
  tip.hidden = true;
  const title = document.createElement("strong");
  const meaning = document.createElement("span");
  tip.append(title, meaning);
  document.body.append(tip);
  let active = null;
  function close() {
    if (active) active.button.removeAttribute("aria-describedby");
    active = null;
    tip.hidden = true;
  }
  function show(button, input) {
    close();
    active = {button, ...input};
    title.textContent = button.dataset.termName;
    meaning.textContent = button.dataset.termMeaning;
    button.setAttribute("aria-describedby", tip.id);
    tip.hidden = false;
    const anchor = button.getBoundingClientRect();
    const box = tip.getBoundingClientRect();
    const width = document.documentElement.clientWidth || window.innerWidth;
    const height = window.innerHeight;
    const left = Math.max(12, Math.min(anchor.left, width - box.width - 12));
    const preferredTop = anchor.top >= box.height + 20 ?
      anchor.top - box.height - 8 : anchor.bottom + 8;
    tip.style.left = left + "px";
    tip.style.top = Math.max(12, Math.min(preferredTop, height - box.height - 12)) + "px";
  }
  article.addEventListener("pointerdown", event => {
    const button = event.target.closest(".term-help");
    if (!button || event.button !== 0 || event.isPrimary === false) return;
    show(button, {pointerId: event.pointerId});
    try { button.setPointerCapture(event.pointerId); } catch { /* Window release remains a fallback. */ }
  });
  const releasePointer = event => {
    if (active && active.pointerId === event.pointerId) close();
  };
  window.addEventListener("pointerup", releasePointer);
  window.addEventListener("pointercancel", releasePointer);
  article.addEventListener("lostpointercapture", releasePointer);
  article.addEventListener("click", event => {
    if (event.target.closest(".term-help")) event.preventDefault();
  });
  article.addEventListener("contextmenu", event => {
    if (event.target.closest(".term-help")) event.preventDefault();
  });
  article.addEventListener("keydown", event => {
    const button = event.target.closest(".term-help");
    if (!button || ![" ", "Enter"].includes(event.key)) return;
    event.preventDefault();
    if (!event.repeat) show(button, {key: event.key});
  });
  window.addEventListener("keyup", event => {
    if (active && active.key === event.key) { event.preventDefault(); close(); }
  });
  window.addEventListener("keydown", event => { if (event.key === "Escape") close(); });
  document.addEventListener("focusout", event => {
    if (active && event.target === active.button) close();
  });
  window.addEventListener("blur", close);
  window.addEventListener("resize", close);
  window.addEventListener("scroll", close, true);
  document.addEventListener("visibilitychange", close);
})();
