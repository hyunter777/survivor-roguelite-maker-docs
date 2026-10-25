"""Check published prose, source separation and built local links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import json, re, sys

ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN=re.compile(r'however|note that this does not guarantee|we do not claim|this is not intended to|not necessarily|may or may not|at this time|currently does not|be aware that|it is important to note|keep in mind|please note|disclaimer|limitations|we cannot guarantee|should work|in most cases|\b(?:may|might|should|cannot|unsupported|caveat)\b|not (?:guaranteed|supported|intended)',re.I)
LEAKS=re.compile(r'(?<![A-Za-z])[A-Za-z]:[\\/]',re.I)

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=set(); self.prose=[]; self.hidden=0
    def handle_starttag(self,tag,attrs):
        if tag in {'script','style'}:self.hidden+=1
        data=dict(attrs)
        if 'id' in data:self.ids.add(data['id'])
        if tag=='a' and 'name' in data:self.ids.add(data['name'])
        for key in ['href','src']:
            if key in data:self.links.append(data[key])
    def handle_endtag(self,tag):
        if tag in {'script','style'}:self.hidden=max(0,self.hidden-1)
    def handle_data(self,data):
        if not self.hidden:self.prose.append(data)

def main():
    errors=[]; forbidden=[]
    sources=list((ROOT/'docs/en').rglob('*.md'))+list((ROOT/'docfx').glob('*.md'))+list((ROOT/'api-metadata').glob('*.yml'))+list((ROOT/'docs/assets').glob('*.svg'))+[ROOT/'outline.md',ROOT/'README.md',ROOT/'screenshots-needed.md']
    for path in sources:
        text=path.read_text(encoding='utf-8-sig')
        if FORBIDDEN.search(text): forbidden.append(path.relative_to(ROOT).as_posix())
        if LEAKS.search(text):errors.append('Public source separation: '+path.relative_to(ROOT).as_posix())
    parsed={}
    for path in (ROOT/'site').rglob('*.html'):
        parser=Links();parser.feed(path.read_text(encoding='utf-8'));parsed[path.resolve()]=parser
        if FORBIDDEN.search(' '.join(parser.prose)):forbidden.append(path.relative_to(ROOT).as_posix())
    for path,parser in parsed.items():
        for link in parser.links:
            url=urlsplit(link)
            if url.scheme or url.netloc:continue
            address=unquote(url.path)
            if address.startswith('/survivor-roguelite-maker-docs/'):
                dest=ROOT/'site'/address[len('/survivor-roguelite-maker-docs/'):]
            elif address.startswith('/'):continue
            else:dest=path.parent/address if address else path
            if dest.is_dir():dest=dest/'index.html'
            dest=dest.resolve()
            if not dest.exists():errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {link}');continue
            if url.fragment and dest in parsed and unquote(url.fragment) not in parsed[dest].ids:
                errors.append(f'Broken anchor: {path.relative_to(ROOT)} -> {link}')
    report={'manual_pages':len(list((ROOT/'docs/en').rglob('*.md'))),'api_metadata_files':len(list((ROOT/'api-metadata').glob('*.yml'))),
        'html_pages_checked':len(parsed),'forbidden_phrase_hits':len(forbidden),'forbidden_files':forbidden,'errors':errors}
    out=ROOT/'.build/content-check.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2));return 1 if errors or forbidden else 0
if __name__=='__main__':sys.exit(main())
