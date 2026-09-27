import sys,json,sys
from pathlib import Path
_ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(_ROOT))
import test_generator as tg
R=Path(__file__).resolve().parents[2]
# fixes file: lines "book|topic|q|togri(A-D or -)|savol or -|v1;;v2;;v3;;v4 or -"
book=None;changed={};log=open(R/'audit/tuzatishlar_qolda.jsonl','a')
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.rstrip('\n')
    if not line.strip(): continue
    b,t,q,k,sv,vs=line.split('|',5)
    _c=[p for p in R.glob('*/*') if p.is_dir()]
    bd=([p for p in _c if p.name==b] or [p for p in _c if b in str(p)])[0]
    num=int(''.join(c for c in t if c.isdigit())); suf=''.join(c for c in t if c.isalpha())
    cand=sorted(bd.glob(f'{num:03d}_*.json'))
    if len(cand)>1 and not suf: sys.exit(f'XATO: {b} {num} mavzu raqami ikki faylda bor - show.py dagi harfni ishlating (masalan {num}a / {num}b): '+line)
    f=cand['abcdefgh'.index(suf)] if suf else cand[0]
    d=changed.get(f) or json.load(open(f)); changed[f]=d
    s=d['savollar'][int(q)-1]; old=json.loads(json.dumps(s))
    if sv!='-': s['savol']=sv
    if vs!='-':
        v=vs.split(';;')
        if all(len(x)>1 and x[0] in 'ABCD' and x[1]=='=' for x in v):
            nv=list(s['variantlar'])
            for x in v: nv['ABCD'.index(x[0])]=x[2:]
            v=nv
        assert len(v)==4 and len(set(v))==4,line; s['variantlar']=v
    if k!='-': s['togri']='ABCD'.index(k)
    log.write(json.dumps({'fayl':str(f.relative_to(R)),'n':int(q),'eski':old,'yangi':s},ensure_ascii=False)+'\n')
dirs=set()
for f,d in changed.items():
    f.write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding='utf-8')
    tg.txt_yoz(f.with_suffix('.txt'),d['mavzu'],d['savollar']); dirs.add(f.parent)
for p in dirs:
    fs=sorted(p.glob('[0-9]*.json'))
    (p/'_TOLIQ.json').write_text(json.dumps([json.load(open(x)) for x in fs],ensure_ascii=False,indent=1),encoding='utf-8')
print('ok',len(changed),'fayl')
