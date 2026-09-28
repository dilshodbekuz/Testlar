import json,shutil,copy
from pathlib import Path
R=Path.cwd();O=R/'audit/production_3sinf';events=json.loads((O/'changes_applied.json').read_text(encoding='utf-8'))
items=[('Matematika','014',23,"Kulol har bir laganga gul chizishga bir xil vaqt sarflaydi. U 2 ta laganga 50 daqiqada gul chizsa, 7 ta laganga necha daqiqada gul chizadi?"),('Matematika','030',23,"Sinfga avval 172 ta, keyin 143 ta darslik keltirildi. Barcha darsliklar o'quvchilarga teng taqsimlandi va har bir o'quvchi 9 tadan darslik oldi. Sinfda nechta o'quvchi bor?"),('Matematika','045',7,"Odatiy rim yozuvida I, X, C va M ketma-ket ko'pi bilan uch marta yoziladi va ustki chiziq ishlatilmaydi. Shu qoida bo'yicha eng katta son qaysi?"),('Matematika','045',29,"Ustki chiziqsiz odatiy rim yozuvida M ketma-ket ko'pi bilan uch marta yoziladi. Nega 4000 sonini MMMM shaklida yozish bu qoidaga zid?"),('Ingliz tili','002',5,"Ingliz tilida kishining kasbini umumiy ma'noda tanishtirganda, masalan, 'She is a teacher', kasb nomidan oldin qaysi artikl turi qo'llanadi?")]
for subject,prefix,n,s in items:
 p=next((R/'3-sinf'/f'3-sinf 3-Sinf {subject}').glob(prefix+'_*.json'));d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];before=copy.deepcopy(q);q['savol']=s
 b=O/'backup'/p.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 events.append({'file':p.relative_to(R).as_posix(),'question_no':n,'before':before,'after':copy.deepcopy(q),'reason':'Hisoblash shartini va qoida chegarasini aniqlashtirish'})
(O/'changes_applied.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('unique changed',len({(x['file'],x['question_no']) for x in events}))
