"""Validate only the isolated public directory; stdlib, no clinical data access."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.assets = []
        self.headings = []
    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if 'id' in a:
            if a['id'] in self.ids:
                errors.append(f"Duplicate id: {a['id']}")
            self.ids.add(a['id'])
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag in {'script', 'iframe'}:
            errors.append(f'Unexpected active/embed element: {tag}')
        if tag == 'img':
            if not a.get('alt'):
                errors.append('Image without descriptive alt text')
            self.assets.append(a.get('src', ''))
        if tag == 'source':
            self.assets.extend(v.strip().split(' ')[0] for v in a.get('srcset', '').split(','))
        if tag == 'link' and a.get('rel') == 'stylesheet':
            self.assets.append(a.get('href', ''))
        if tag == 'h1':
            self.headings.append(tag)

page = Page()
html = (DOCS/'index.html').read_text()
page.feed(html)
if len(page.headings) != 1:
    errors.append('Expected one primary heading')
for link in page.links + page.assets:
    u = urlsplit(link)
    if u.scheme in {'https', 'mailto'}:
        if link in page.assets:
            errors.append('External asset dependency')
        continue
    if u.scheme or u.netloc:
        errors.append('Unexpected URL scheme or host')
        continue
    if u.path:
        destination = (DOCS/unquote(u.path)).resolve()
        if not destination.is_relative_to(DOCS.resolve()) or not destination.is_file():
            errors.append(f'Missing or out-of-scope asset/link: {u.path}')
    elif u.fragment and u.fragment not in page.ids:
        errors.append(f'Missing anchor: {u.fragment}')
for n in range(1, 9):
    if f'ref-{n}' not in page.ids:
        errors.append(f'Missing reference {n}')

private_patterns = [r'PatientName', r'PatientID', r'AccessionNumber', r'PatientBirthDate',
                    r'/Volumes/', r'/Users/',
                    r'[A-Z]:\\', r'\b[A-Z]{2,5}[_\^]\d{3,}\b',
                    r'\b\d+(?:\.\d+){5,}\b']
files = []
for path in DOCS.rglob('*'):
    if path.name.startswith('._') or path.name == '.DS_Store':
        continue  # filesystem sidecars must not be staged/published
    if path.is_symlink():
        errors.append('Symlinks are not allowed in the public site')
        continue
    if not path.is_file():
        continue
    files.append(path)
    if path.suffix not in {'.html', '.css', '.svg'} and path.name != '.nojekyll':
        errors.append(f'Unreviewed file type in public site: {path.name}')
        continue
    text = path.read_text()
    for pattern in private_patterns:
        if re.search(pattern, text, flags=re.I):
            errors.append(f'Sensitive pattern detected in {path.name}; inspect locally')
    if path.suffix == '.svg':
        root = ET.fromstring(text)
        if root.find('{http://www.w3.org/2000/svg}title') is None:
            errors.append(f'SVG without accessible title: {path.name}')
        if re.search(r'<(?:script|image|foreignObject)\b|(?:href|src)\s*=', text, re.I):
            errors.append(f'Unexpected external or active SVG content: {path.name}')
    if path.suffix == '.css' and re.search(r'@import|url\s*\(', text, re.I):
        errors.append('Review unexpected CSS resource dependency')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(files)} public files; {len(page.ids)} unique anchors; '
      f'{len(page.assets)} local asset references; 8 selected references.')
print('No known private identifier/path patterns or unreviewed data formats found.')
print('This is a source-isolation check, not a clinical de-identification certificate.')
