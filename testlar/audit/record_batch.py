"""Record only questions actually read and reviewed in the conversation."""
from pathlib import Path
import json, hashlib, sys

root=Path(__file__).resolve().parent.parent
folder=root/'3-sinf/3-sinf 3-Sinf Matematika'
start,end=map(int,sys.argv[1:3])
notes=json.loads(Path(sys.argv[3]).read_text())
dest=root/'audit/manual_reviews.json'
reviews=json.loads(dest.read_text()) if dest.exists() else []
bykey={(r['file'],r['question_no']):r for r in reviews}
for p in sorted(folder.glob('[0-9]*.json')):
    no=int(p.name[:3])
    if not start<=no<=end:continue
    for i,q in enumerate(json.loads(p.read_text())['savollar'],1):
        status,note=notes.get(f'{no}:{i}',['tekshirildi',None])
        row={'file':str(p.relative_to(root)),'question_no':i,'sha256':hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'status':status,'notes':[note] if note else []}
        bykey[(row['file'],i)]=row
dest.write_text(json.dumps(list(bykey.values()),ensure_ascii=False,indent=2)+'\n')
print('Recorded review entries:',len(bykey))
