import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const testsDirectory = fileURLToPath(new URL("./", import.meta.url));

test("published-content verification requires a closed native answer, its text and its label", async t => {
  const fixture = await mkdtemp(path.join(testsDirectory, ".site-verification-"));
  let mode = "complete";
  const baseurl = "/test-course";
  const lessonURL = baseurl + "/lessons/practice.html";
  const answer = "The decision is final, but export is still present.";
  const label = "Compare your reasoning";
  const server = createServer((request, response) => {
    if (request.url === lessonURL) {
      response.setHeader("Content-Type", "text/html");
      response.end('<article class="lesson-content"><h1>Practice a review</h1>' +
        '<p>Which account still needs a change?</p>' +
        (mode === "missing-wrapper" ? "<div>" : '<details class="practice-answer"' + (mode === "open-answer" ? " open" : "") + ">") +
        (mode === "missing-label" ? "" : "<summary>" + label + "</summary>") +
        (mode === "missing-answer" ? "" : "<p>" + answer + "</p>") +
        "<ul><li>Check the exact account.</li><li>Keep required reading.</li></ul>" +
        (mode === "missing-wrapper" ? "</div>" : "</details>") + "</article>" +
        '<a aria-current="page" href="' + lessonURL + '">Current lesson</a>');
    } else if (request.url === baseurl + "/") {
      response.setHeader("Content-Type", "text/html");
      response.end('<ol class="course-lessons"><li><a href="' + lessonURL + '">Practice</a></li></ol>');
    } else if (request.url === baseurl + "/assets/site.css") {
      response.setHeader("Content-Type", "text/css");
      response.end("body { color: black; }");
    } else {
      response.writeHead(404);
      response.end("Not found");
    }
  });
  t.after(async () => {
    await new Promise(resolve => server.close(resolve));
    const relative = path.relative(testsDirectory, path.resolve(fixture));
    assert.ok(!relative.startsWith("..") && !path.isAbsolute(relative) && relative.startsWith(".site-verification-"));
    await rm(fixture, { recursive: true, force: true });
  });
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  for (const directory of ["author", "_data", "lessons", "assets"]) {
    await mkdir(path.join(fixture, directory));
  }
  await writeFile(path.join(fixture, "author/verify-site.mjs"), await readFile(new URL("../author/verify-site.mjs", import.meta.url)));
  await writeFile(path.join(fixture, "_config.yml"), JSON.stringify({
    url: "http://127.0.0.1:" + server.address().port, baseurl,
  }));
  await writeFile(path.join(fixture, "_data/course.yml"), JSON.stringify({
    lessons: [{ id: "CRT-TEST", title: "Practice a review", source: "lessons/practice.md", url: "/lessons/practice.html" }],
  }));
  await writeFile(path.join(fixture, "lessons/practice.md"), [
    "# Practice a review", "", "Which account still needs a change?", "",
    '<details class="practice-answer" markdown="block">', "<summary>" + label + "</summary>", "",
    answer, "", "- Check the exact account.", "- Keep required reading.", "", "</details>", "",
  ].join("\n"));

  async function verify() {
    return new Promise((resolve, reject) => {
      const child = spawn(process.execPath, [path.join(fixture, "author/verify-site.mjs"), "--live"], {
        cwd: fixture, windowsHide: true,
      });
      let stdout = "", stderr = "";
      child.stdout.on("data", chunk => { stdout += chunk; });
      child.stderr.on("data", chunk => { stderr += chunk; });
      const timer = setTimeout(() => { child.kill(); reject(new Error("Verifier fixture timed out")); }, 15000);
      child.on("error", error => { clearTimeout(timer); reject(error); });
      child.on("close", code => { clearTimeout(timer); resolve({ code, stdout, stderr }); });
    });
  }

  const complete = await verify();
  assert.equal(complete.code, 0, complete.stderr);
  assert.equal(JSON.parse(complete.stdout).contentUnits, 6);
  assert.equal(JSON.parse(complete.stdout).live, true);

  mode = "missing-wrapper";
  const missingWrapper = await verify();
  assert.notEqual(missingWrapper.code, 0);
  assert.ok(missingWrapper.stderr.includes("practice answers"), missingWrapper.stderr);

  mode = "open-answer";
  const openAnswer = await verify();
  assert.notEqual(openAnswer.code, 0);
  assert.ok(openAnswer.stderr.includes("practice answer starts open"), openAnswer.stderr);

  mode = "missing-answer";
  const missingAnswer = await verify();
  assert.notEqual(missingAnswer.code, 0);
  assert.ok(missingAnswer.stderr.includes("missing: " + answer), missingAnswer.stderr);

  mode = "missing-label";
  const missingLabel = await verify();
  assert.notEqual(missingLabel.code, 0);
  assert.ok(missingLabel.stderr.includes("missing: " + label), missingLabel.stderr);
});

