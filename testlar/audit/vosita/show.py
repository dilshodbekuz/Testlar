import sys,json,glob
from pathlib import Path
R=Path(__file__).resolve().parents[2]
# usage: show.py <book-dir-substring> <from> <to>   OR show.py <book> <topic>:<q>,<topic>:<q>
_c=[p for p in R.glob('*/*') if p.is_dir()]
book=([p for p in _c if p.name==sys.argv[1]] or [p for p in _c if sys.argv[1] in str(p)])[0]
fs=sorted(book.glob('[0-9]*.json'))
def tag(f):
    same=sorted(x for x in fs if x.name[:3]==f.name[:3])
    return f.name[:3]+('abcdefgh'[same.index(f)] if len(same)>1 else '')
def pr(f,idx):
    d=json.load(open(f));
    print(f"## {tag(f)} {d['mavzu'][:70]}")
    for i,s in enumerate(d['savollar'],1):
        if idx and i not in idx: continue
        v=' | '.join(f"{'*' if j==s['togri'] else ''}{x}" for j,x in enumerate(s['variantlar']))
        print(f"{i}. {s['savol']} || {v}")
if ':' in sys.argv[2]:
    want={}
    for x in sys.argv[2].split(','):
        t,q=x.split(':'); want.setdefault(t,set()).add(int(q))
    for t,qs in want.items():
        for f in fs:
            if tag(f).lstrip('0')==t.lstrip('0') or (t.isdigit() and f.name[:3]==f"{int(t):03d}"): pr(f,qs)
else:
    for f in fs:
        n=int(f.name[:3])
        if int(sys.argv[2])<=n<=int(sys.argv[3]): pr(f,None)
