import assert from 'node:assert/strict';
import {readFile, readdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import test from 'node:test';
import {Liquid} from 'liquidjs';
import {parseHTML} from 'linkedom';
import {parse} from 'yaml';

const root = new URL('../', import.meta.url);
const read = p => readFile(new URL(p, root), 'utf8');
const config = parse(await read('_config.yml'));
const hands_on = JSON.parse(await read('_data/hands_on.json'));
const course = parse(await read('_data/course.yml'));
const engine = new Liquid({root:fileURLToPath(new URL('_includes/', root)),jekyllInclude:true});
engine.registerFilter('relative_url', value => config.baseurl + value);
const site = {...config, data:{course,hands_on}};
const label = lesson => `${lesson.route === 'specialist' ? 'Specialist' : 'Lesson'} ${hands_on.lessons.filter(l=>l.route===lesson.route).indexOf(lesson)+1}`;
const render = async (template, path) => parseHTML(await engine.parseAndRender(await read(template), {site,page:{path},content:'<p>Read the task</p>'})).document;

test('hands-on navigation opens the selected group and preserves every task exactly once', async () => {
  assert.equal(hands_on.lessons.length,24);
  assert.equal(new Set(hands_on.lessons.map(l=>l.id)).size,24);
  for (const lesson of hands_on.lessons) {
    const doc = await render('_layouts/default.html',lesson.source);
    assert.deepEqual([...doc.querySelectorAll('.lesson-nav a')].map(a=>a.getAttribute('href')),hands_on.lessons.map(l=>config.baseurl+l.url));
    assert.equal(doc.querySelectorAll('.nav-module[open]').length,1);
    assert.equal(doc.querySelector('.nav-module[open] summary').id,'nav-hands-on-'+lesson.group);
    assert.equal(doc.querySelector('a[aria-current="page"]').getAttribute('href'),config.baseurl+lesson.url);
    assert.deepEqual([...doc.querySelectorAll('.lesson-nav .lesson-id')].map(n=>n.textContent),hands_on.lessons.map(label));
    assert.equal(doc.querySelector('.course-sections a[aria-current="location"]').textContent,'Hands-On');
    assert.equal(lesson.url,'/'+lesson.source.replace(/\.md$/,'.html'));
    assert.ok((await read(lesson.source)).startsWith('# '));
  }
  const home = await render('_layouts/default.html','hands-on/index.html');
  assert.equal(home.querySelectorAll('.nav-module[open]').length,1);
  assert.equal(home.querySelectorAll('a[aria-current="page"]').length,0);
});

test('hands-on landing and adjacent links keep core and specialist tasks distinct', async () => {
  const home = await render('hands-on/index.html','hands-on/index.html');
  assert.deepEqual([...home.querySelectorAll('.course-lessons h3 a')].map(a=>a.getAttribute('href')),hands_on.lessons.map(l=>config.baseurl+l.url));
  assert.equal(home.querySelector('#specialist').hasAttribute('open'),false);
  assert.equal(home.querySelector('.start-link').getAttribute('href'),config.baseurl+hands_on.lessons[0].url);
  assert.ok(home.querySelector('a[download][href$="ISC_Certifications_Lab_Kit.zip"]'));
  assert.deepEqual([...home.querySelectorAll('.course-lessons .lesson-id')].map(n=>n.textContent),hands_on.lessons.map(label));
  assert.equal(label(hands_on.lessons.find(l=>l.id==='CLB-018')),'Lesson 6');
  assert.equal(label(hands_on.lessons.find(l=>l.id==='CLB-006')),'Lesson 7');
  assert.equal(label(hands_on.lessons.find(l=>l.id==='CLB-017')),'Lesson 18');
  assert.deepEqual(hands_on.lessons.filter(l=>l.route==='specialist').map(label),Array.from({length:6},(_,i)=>`Specialist ${i+1}`));
  for (const lesson of hands_on.lessons) {
    const route = hands_on.lessons.filter(l=>l.route===lesson.route), i=route.indexOf(lesson);
    const doc = await render('_layouts/hands-on-lesson.html',lesson.source);
    assert.deepEqual([...doc.querySelectorAll('.lesson-pagination a')].map(a=>a.getAttribute('href')),[route[i-1],route[i+1]].filter(Boolean).map(l=>config.baseurl+l.url));
    assert.equal(doc.querySelector('.lesson-placement').textContent,`Hands-on · ${label(lesson)}`);
    assert.deepEqual([...doc.querySelectorAll('.lesson-pagination a span')].map(n=>n.textContent),[i>0?`Previous · ${label(route[i-1])}`:null,i<route.length-1?`Next · ${label(route[i+1])}`:null].filter(Boolean));
  }
});

test('hands-on reader renders Markdown answers and excludes author and private pages', async () => {
  assert.ok(config.defaults.some(d=>d.scope.path==='hands-on/lessons'&&d.values.layout==='hands-on-lesson'));
  for(const path of ['hands-on/author','hands-on/private','hands-on/evidence','hands-on/COURSE_REGISTER.md','hands-on/README.md']) assert.ok(config.exclude.includes(path),path);
  const names=await readdir(new URL('hands-on/lessons/',root));
  assert.equal(names.length,24);
  for (const lesson of hands_on.lessons) {
    const text=await read(lesson.source);
    assert.ok(!/<details>/.test(text),lesson.id+' Markdown inside answers');
  }
  const template=await read('_layouts/hands-on-lesson.html');
  assert.ok(template.includes('term-help-data'));
  assert.ok(template.includes('table-scroll'));
  assert.ok(!(await read('hands-on/index.html')).match(/validation pending|not tested|working edition/i));
});
