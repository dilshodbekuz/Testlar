import json,shutil
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'audit/tuzatish_861';J=BASE/'SINXRONLASH_JURNALI.jsonl';B=BASE/'zaxira_txt_va_jamlanma'

def txt_from(data):
    lines=[data.get('mavzu','').strip(),'']
    order=[('oson','OSON'),("o'rtacha","O'RTACHA"),('qiyin','QIYIN')]
    for level,label in order:
        qs=[(i,q) for i,q in enumerate(data['savollar'],1) if q.get('qiyinlik')==level]
        if not qs:continue
        lines += [f'--- {label} ---','']
        for i,q in qs:
            lines.append(f"{i}. {q['savol']}")
            for j,opt in enumerate(q['variantlar']):
                lines.append(('+' if j==q['togri'] else '')+f"{'ABCD'[j]}) {opt}")
            lines.append('')
    return '\n'.join(lines).rstrip()+'\n'

events=[];txt_changed=0;agg_changed=0
for grade in sorted(ROOT.glob('[3-9]-sinf')):
    for folder in sorted(x for x in grade.iterdir() if x.is_dir()):
        jsons=sorted(p for p in folder.glob('*.json') if not p.name.startswith('_'))
        if not jsons:continue
        topics=[]
        for p in jsons:
            data=json.loads(p.read_text(encoding='utf-8'));topics.append(data)
            txt=p.with_suffix('.txt');new=txt_from(data);old=txt.read_text(encoding='utf-8') if txt.exists() else ''
            if old!=new:
                rel=txt.relative_to(ROOT);backup=B/rel;backup.parent.mkdir(parents=True,exist_ok=True)
                if txt.exists() and not backup.exists():shutil.copy2(txt,backup)
                txt.write_text(new,encoding='utf-8');txt_changed+=1
                events.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'txt_jsonga_moslandi','fayl':str(rel)})
        agg=folder/'_TOLIQ.json';new=json.dumps(topics,ensure_ascii=False,indent=2)+'\n';old=agg.read_text(encoding='utf-8') if agg.exists() else ''
        if old!=new:
            rel=agg.relative_to(ROOT);backup=B/rel;backup.parent.mkdir(parents=True,exist_ok=True)
            if agg.exists() and not backup.exists():shutil.copy2(agg,backup)
            agg.write_text(new,encoding='utf-8');agg_changed+=1
            events.append({'vaqt':datetime.now().isoformat(timespec='seconds'),'tur':'jamlanma_alohida_jsonlarga_moslandi','fayl':str(rel),'mavzu_soni':len(topics)})
with J.open('a',encoding='utf-8') as f:
    for x in events:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('txt_yangilandi',txt_changed,'jamlanma_yangilandi',agg_changed)
