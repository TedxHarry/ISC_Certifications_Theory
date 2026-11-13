import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { Liquid } from "liquidjs";
import { parseHTML } from "linkedom";
import { parse } from "yaml";

const root = new URL("../", import.meta.url);
const config = parse(await readFile(new URL("_config.yml", root), "utf8"));
const course = parse(await readFile(new URL("_data/course.yml", root), "utf8"));
const template = await readFile(new URL("_layouts/default.html", root), "utf8");
const engine = new Liquid({
  root: fileURLToPath(new URL("_includes/", root)),
  jekyllInclude: true,
});
engine.registerFilter("relative_url", (path) => config.baseurl + path);

async function renderNavigation(path) {
  const html = await engine.parseAndRender(template, {
    site: { ...config, data: { course } },
    page: { path, title: "Navigation test" },
    content: "<h1>Reading content stays available</h1>",
  });
  return parseHTML(html).document;
}

test("every direct lesson opens only its own main module or reference/practice group", async () => {
  for (const lesson of course.lessons) {
    const doc = await renderNavigation(lesson.source);
    const modules = [...doc.querySelectorAll("details.nav-module")];
    const mainModules = course.modules.filter(module => course.lessons.some(
      item => item.route === "core" && item.module === module.id));
    assert.equal(modules.length, mainModules.length + course.reading_routes.filter(route => route.id !== "core").length);
    const openModules = modules.filter((module) => module.hasAttribute("open"));
    assert.equal(openModules.length, 1);
    assert.equal(openModules[0].querySelector("summary").id, "nav-" + (lesson.route === "core" ? lesson.module : lesson.route));
    assert.equal(
      openModules[0].querySelector('a[aria-current="page"]').getAttribute("href"),
      config.baseurl + lesson.url,
    );
  }
});

test("home opens the first module without marking a lesson as current", async () => {
  const doc = await renderNavigation("index.html");
  const openModules = [...doc.querySelectorAll("details.nav-module[open]")];
  assert.equal(openModules.length, 1);
  assert.equal(openModules[0].querySelector("summary").id, "nav-" + course.modules[0].id);
  assert.equal(doc.querySelectorAll('[aria-current="page"]').length, 0);
});

test("disclosures keep every lesson reachable exactly once, without empty main modules", async () => {
  const doc = await renderNavigation(course.lessons.at(-1).source);
  const allLinks = [...doc.querySelectorAll(".lesson-nav a")].map(a => a.getAttribute("href"));
  assert.equal(allLinks.length, course.lessons.length);
  assert.equal(new Set(allLinks).size, allLinks.length);
  assert.deepEqual([...allLinks].sort(), course.lessons.map(l => config.baseurl + l.url).sort());
  for (const module of course.modules) {
    const expected = course.lessons.filter(l => l.route === "core" && l.module === module.id);
    const group = doc.querySelector("#nav-" + module.id)?.parentElement;
    if (!expected.length) { assert.equal(group, undefined); continue; }
    assert.equal(group?.localName, "details");
    assert.equal(group.firstElementChild.localName, "summary");
    assert.equal(group.hasAttribute("name"), false);
    assert.deepEqual([...group.querySelectorAll("a")].map(a => a.getAttribute("href")),
      expected.map(l => config.baseurl + l.url));
  }
  for (const route of course.reading_routes.filter(r => r.id !== "core")) {
    const group = doc.querySelector("#nav-" + route.id)?.parentElement;
    assert.equal(group?.localName, "details");
    assert.equal(group.hasAttribute("name"), false);
    assert.deepEqual([...group.querySelectorAll("a")].map(a => a.getAttribute("href")),
      course.lessons.filter(l => l.route === route.id).map(l => config.baseurl + l.url));
  }
});

test("the whole panel has an always-reachable native disclosure outside its scroll region", async () => {
  const doc = await renderNavigation(course.lessons.at(-1).source);
  const panel = doc.querySelector("details.course-navigation");
  assert.equal(panel?.firstElementChild.localName, "summary");
  assert.match(panel.firstElementChild.textContent, /Show lessons/);
  assert.match(panel.firstElementChild.textContent, /Hide lessons/);
  assert.ok(panel.querySelector(".navigation-scroll > nav"));
  assert.equal(panel.firstElementChild.closest(".navigation-scroll"), null);
  assert.ok(doc.querySelector("#main h1"));
});

test("every lesson belongs to one known nonempty reading route and keeps its permanent URL", () => {
  const ids = course.reading_routes.map(r => r.id);
  assert.equal(new Set(ids).size, ids.length);
  assert.ok(ids.includes("core"));
  assert.equal(new Set(course.lessons.map(l => l.id)).size, course.lessons.length);
  assert.equal(new Set(course.lessons.map(l => l.url)).size, course.lessons.length);
  for (const lesson of course.lessons) {
    assert.ok(ids.includes(lesson.route), lesson.id + " unknown route");
    assert.equal(lesson.url, "/" + lesson.source.replace(/\.md$/, ".html"));
  }
  for (const id of ids) assert.ok(course.lessons.some(l => l.route === id), id + " empty route");
});

test("Next and Previous stay in the current reading route, including every boundary", async () => {
  const lessonTemplate = await readFile(new URL("_layouts/lesson.html", root), "utf8");
  for (const lesson of course.lessons) {
    const route = course.lessons.filter(l => l.route === lesson.route);
    const index = route.findIndex(l => l.id === lesson.id);
    const expected = [route[index - 1], route[index + 1]].filter(Boolean)
      .map(l => config.baseurl + l.url);
    const html = await engine.parseAndRender(lessonTemplate, {
      site: { ...config, data: { course } }, page: { path: lesson.source }, content: "<h1>Lesson</h1>",
    });
    const doc = parseHTML(html).document;
    assert.deepEqual([...doc.querySelectorAll(".lesson-pagination a")].map(a => a.getAttribute("href")),
      expected, lesson.id);
  }
});

test("home separates the main route from collapsed task references and practice", async () => {
  const homeTemplate = await readFile(new URL("index.html", root), "utf8");
  const html = await engine.parseAndRender(homeTemplate, { site: { ...config, data: { course } } });
  const doc = parseHTML(html).document;
  const main = course.lessons.filter(l => l.route === "core");
  assert.deepEqual([...doc.querySelectorAll(".course-module .course-lessons h3 a")].map(a => a.getAttribute("href")),
    main.map(l => config.baseurl + l.url));
  assert.equal(doc.querySelector(".start-link").getAttribute("href"), config.baseurl + main[0].url);
  for (const route of course.reading_routes.filter(r => r.id !== "core")) {
    const group = doc.querySelector("#" + route.id);
    assert.equal(group.localName, "details");
    assert.equal(group.firstElementChild.localName, "summary");
    assert.equal(group.hasAttribute("open"), false);
    assert.deepEqual([...group.querySelectorAll("h3 a")].map(a => a.getAttribute("href")),
      course.lessons.filter(l => l.route === route.id).map(l => config.baseurl + l.url));
  }
  assert.equal(doc.querySelectorAll(".course-lessons > li").length, course.lessons.length);
});
