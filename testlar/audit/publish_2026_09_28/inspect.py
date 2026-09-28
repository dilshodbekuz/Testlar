import json
from pathlib import Path
R=Path.cwd();O=R/'audit/publish_2026_09_28'
for line in (O/'avtomatik_topilmalar.jsonl').read_text(encoding='utf-8').splitlines():
 x=json.loads(line)
 if x['code']=='text_encoding':continue
 p=R/x['file'];q=json.loads(p.read_text(encoding='utf-8'))['savollar'][x['question_no']-1]
 print(json.dumps({'f':x['file'],'n':x['question_no'],'type':x['code'],'q':q},ensure_ascii=False))
for x in json.loads((O/'fayl_muammolari.json').read_text(encoding='utf-8')):
 if x['code']!='duplicate_topic_number':print(json.dumps(x,ensure_ascii=False))
