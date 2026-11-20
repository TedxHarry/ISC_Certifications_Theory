"""Rebuild and verify the downloadable learner kit from this repository."""
import hashlib
import json
import posixpath
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
source = root / 'hands-on'
target = source / 'downloads' / 'ISC_Certifications_Lab_Kit.zip'
paths = [p for folder in ['lessons', 'lab-data', 'tools', 'assets']
         for p in (source / folder).rglob('*')
         if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts]
paths += [source / p for p in ['author/contracts/CLS-005_Read_Only_Request_Plan.json',
          'author/contracts/CLS-006_Config_Example.json',
          'author/tests/test_collect_certification_evidence.py']]
contents = {p.relative_to(source).as_posix(): p.read_bytes() for p in paths}
contents['README.md'] = (source / 'LAB_KIT_README.md').read_bytes()
contents['.gitignore'] = b'private/\nevidence/raw/\n__pycache__/\n*.py[cod]\n*.log\n'
assert len([p for p in contents if p.startswith('lessons/')]) == 24
assert len([p for p in contents if p.endswith('.csv')]) == 14
assert not any('/assessments/' in p or '/revisions/' in p or p.startswith('private/') for p in contents)
target.parent.mkdir(parents=True, exist_ok=True)
assert target.resolve().parent == (source / 'downloads').resolve()
with ZipFile(target, 'w', ZIP_DEFLATED, compresslevel=9) as archive:
    for name, content in sorted(contents.items()):
        info = ZipInfo('ISC_Certifications_Hands_On/' + name, date_time=(2026, 11, 20, 0, 0, 0))
        info.compress_type = ZIP_DEFLATED
        archive.writestr(info, content, compresslevel=9)
with ZipFile(target) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(contents)
    for name, content in contents.items():
        assert archive.read('ISC_Certifications_Hands_On/' + name) == content
    relative_links = 0
    for name, content in contents.items():
        if not name.endswith('.md'):
            continue
        for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content.decode('utf-8')):
            if ':' in link or link.startswith('#'):
                continue
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(name), link.split('#')[0]))
            assert destination in contents, (name, link)
            relative_links += 1
print(json.dumps({'files': len(contents), 'bytes': target.stat().st_size,
                  'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
                  'relative_links': relative_links, 'assessor_answers': False}))
