import json
from pathlib import Path
R=Path.cwd()
for p in sorted((R/'3-sinf/3-sinf 3-Sinf Ingliz tili').glob('00[1-3]_*.json')):
 print('\nFILE',p.name)
 for n,q in enumerate(json.loads(p.read_text(encoding='utf-8'))['savollar'],1):print(n,q['savol'],' || ',' | '.join(q['variantlar']),' KEY',q['togri'])
rows=json.loads((R/'audit/manual_reviews.json').read_text(encoding='utf-8'))
for r in rows:
 if r['file'].startswith('3-sinf/') and r['status']=='tahrir':
  p=R/r['file']
  if p.exists():
   import hashlib
   q=json.loads(p.read_text(encoding='utf-8'))['savollar'][r['question_no']-1]
   if hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==r['sha256']: print('UNFIXED',r,q)
