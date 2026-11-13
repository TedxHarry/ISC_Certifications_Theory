import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import {parseHTML} from "linkedom";
import {Liquid} from "liquidjs";
const source = await readFile(new URL("../assets/term-help.js", import.meta.url), "utf8");
const glossary = JSON.parse(await readFile(new URL("../_data/term_help.json", import.meta.url), "utf8"));
function fixture(data = glossary) {
  const {document, window} = parseHTML(`<html><body>
    <nav>Account correlation</nav><article class="lesson-content">
    <h2>Account correlation</h2><p><strong>Account correlation</strong> associates an account.
    This account has an access profile. We limit the selection.
    <a href="#other">Account correlation</a> <code>Account correlation</code></p>
    <pre>Account correlation</pre><p><strong>Provisioning</strong> changes access.</p>
    </article><script id="term-help-data" type="application/json"></script></body></html>`);
  document.querySelector("#term-help-data").textContent = typeof data === "string" ? data : JSON.stringify(data);
  window.innerWidth = 1024; window.innerHeight = 768;
  const article = document.querySelector("article");
  const original = article.textContent;
  const run = () => vm.runInNewContext(source, {document, window});
  run();
  return {document, window, article, original, run,
    tip: document.querySelector("#term-help-tooltip"),
    button: document.querySelector("button.term-help")};
}
function send(target, window, type, values = {}) {
  const event = new window.Event(type, {bubbles:true, cancelable:true});
  for (const [key, value] of Object.entries(values)) Object.defineProperty(event, key, {value});
  target.dispatchEvent(event);
  return event;
}
test("term help preserves lesson text and avoids links, headings, code and ambiguous ordinary words", () => {
  const f = fixture();
  assert.equal(f.article.textContent, f.original);
  assert.equal(f.button.textContent, "Account correlation");
  assert.equal(f.document.querySelectorAll("nav button, h2 button, a button, code button, pre button").length, 0);
  assert.equal([...f.article.querySelectorAll("button")].some(b => ["account","limit"].includes(b.textContent)), false);
  assert.ok([...f.article.querySelectorAll("button")].some(b => b.textContent === "access profile"));
  for (const name of ["pointerover","mouseover","focus","click"]) send(f.button, f.window, name);
  assert.equal(f.tip.hidden, true);
  f.run();
  assert.equal(f.document.querySelectorAll("#term-help-tooltip").length, 1);
  assert.equal(f.article.textContent, f.original);
});
test("pointer help closes on release outside the term, cancellation and lost capture", () => {
  for (const end of ["pointerup","pointercancel","lostpointercapture"]) {
    const f = fixture();
    send(f.button, f.window, "pointerdown", {button:0,pointerId:7,isPrimary:true});
    assert.equal(f.tip.hidden, false);
    assert.equal(f.button.getAttribute("aria-describedby"), f.tip.id);
    assert.match(f.tip.textContent, /appropriate identity/);
    send(end === "lostpointercapture" ? f.button : f.window, f.window, end, {pointerId:7});
    assert.equal(f.tip.hidden, true);
    assert.equal(f.button.hasAttribute("aria-describedby"), false);
  }
  const f = fixture();
  send(f.button, f.window, "pointerdown", {button:2,pointerId:7});
  assert.equal(f.tip.hidden, true);
});
test("keyboard help lasts only while Space or Enter is held and clears on interruption", () => {
  for (const key of [" ","Enter"]) {
    const f = fixture();
    const down = send(f.button, f.window, "keydown", {key,repeat:false});
    assert.equal(down.defaultPrevented, true);
    assert.equal(f.tip.hidden, false);
    send(f.window, f.window, "keyup", {key});
    assert.equal(f.tip.hidden, true);
  }
  for (const name of ["blur","resize","scroll","visibilitychange","focusout","Escape"]) {
    const f = fixture();
    send(f.button, f.window, "keydown", {key:" ",repeat:false});
    const target = name === "visibilitychange" ? f.document : name === "focusout" ? f.button : f.window;
    send(target, f.window, name === "Escape" ? "keydown" : name, {key:"Escape"});
    assert.equal(f.tip.hidden, true, name);
  }
});
test("missing or invalid help data leaves ordinary reading available", () => {
  for (const data of ["invalid", null, []]) {
    const f = fixture(data);
    assert.equal(f.article.textContent, f.original);
    assert.equal(f.document.querySelectorAll("button.term-help").length, 0);
    assert.equal(f.tip, null);
  }
});
test("public term meanings have unique labels, plain text and no source or lesson links", () => {
  const seen = new Set();
  for (const entry of glossary) {
    assert.ok(entry.term.trim() && entry.meaning.trim());
    assert.ok(!/[<>]|https?:\/\//.test(entry.meaning));
    for (const label of [entry.term,...entry.aliases]) {
      const key = label.toLowerCase();
      assert.ok(!seen.has(key), "ambiguous alias: " + label);
      seen.add(key);
    }
  }
});

test("lesson layout embeds the public dictionary and versions reader assets for a new build", async () => {
  const engine = new Liquid();
  engine.registerFilter("relative_url", value => "/ISC_Certifications_Theory" + value);
  const site = {time:new Date("2026-11-13T00:00:00Z"),data:{term_help:glossary,course:{lessons:[]}}};
  const template = (await readFile(new URL("../_layouts/lesson.html", import.meta.url), "utf8"))
    .replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
  const doc = parseHTML(await engine.parseAndRender(template,{site,page:{path:"lesson.md"},content:"<p>Reading stays available</p>"})).document;
  assert.deepEqual(JSON.parse(doc.querySelector("#term-help-data").textContent),glossary);
  assert.match(doc.querySelector("script[src]").getAttribute("src"), /^\/ISC_Certifications_Theory\/assets\/term-help\.js\?v=\d+$/);
  const shared = await readFile(new URL("../_layouts/default.html", import.meta.url),"utf8");
  const style = shared.match(/<link rel="stylesheet"[^>]+>/)[0];
  const rendered = await engine.parseAndRender(style,{site});
  assert.match(rendered,/site\.css\?v=\d+/);
});
