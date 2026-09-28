import json,copy,shutil,hashlib
from pathlib import Path
R=Path.cwd();O=R/'audit/production_3sinf';B=R.parent/'kitoblar/3-sinf';events=json.loads((O/'changes_applied.json').read_text(encoding='utf-8'))
patches={('040',18):"Masalada Eyfel minorasining balandligi 320 m, Toshkent teleminorasining balandligi 375 m deb olingan. Shu qiymatlar bo'yicha Toshkent teleminorasi necha metr baland?",('040',29):"Masalada Eyfel minorasining balandligi 320 m, Toshkent teleminorasining balandligi 375 m deb olingan. Shu ikki balandlikning yig'indisi necha metr?",('042',6):"2019-yilgi 3-sinf Matematika darsligining 84-betiga ko'ra, Ulug'bek observatoriyasida tuzilgan xaritada nechta yulduz qayd etilgan?",('042',20):"Mirzo Ulug'bek 1394-yilda tug'ilgan. U 1437-yilda necha yoshga to'lgan?",('042',27):"Masalada yulduz xaritasi 1437-yilda tuzilgani, Ulug'bek esa 1449-yilda vafot etgani berilgan. Shu ikki yil orasida necha yil bor?",('057',2):"2019-yilgi 3-sinf Matematika darsligining 114-betidagi masalada 1 soatda 120 km yuradigan transport vositasi qaysi?"}
for (prefix,n),s in patches.items():
 p=next((R/'3-sinf/3-sinf 3-Sinf Matematika').glob(prefix+'_*.json'));d=json.loads(p.read_text(encoding='utf-8'));q=d['savollar'][n-1];bef=copy.deepcopy(q);q['savol']=s
 b=O/'backup'/p.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 events.append({'file':p.relative_to(R).as_posix(),'question_no':n,'before':bef,'after':copy.deepcopy(q),'reason':'Mahalliy Matematika (2019) darsligi bilan solishtirildi; yetishmagan shart va manba aniqlashtirildi'})
(O/'changes_applied.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
page_map={('001',10):[5],('040',7):[79],('040',10):[80],('040',18):[79],('040',29):[79],('041',2):[81],('041',3):[81],('041',4):[81],('042',5):[84],('042',6):[84],('042',8):[84],('042',9):[84],('042',20):[84],('042',27):[84],('043',3):[85],('043',6):[86,87],('043',25):[86,87],('046',10):[91],('056',5):[114],('057',2):[114],('057',3):[114],('079',7):[188]}
book=B/'3-sinf 3-Sinf Matematika.pdf';booksha=hashlib.sha256(book.read_bytes()).hexdigest();refs=[]
for (prefix,n),pages in page_map.items():
 p=next((R/'3-sinf/3-sinf 3-Sinf Matematika').glob(prefix+'_*.json'));q=json.loads(p.read_text(encoding='utf-8'))['savollar'][n-1]
 refs.append({'file':p.relative_to(R).as_posix(),'question_no':n,'sha256':hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'source_file':str(book),'source_sha256':booksha,'pdf_pages':pages,'status':'darslik_bilan_tekshirildi','note':'Kalit foydalanuvchi bergan 2019-yilgi darslikka mos. Tarixiy ma’lumotlar mustaqil tarixiy ekspertiza sifatida emas, shu darslik bayoni bo‘yicha tasdiqlandi.'})
eng=B/'3-sinf 3-Sinf Ingliz tili.pdf';eh=hashlib.sha256(eng.read_bytes()).hexdigest()
for prefix,page in [('001',4),('002',5),('003',6)]:
 p=next((R/'3-sinf/3-sinf 3-Sinf Ingliz tili').glob(prefix+'_*.json'))
 refs.append({'file':p.relative_to(R).as_posix(),'question_no':None,'source_file':str(eng),'source_sha256':eh,'pdf_pages':[page],'status':'mavzu_sahifasi_korildi','note':'Skan sahifa ko‘z bilan o‘qildi; tahrirlangan savollar mustaqil topshiriqlar sifatida mavzu lug‘ati va ko‘nikmalari bilan solishtirildi.'})
(O/'local_source_reviews.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
inv=json.loads((O/'local_sources/book_inventory.json').read_text(encoding='utf-8'));missing=[x for x in inv if not x['test_topics']]
lines=['# Mahalliy kitoblar: testi yaratilmaganlari','', 'Manba: Test_Generator/kitoblar. 2026-09-28. Mos test papkasida alohida mavzu JSON mavjudligi tekshirildi.','',f'Testi topilmagan kitoblar: {len(missing)} ta. Bu ro‘yxat butunlay yo‘q testlarga tegishli; qisman to‘ldirilmagan mavzular alohida completeness.json da.','']
for g in sorted({x['grade'] for x in missing},key=lambda x:int(x.split('-')[0])):
 lines += ['## '+g,'']+[ '- '+x['book'] for x in missing if x['grade']==g]+['']
(O/'TESTI_YOQ_KITOBLAR.md').write_text('\n'.join(lines),encoding='utf-8')
print('Local source checks',len(page_map),'total changed',len({(x['file'],x['question_no']) for x in events}),'missing books',len(missing))
