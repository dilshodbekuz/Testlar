import json
from pathlib import Path
from pypdf import PdfReader
R=Path.cwd();B=R.parent/'kitoblar';O=R/'audit/production_3sinf/local_sources';O.mkdir(exist_ok=True,parents=True)
inv=[]
for g in sorted(B.iterdir()):
 if not g.is_dir():continue
 for p in sorted(g.glob('*.pdf')):
  target=R/g.name/p.stem;fs=list(target.glob('[0-9]*.json')) if target.exists() else []
  row={'grade':g.name,'book':p.name,'path':str(p),'test_topics':len(fs),'test_folder':str(target)}
  if g.name=='3-sinf':
   d=PdfReader(p);pages=[pg.extract_text() or "" for pg in d.pages];row.update(pages=len(pages),text_chars=sum(map(len,pages)),empty_pages=sum(len(x.strip())<40 for x in pages))
   (O/(p.stem+'.json')).write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
   print(json.dumps(row,ensure_ascii=False))
  inv.append(row)
(O/'book_inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2),encoding='utf-8')
print('MISSING',json.dumps([{'grade':x['grade'],'book':x['book']} for x in inv if not x['test_topics']],ensure_ascii=False))

