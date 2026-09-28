import json
from pathlib import Path
rows=json.loads(Path('audit/production_3sinf/completeness.json').read_text(encoding='utf-8'))
for x in rows:
 if 'Matematika/' in x['file']:print(x['file'].split('/')[-1],x['levels'])
