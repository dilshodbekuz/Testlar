import json
from pathlib import Path
R=Path.cwd();rows=json.loads((R/'audit/production_3sinf/old_review_changes.json').read_text(encoding='utf-8'))
for x in rows:
 if 'Matematika/' not in x['file']:continue
 q=x['q'];print(x['file'].split('/')[-1][:3],x['n'],x['old_status'],q['savol'],' | '.join(q['variantlar']), 'KEY',q['togri'])
