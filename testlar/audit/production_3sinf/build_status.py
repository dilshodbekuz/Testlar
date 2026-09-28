"""Build a hash-bound review ledger. Unreviewed items never become approved automatically."""
import json,hashlib,csv,re,shutil
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parents[2];O=R/'audit/production_3sinf'
def sha(q):return hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
old={(x['file'].replace('\\','/'),x['question_no']):x for x in json.loads((R/'audit/manual_reviews.json').read_text(encoding='utf-8'))}
changes=json.loads((O/'changes_applied.json').read_text(encoding='utf-8'))
read_now={(x['file'],x['n']) for x in json.loads((O/'old_review_changes.json').read_text(encoding='utf-8')) if 'Matematika/' in x['file']}
read_now.update((x['file'],x['question_no']) for x in changes)
source_ids={('001',10),('040',7),('040',10),('040',18),('040',29),('041',2),('041',3),('041',4),('042',5),('042',6),('042',8),('042',9),('042',20),('042',27),('043',3),('043',6),('043',25),('046',10),('056',5),('057',2),('057',3),('079',7)}
source_path=O/'local_source_reviews.json'
source_refs={(x['file'],x['question_no']):x for x in json.loads(source_path.read_text(encoding='utf-8')) if x['question_no'] is not None} if source_path.exists() else {}
rows=[];subjects=[]
for folder in sorted((R/'3-sinf').iterdir()):
 if not folder.is_dir():continue
 fs=sorted(folder.glob('[0-9]*.json'));count=0;sc=Counter()
 for p in fs:
  d=json.loads(p.read_text(encoding='utf-8'));rel=p.relative_to(R).as_posix()
  for n,q in enumerate(d['savollar'],1):
   key=(rel,n);prev=old.get(key);h=sha(q);proof='';state='tekshirilmagan'
   if prev and prev['sha256']==h and prev['status']=='tekshirildi':state='oldingi_tekshiruv_mos';proof='audit/manual_reviews.json: exact sha256 match; not newly rechecked'
   if 'Ingliz tili/' in rel and p.name[:3] in ['001','002','003']:read_now.add(key)
   if 'Matematika/' in rel and re.search(r'darslik|jadval|rasm|andaza|Ulug.bek|Beruniy|Xorazmiy|Eyfel|poyezd.*nom|sutkada.*havo',q['savol'],re.I):read_now.add(key)
   if key in read_now:state='joriy_tekshirildi';proof='2026-09-28: question, all options, and answer read; revised where needed'
   if 'Matematika/' in rel and (p.name[:3],n) in source_ids:state='manba_kerak';proof='Exact textbook edition/page or factual source required; not approved'
   ref=source_refs.get(key)
   if ref and ref['sha256']==h:
    state='joriy_tekshirildi';proof='Mahalliy darslik: '+ref['source_file']+'; PDF betlari '+str(ref['pdf_pages'])+'; local_source_reviews.json'
   rows.append({'file':rel,'question_no':n,'sha256':h,'status':state,'evidence':proof})
   count+=1;sc[state]+=1
 m=json.loads((folder/'_mavzular.json').read_text(encoding='utf-8')) if (folder/'_mavzular.json').exists() else []
 subjects.append({'fan':folder.name,'mavzu_fayli':len(fs),'savol':count,'kitob_mundarijasi':len(m),'holatlar':dict(sc)})
(O/'review_ledger.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (O/'tekshiruv_navbati.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['file','question_no','sha256','status','evidence']);w.writeheader();w.writerows(x for x in rows if x['status']!='joriy_tekshirildi')
with (O/'manba_kerak.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['file','question_no','sha256','status','evidence']);w.writeheader();w.writerows(x for x in rows if x['status']=='manba_kerak')
summary={'grade':'3-sinf','date':'2026-09-28','production_ready':False,'total_questions':len(rows),'total_topic_files':sum(s['mavzu_fayli'] for s in subjects),'changed_questions':len({(x['file'],x['question_no']) for x in changes}),'review_statuses':dict(Counter(x['status'] for x in rows)),'subjects':subjects,'missing_tests':[s['fan'] for s in subjects if s['mavzu_fayli']==0],'absent_subject_folders':['3-sinf Musiqa: mahalliy PDF mavjud, test papkasi mavjud emas'],'blocking_reasons':['Barcha savollar joriy mazmuniy tekshiruvdan o‘tmagan','Barcha mavzular hali mahalliy darsliklar bilan solishtirilmagan','Ona tili va Musiqa testlari mavjud emas']}
(O/'NASHR_HOLATI.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# 3-sinf — tuzatishlar va nashr holati','', '**Holat: ish davom ettirilishi kerak. To‘liq production uchun tayyor emas.**','', 'Sana: 2026-09-28. 4–9-sinf fayllari bu bosqichda o‘zgartirilmadi.','',f"Jami {len(rows):,} savol, {summary['total_topic_files']} mavzu. {summary['changed_questions']} ta noyob savol tuzatildi. Asl nusxalar audit/production_3sinf/backup papkasida.",'', '## Bajarildi','', '- Ingliz tili 001–003 mavzularidagi 90 savolning hammasi matni, variantlari va kaliti bilan o‘qildi; 73 savol tahrirlandi. Kasb tarjimalari, aka-uka/opa-singil sanog‘i, bir nechta to‘g‘ri javob va matnsiz savollar tuzatildi.','- Matematikadagi avvalgi tahrirlangan savollar va qo‘shimcha shubhali savollar qayta ko‘rildi; 24 savolda shart va ifodalar aniqlandi; 22 ta manbaga bog‘liq savol mahalliy Matematika (2019) darsligi bilan solishtirildi.','- 3-sinfning barcha 570 mavzu fayli tuzilma nazoratidan o‘tdi; 578 sodda arifmetik savol qayta hisoblandi.','- JSON, TXT va _TOLIQ.json moslashtirildi. Tasviriy san’atdagi 9 va Texnologiyadagi 31 qo‘shimcha mavzu jamlanmalarga qo‘shildi.','- Har bir fan uchun fayl nomi va noyob identifikatori bor _testlar_index.json yaratildi. Darslikning asl _mavzular.json mundarijasi saqlandi.','', '## Tekshiruv darajasi','']
for k,v in summary['review_statuses'].items():lines.append(f'- {k}: {v}')
lines += ['', 'oldingi_tekshiruv_mos — avvalgi qayd bilan savolning mazmun izi mos; bu bugun qayta tekshirildi degani emas. Joriy tekshirildi holati ham darslik nashriga moslikni avtomatik tasdiqlamaydi.','', '## Fanlar inventari','', '| Fan | Mavzu fayli | Savol | Darslik mundarijasidagi band |','|---|---:|---:|---:|']
for s in subjects:lines.append(f"| {s['fan']} | {s['mavzu_fayli']} | {s['savol']} | {s['kitob_mundarijasi']} |")
lines+=['','## Testi yo‘q yoki yetishmayotgan kitoblar','', '- **3-sinf Ona tili:** alohida test yo‘q, _TOLIQ.json va _mavzular.json bo‘sh.','- **3-sinf Musiqa:** joriy to‘plamda fan papkasi yo‘q. Eski auditda 30 savol eslatilgan, lekin ularni hozirgi testlar orasida topib bo‘lmadi.','- Mahalliy kitoblar papkasi to‘liq inventarizatsiya qilindi. Barcha sinflar bo‘yicha testi yo‘q 42 kitob TESTI_YOQ_KITOBLAR.md da; 3-sinfda 11 kitobning 9 tasiga test bor.','', '## Nashrni to‘xtatib turgan masalalar','', '- Mahalliy darsliklar topildi. Bir xil fan ichida parallel mavzu to‘plamlari bor; 159 ta takror mavzu-raqami guruhi saqlangan. Yangi indeksda ular noyob ID bilan ajratilgan, lekin o‘quv dasturiga mos versiyasini tanlash kerak.','- Matematikadagi 22 ta manbaga bog‘liq savol endi mahalliy darslik betlari bilan tekshirildi. Bet raqamlari va fayl mazmun izlari local_source_reviews.json da saqlandi.','- Ingliz tilining 004–067 mavzulari va qolgan fanlarning mazmuniy tekshiruvi hali yakunlanmagan.','- Mahalliy PDFlar mavjud; Ingliz tili, Ona tili va Musiqa kitoblari asosan skan sahifalardan iborat. Ularni sahifa tasviri orqali tekshirish mumkin. Manba yo‘qligi sababli ishni to‘xtatish uchun asos yo‘q.','', '## Keyingi ish','', '1. Faqat Test_Generator/kitoblar ichidagi mahalliy darsliklardan foydalanish; internetdan qidirmaslik.','2. Ingliz tili 004-mavzudan davom etish; so‘ng boshqa fanlarni savolma-savol tekshirish.','3. Manbaga bog‘liq savollar va parallel to‘plamlarni darslik bilan solishtirish.','4. Yetishmayotgan kitoblar bo‘yicha test yaratish talabini manba asosida aniqlash.','5. Barcha savollar joriy tekshiruvdan o‘tgach, qayta nazorat va yakuniy eksport.','', '## Fayllar','', '- changes_applied.json — har bir tahrirning oldingi va keyingi ko‘rinishi.','- review_ledger.json — savol darajasidagi mazmun izi va tekshiruv holati.','- tekshiruv_navbati.csv — joriy tasdiq olmagan savollar.','- manba_kerak.csv — hali manba bilan tasdiqlanmagan qaydlar; dastlabki 22 matematika savoli mahalliy manba orqali yopildi.','- recheck/statistika.json — yangi avtomatik tekshiruv natijasi.','- NASHR_HOLATI.json — production_ready: false.','', '**Bu bosqichni “hamma test xatosiz” yoki “production tayyor” deb belgilash mumkin emas.**']
(O/'HISOBOT.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
# Replace the misleading grade summary with current, explicitly limited status.
p=R/'3-sinf/HISOBOT.md';b=O/'backup'/p.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True)
if not b.exists():shutil.copy2(p,b)
p.write_text('# 3-sinf — joriy holat\n\n2026-09-28: 97 savol tuzatildi; 570 mavzu / 16 963 savol avtomatik tekshirildi.\n\n**To‘liq production uchun hali tayyor emas.** Mahalliy darsliklar topildi; mazmuniy tekshiruv davom ettirilishi kerak.\n\n[Batafsil hisobot](../audit/production_3sinf/HISOBOT.md)\n',encoding='utf-8')
p=R/'TEKSHIRUV_HISOBOTI.md';oldtext=p.read_text(encoding='utf-8');banner='> **2026-09-28 yangilanish:** Quyidagi eski hisobot joriy holatni tasdiqlamaydi. 3-sinf bo‘yicha [yangi tuzatishlar va holat](audit/production_3sinf/HISOBOT.md) mavjud. To‘liq production holati: tayyor emas.\n\n'
if not oldtext.startswith('> **2026-09-28 yangilanish:**'):
 b=O/'backup'/p.relative_to(R)
 if not b.exists():shutil.copy2(p,b)
 p.write_text(banner+oldtext,encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='subjects'},ensure_ascii=False,indent=2))
