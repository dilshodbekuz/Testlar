import importlib.util,json,copy
from pathlib import Path
p=Path.cwd()/'audit/production_3sinf/validate.py';s=importlib.util.spec_from_file_location('v',p);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
ledger=json.loads((p.parent/'review_ledger.json').read_text(encoding='utf-8'));r=next(x for x in ledger if x['status']=='joriy_tekshirildi');q=json.loads((Path.cwd()/r['file']).read_text(encoding='utf-8'))['savollar'][r['question_no']-1]
assert v.approved(q,r)
x=copy.deepcopy(q);x['togri']=(x['togri']+1)%4;assert not v.approved(x,r)
x=copy.deepcopy(q);x['savol']+=' changed';assert not v.approved(x,r)
x=copy.deepcopy(q);x['variantlar'][0]+=' changed';assert not v.approved(x,r)
for status in ['tekshirilmagan','manba_kerak','oldingi_tekshiruv_mos']:
 rr=dict(r,status=status);assert not v.approved(q,rr)
assert not v.approved(q,None)
print('Review gate tests passed: changed answers, questions, options and unapproved states rejected.')
