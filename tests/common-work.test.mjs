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
const guide = JSON.parse(await readFile(new URL("_data/common_work.json", root), "utf8"));
const home = (await readFile(new URL("index.html", root), "utf8")).replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
const engine = new Liquid({ root: fileURLToPath(new URL("_includes/", root)), jekyllInclude: true });
engine.registerFilter("relative_url", path => config.baseurl + path);
const tasks = guide.groups.flatMap(group => group.tasks);
const formats = new Set(["Walkthrough", "Practice", "Explanation", "Task reference", "Investigation"]);

async function render(data = guide) {
  const html = await engine.parseAndRender(home, {
    site: { ...config, data: { course, common_work: data } },
  });
  return parseHTML(html).document;
}

test("task finder data resolves to complete existing lessons with honest practice labels", async () => {
  assert.ok(guide.groups.length > 0);
  assert.equal(new Set(guide.groups.map(group => group.id)).size, guide.groups.length);
  assert.equal(new Set(tasks.map(task => task.id)).size, tasks.length);
  for (const group of guide.groups) {
    assert.match(group.id, /^[a-z][a-z0-9-]*$/);
    assert.ok(group.title.trim() && group.tasks.length);
    for (const task of group.tasks) {
      assert.match(task.id, /^[a-z][a-z0-9-]*$/);
      assert.ok(task.label.trim() && task.description.trim());
      assert.ok(formats.has(task.format));
      const lesson = course.lessons.find(item => item.id === task.lesson);
      assert.ok(lesson, "Missing lesson: " + task.lesson);
      assert.equal(task.format === "Practice", lesson.route === "practice");
      assert.equal(Object.hasOwn(task, "url"), false, "URLs belong to the manifest");
      const source = await readFile(new URL(lesson.source, root), "utf8");
      assert.match(source, /^# /m);
      assert.ok(source.split(/\s+/).length > 200, "Destination must be authored: " + task.lesson);
    }
  }
});

test("task finder starts closed and renders each task with its manifest URL and format", async () => {
  const doc = await render();
  const panel = doc.querySelector("#common-work");
  assert.equal(panel.localName, "details");
  assert.equal(panel.firstElementChild.localName, "summary");
  assert.equal(panel.hasAttribute("open"), false);
  assert.equal(panel.querySelector("nav").getAttribute("aria-label"), "Find lessons by certification task");
  const groups = [...panel.querySelectorAll(".work-group")];
  assert.equal(groups.length, guide.groups.length);
  for (const [index, group] of groups.entries()) {
    assert.equal(group.localName, "details");
    assert.equal(group.hasAttribute("open"), false);
    assert.equal(group.hasAttribute("name"), false);
    assert.equal(group.firstElementChild.textContent.trim(), guide.groups[index].title);
  }
  const entries = [...panel.querySelectorAll(".work-tasks > li")];
  assert.equal(entries.length, tasks.length);
  for (const [index, entry] of entries.entries()) {
    const task = tasks[index];
    const lesson = course.lessons.find(item => item.id === task.lesson);
    assert.equal(entry.querySelector("a").getAttribute("href"), config.baseurl + lesson.url);
    assert.equal(entry.querySelector("a").textContent, task.label);
    assert.equal(entry.querySelector(".work-kind").textContent, task.format);
    assert.equal(entry.querySelector("p").textContent, task.description);
  }
});

test("task entry preserves the main Start link and every existing reading-route list", async () => {
  const doc = await render();
  const first = course.lessons.find(lesson => lesson.route === "core");
  assert.equal(doc.querySelector(".start-link").getAttribute("href"), config.baseurl + first.url);
  const all = [...doc.querySelectorAll(".course-lessons > li h3 a")].map(link => link.getAttribute("href"));
  assert.equal(all.length, course.lessons.length);
  assert.equal(new Set(all).size, course.lessons.length);
  for (const route of course.reading_routes) {
    const selector = route.id === "core" ? ".course-module .course-lessons h3 a" : "#" + route.id + " .course-lessons h3 a";
    const links = [...doc.querySelectorAll(selector)].map(link => link.getAttribute("href"));
    assert.deepEqual(links, course.lessons.filter(lesson => lesson.route === route.id).map(lesson => config.baseurl + lesson.url));
  }
});

test("missing or empty task data leaves the complete lesson lists without an empty finder", async () => {
  for (const data of [null, {}, { groups: [] }]) {
    const doc = await render(data);
    assert.equal(doc.querySelector("#common-work"), null);
    assert.equal(doc.querySelectorAll(".course-lessons > li").length, course.lessons.length);
    assert.ok(doc.querySelector(".start-link"));
  }
});
