import json,re,sys
from pathlib import Path
from fractions import Fraction
R=Path('/Users/dilshodbek/Desktop/Testlar/testlar')
def num(x):
    x=x.strip().replace('−','-').replace('–','-').replace(' ','')
    x=re.sub(r'(cm|sm|m|km|kg|g|l|ta|°)$','',x)
    if re.fullmatch(r'-?\d+,\d+',x): x=x.replace(',','.')
    try:
        if re.fullmatch(r'-?\d+/\d+',x): a,b=x.split('/'); return Fraction(int(a),int(b))
        if re.fullmatch(r'-?\d+(\.\d+)?',x): return Fraction(x)
    except: pass
    return None
def ev(expr):
    e=expr.replace('−','-').replace('–','-').replace('×','*').replace('·','*').replace('÷','/').replace(':','/').replace('x','*') 
    e=re.sub(r'\s+','',e)
    if not re.fullmatch(r'[\d+\-*/().]+',e) or not re.search(r'[+\-*/]',e[1:]): return None
    e=re.sub(r'(\d+)',r'Fraction(\1)',e)
    try: return eval(e)
    except: return None
out=[]
for f in sorted(R.glob('*/*/[0-9]*.json')):
    try: d=json.load(open(f))
    except Exception as ex: out.append(f'BUZUQ {f}');continue
    for i,s in enumerate(d['savollar'],1):
        v=s['variantlar'];k=s['togri']
        tag=f"{f.parts[-2][7:]}|{f.name[:3]}:{i}"
        norm=[x.strip().lower() for x in v]
        if len(set(norm))<4: out.append(f"DUP {tag} {s['savol'][:100]} || {v} *{k}")
        vals=[num(x) for x in v]
        eq=[(a,b) for a in range(4) for b in range(a+1,4) if vals[a] is not None and vals[a]==vals[b] and norm[a]!=norm[b]]
        if eq: out.append(f"EKV {tag} {s['savol'][:100]} || {v} *{k}")
        m=re.fullmatch(r'\s*([\d\s+\-−–*×·:÷/()]+?)\s*=\s*\??\s*(nimaga teng\??|qancha\??|nechaga teng\??|\?)?\s*',s['savol'].split('.')[-1] if False else s['savol'])
        if m:
            r=ev(m.group(1))
            if r is not None:
                ok=[j for j in range(4) if vals[j]==r]
                if ok!=[k]: out.append(f"HISOB {tag} {s['savol']} = {r} || {v} *{k}")
print('\n'.join(out)); print(len(out),file=sys.stderr)
