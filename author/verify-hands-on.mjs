import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {parse} from 'yaml';
import {parseHTML} from 'linkedom';

const root=new URL('../',import.meta.url);
const read=p=>readFile(new URL(p,root),'utf8');
const course=JSON.parse(await read('_data/hands_on.json'));
const config=parse(await read('_config.yml'));
const live=process.argv.includes('--live');
const base=config.url+config.baseurl;
const label=lesson=>`${lesson.route==='specialist'?'Specialist':'Lesson'} ${course.lessons.filter(l=>l.route===lesson.route).indexOf(lesson)+1}`;
const norm=s=>s.normalize('NFKC').replace(/[‘’]/g,"'").replace(/[“”]/g,'"').replace(/[–—]/g,'-').replace(/\s+/g,' ').trim();
const inline=s=>norm(s.replace(/<\/?(?:details|summary)\b[^>]*>/g,'').replace(/\*\*|\x60/g,'').replace(/\*([^*\n]+)\*/g,'$1'));
const cache=new Map();
async function page(path){if(!cache.has(path)){const response=await fetch(base+path);assert.equal(response.status,200,path);cache.set(path,await response.text());}return parseHTML(cache.get(path)).document;}
let units=0,tables=0,answers=0,blocks=0;
for(const lesson of course.lessons){
  const md=await read(lesson.source),prose=[],code=[];let fence=null,current=[];
  for(const line of md.split('\n')){
    const match=line.match(/^(\x60{3,}|~{3,})/);
    if(match){if(!fence){fence=match[1];current=[];}else if(match[1]===fence){code.push(current.join('\n').trimEnd());fence=null;}continue;}
    if(fence)current.push(line);else prose.push(line);
  }
  assert.equal(fence,null,lesson.id+' closed code fence');
  const expected=[];
  for(let line of prose){
    line=line.replace(/^(?:>[ \t]?)+/gm,'');
    if(/^\|[-|: ]+\|$/.test(line)){tables++;continue;}
    if(line.startsWith('|'))expected.push(...line.slice(1,-1).split('|').map(inline).filter(Boolean));
    else {const s=inline(line.replace(/^#{1,6} /,'').replace(/^\s*(?:[-+*]|\d+[.)])\s+/,''));if(s)expected.push(s);}
  }
  const answerLabels=[...md.matchAll(/<details[^>]*>\s*<summary>([\s\S]*?)<\/summary>/g)].map(m=>inline(m[1]));
  units+=expected.length;answers+=answerLabels.length;blocks+=code.length;
  if(live){
    const doc=await page(lesson.url),article=doc.querySelector('article.lesson-content');
    assert.ok(article,lesson.id+' article');
    const actual=norm(article.textContent);
    for(const s of expected)assert.ok(actual.includes(s),lesson.id+' missing '+s.slice(0,110));
    assert.deepEqual([...article.querySelectorAll('pre code')].map(n=>n.textContent.trimEnd()),code,lesson.id+' code');
    assert.equal(article.querySelectorAll('table').length,prose.filter(s=>/^\|[-|: ]+\|$/.test(s)).length,lesson.id+' tables');
    const disclosures=[...article.querySelectorAll('details')];assert.equal(disclosures.length,answerLabels.length,lesson.id+' answers');
    for(const [i,a]of disclosures.entries()){
      assert.equal(a.hasAttribute('open'),false);assert.equal(inline(a.querySelector('summary').textContent),answerLabels[i]);
      assert.ok(a.querySelector('p,ul,ol,table,pre'),lesson.id+' parsed answer content');
    }
    assert.equal(doc.querySelector('a[aria-current="page"]').getAttribute('href'),config.baseurl+lesson.url);
    assert.deepEqual([...doc.querySelectorAll('.lesson-nav .lesson-id')].map(n=>n.textContent),course.lessons.map(label),lesson.id+' sidebar numbering');
    assert.equal(doc.querySelector('.lesson-placement').textContent,'Hands-on · '+label(lesson),lesson.id+' placement numbering');
    const route=course.lessons.filter(l=>l.route===lesson.route),i=route.indexOf(lesson);
    assert.deepEqual([...doc.querySelectorAll('.lesson-pagination a')].map(a=>a.getAttribute('href')),[route[i-1],route[i+1]].filter(Boolean).map(l=>config.baseurl+l.url),lesson.id+' adjacent destinations');
    assert.deepEqual([...doc.querySelectorAll('.lesson-pagination a span')].map(n=>n.textContent),[i>0?'Previous · '+label(route[i-1]):null,i<route.length-1?'Next · '+label(route[i+1]):null].filter(Boolean),lesson.id+' adjacent numbering');
    assert.ok(!/tenant validation pending|working edition/i.test(doc.body.textContent));
    for(const a of doc.querySelectorAll('a[href]')){const href=a.getAttribute('href');if(href.startsWith(config.baseurl+'/')&&!href.includes('#')&&!href.endsWith('.zip'))await page(href.slice(config.baseurl.length));}
  }
}
if(live){
  const home=await page('/hands-on/');
  assert.equal(home.querySelectorAll('.course-lessons > li').length,course.lessons.length);
  assert.deepEqual([...home.querySelectorAll('.course-lessons .lesson-id')].map(n=>n.textContent),course.lessons.map(label),'landing numbering');
  for(const lesson of course.lessons)assert.ok(home.querySelector('a[href="'+config.baseurl+lesson.url+'"]'));
  const kit='/hands-on/downloads/ISC_Certifications_Lab_Kit.zip';
  const r=await fetch(base+kit);assert.equal(r.status,200,kit);
  const online=Buffer.from(await r.arrayBuffer()),local=await readFile(new URL(kit.slice(1),root));
  assert.equal(createHash('sha256').update(online).digest('hex'),createHash('sha256').update(local).digest('hex'),'lab kit content');
  for(const path of ['/hands-on/author/assessments/CLB-017_Assessor_Guide.html','/hands-on/COURSE_REGISTER.html','/hands-on/AGENTS.html','/hands-on/README.html','/hands-on/author/contracts/CLS-006_Config_Example.json'])assert.equal((await fetch(base+path)).status,404,'excluded '+path);
}
console.log(JSON.stringify({lessons:course.lessons.length,contentUnits:units,tables,answers,codeBlocks:blocks,servedPages:cache.size,live}));
