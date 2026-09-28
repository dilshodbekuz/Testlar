import json
from pathlib import Path
P=Path('audit/production_3sinf/local_sources/3-sinf 3-Sinf Matematika.json');pages=json.loads(P.read_text(encoding='utf-8'))
print('PAGES',len(pages))
for i in [0,1,4,78,79,80,83,84,85,90,113,187]:
 print('\nPAGE',i+1,'\n',pages[i][:4400])
