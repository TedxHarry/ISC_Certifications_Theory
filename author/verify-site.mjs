import assert from "node:assert/strict";
import { readFile, readdir } from "node:fs/promises";
import { parse } from "yaml";
import { parseHTML } from "linkedom";
const root = new URL("../", import.meta.url);
const read = p => readFile(new URL(p, root), "utf8");
const course = parse(await read("_data/course.yml"));
const config = parse(await read("_config.yml"));
const live = process.argv.includes("--live");
const base = config.url + config.baseurl;
const normalize = s => s.normalize("NFKC").replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/[–—]/g,"-").replace(/\s+/g," ").trim();
const inline = s => normalize(s.replace(/\*\*|\x60/g,""));
const assetNames = (await readdir(new URL("assets/",root))).filter(n=>n.endsWith(".txt"));
const assets = await Promise.all(assetNames.map(async n=>[n,(await read("assets/"+n)).trimEnd()]));
const fetched = new Map();
async function page(path) {
 if(!fetched.has(path)) {
  const response=await fetch(base+path);
  assert.equal(response.status,200,path);
  fetched.set(path,await response.text());
 }
 return fetched.get(path);
}
let units=0,diagrams=0,tables=0,localLinks=0;
assert.ok(course.lessons.length>0);
for(const lesson of course.lessons) {
 const md=await read(lesson.source);
 assert.ok(md.startsWith("# "+lesson.title));
 const blocks=[...md.matchAll(/^\x60{3}text\n([\s\S]*?)\n^\x60{3}/gm)].map(m=>m[1].trimEnd());
 for(const b of blocks) assert.ok(assets.some(([,text])=>text===b),lesson.id+" editable diagram");
 diagrams+=blocks.length;
 const prose=md.replace(/^\x60{3}[^\n]*\n[\s\S]*?^\x60{3}\s*$/gm,"");
 const expected=[];
 for(const paragraph of prose.split(/\n\s*\n/)) {
  if(!paragraph.trim())continue;
  for(let line of paragraph.split("\n")) {
   if(/^\|[-|: ]+\|$/.test(line)) {tables++;continue;}
   if(line.startsWith("|"))expected.push(...line.slice(1,-1).split("|").map(x=>inline(x)).filter(Boolean));
   else expected.push(inline(line.replace(/^#{1,6} /,"").replace(/^\s*(?:[-+*]|\d+[.)])\s+/,"")));
  }
 }
 units+=expected.length;
 if(live) {
  const html=await page(lesson.url);
  const doc=parseHTML(html).document;
  const article=doc.querySelector("article.lesson-content");
  assert.ok(article,lesson.id+" learner article");
  const text=normalize(article.textContent);
  for(const unit of expected)assert.ok(text.includes(unit),lesson.id+" missing: "+unit.slice(0,90));
  assert.deepEqual([...article.querySelectorAll("pre code")].map(n=>n.textContent.trimEnd()),blocks);
  assert.equal(article.querySelectorAll("table").length,(prose.match(/^\|[-|: ]+\|$/gm)||[]).length);
  assert.equal(doc.querySelector('a[aria-current="page"]')?.getAttribute("href"),config.baseurl+lesson.url);
  for(const anchor of doc.querySelectorAll("a[href]")) {
   const href=anchor.getAttribute("href");
   if(href.startsWith(config.baseurl+"/")&&!href.includes("#")) {
    await page(href.slice(config.baseurl.length));localLinks++;
   }
  }
 }
}
if(live) {
 const home=parseHTML(await page("/")).document;
 for(const lesson of course.lessons)assert.ok(home.querySelector('a[href="'+config.baseurl+lesson.url+'"]'));
 assert.equal(home.querySelectorAll(".course-lessons > li").length,course.lessons.length);
 for(const [name,text] of assets) {
  const response=await fetch(base+"/assets/"+name);
  assert.equal(response.status,200,name);
  assert.equal((await response.text()).trimEnd(),text,name);
 }
 const response=await fetch(base+"/assets/site.css");assert.equal(response.status,200);
 for(const path of ["/COURSE_REGISTER.html","/TEACHING_SPECIFICATION.html","/AGENTS.html","/author/revisions/CRT-001_Revision_Record.html"]) {
  const response=await fetch(base+path);assert.equal(response.status,404,"author content must not be published: "+path);
 }
}
console.log(JSON.stringify({lessons:course.lessons.length,contentUnits:units,diagrams,tables,assets:assets.length,localLinks,live}));
