import json,re
from pathlib import Path
R=Path.cwd();folder=R/'3-sinf/3-sinf 3-Sinf Matematika'
for p in sorted(folder.glob('[0-9]*.json')):
 for n,q in enumerate(json.loads(p.read_text(encoding='utf-8'))['savollar'],1):
  if re.search(r'darslik|jadval|rasm|andaza|Ulug.bek|Beruniy|Xorazmiy|Eyfel|poyezd.*nom|sutkada.*havo',q['savol'],re.I):
   print(p.name[:3],n,q['savol'],' | '.join(q['variantlar']),' KEY',q['togri'])
