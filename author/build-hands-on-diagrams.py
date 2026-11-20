"""Build the two authored hands-on flows as portable, script-free SVGs."""
import json
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

assets = Path(__file__).resolve().parents[1] / 'hands-on' / 'assets'

def build(stem, positions, width, height, description):
    spec = json.loads((assets / (stem + '.canonical.json')).read_text(encoding='utf-8'))
    diagram = spec['diagrams'][0]
    nodes = diagram['data']['nodes']
    assert set(positions) == {n['id'] for n in nodes}
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-labelledby="title description">',
             '<title id="title">' + escape(diagram['title']) + '</title>',
             '<desc id="description">' + escape(description) + '</desc>',
             '<rect width="100%" height="100%" fill="#ffffff"/>']
    for edge in diagram['data']['edges']:
        x,y,w,h = positions[edge['from']]
        tx,ty,tw,th = positions[edge['to']]
        start, end = (x+w/2,y+h), (tx+tw/2,ty-3)
        if stem.startswith('CLB-007') and edge['to'] == 'preview':
            end = (tx+tw*(0.4 if edge['from']=='collected' else 0.6),ty-3)
        mid = (start[1]+end[1])/2
        path = f'M{start[0]} {start[1]} V{mid} H{end[0]} V{end[1]}'
        parts.append(f'<path data-from="{edge["from"]}" data-to="{edge["to"]}" d="{path}" fill="none" stroke="#006c67" stroke-width="2"/>')
        parts.append(f'<polygon points="{end[0]-5},{end[1]-9} {end[0]+5},{end[1]-9} {end[0]},{end[1]}" fill="#006c67"/>')
    for node in nodes:
        x,y,w,h = positions[node['id']]
        lines = textwrap.wrap(node['label'], width=int((w-28)/9.5))
        assert len(lines)*24 <= h-16, node['id']
        parts.append(f'<g data-node="{node["id"]}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#eff4f8" stroke="#526574"/>')
        first = y+h/2-(len(lines)-1)*12+6
        parts.append(f'<text x="{x+w/2}" y="{first}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="18" fill="#123047">')
        for i,line in enumerate(lines):
            parts.append(f'<tspan x="{x+w/2}" dy="{0 if i==0 else 24}">{escape(line)}</tspan>')
        parts.append('</text></g>')
    parts.append('</svg>')
    (assets / (stem+'.svg')).write_text('\n'.join(parts)+'\n', encoding='utf-8')

build('CLB-003_flow', {key:(24,24+i*126,472,92) for i,key in enumerate(['data','preview','decision','task','file','check'])}, 520, 770,
      'Follow the rejected Export holding from collected data through reviewer sign-off, manual work, a simulated CSV change and verification.')
build('CLB-007_cycle_flow', {'file':(24,24,300,92),'template':(356,24,300,92),'collected':(24,158,300,92),'scheduled':(356,158,300,92),'preview':(132,308,416,92),'checked':(132,442,416,92)}, 680, 558,
      'Collect and check the changed CSV data separately from scheduling. Both paths feed a new preview, which the administrator checks and leaves unstarted.')
print('Built two hands-on SVG diagrams from their canonical nodes and edges.')
