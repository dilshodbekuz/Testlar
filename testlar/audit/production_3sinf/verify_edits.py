import json
from pathlib import Path
R=Path.cwd();p=R/'audit/production_3sinf/changes_applied.json';changes=json.loads(p.read_text(encoding='utf-8'))
# Inspect the final edited questions without repeating the unchanged options.
for x in changes:
 q=x['after']
 if 'Matematika/' in x['file'] or x['question_no'] in [1,5,12,17,21,25,26,28,29]:print(x['file'].split('/')[-1][:3],x['question_no'],q['savol'],' | '.join(q['variantlar']),' KEY',q['togri'])
