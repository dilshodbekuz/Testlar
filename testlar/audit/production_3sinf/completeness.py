import json
from pathlib import Path
from collections import Counter
R=Path.cwd();rows=[]
for p in sorted((R/'3-sinf').glob('*/*[0-9]*.json')):
 if p.name.startswith('_'):continue
 d=json.loads(p.read_text(encoding='utf-8'));cs=Counter(q['qiyinlik'] for q in d['savollar'])
 if len(d['savollar'])!=30 or cs!={'oson':10,"o'rtacha":10,'qiyin':10}:rows.append({'file':p.relative_to(R).as_posix(),'count':len(d['savollar']),'levels':dict(cs)})
(Path('audit/production_3sinf/completeness.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Incomplete topics',len(rows),'Missing questions',sum(max(0,30-x['count']) for x in rows))
print(json.dumps(rows[:15],ensure_ascii=False,indent=2))
