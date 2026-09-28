import json
from pathlib import Path
p=next(Path('3-sinf/3-sinf 3-Sinf Ingliz tili').glob('004_*.json'));d=json.loads(p.read_text(encoding='utf-8'))
for n,q in enumerate(d['savollar'],1):print(n,q['savol'],' || ',' | '.join(q['variantlar']),' KEY',q['togri'])
