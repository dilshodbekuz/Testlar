import json
from pathlib import Path
from collections import Counter
R=Path.cwd();O=R/'audit/publish_2026_09_28';stats=json.loads((O/'statistika.json').read_text(encoding='utf-8'))
findings=[]
def add(g,subject,pattern,n,reason,fix):
 p=next((R/f'{g}-sinf'/f'{g}-sinf {g}-Sinf {subject}').glob(pattern+'.json'))
 q=json.loads(p.read_text(encoding='utf-8'))['savollar'][n-1]
 lines=p.read_text(encoding='utf-8').splitlines();needle=json.dumps(q['savol'],ensure_ascii=False);ln=next((i for i,s in enumerate(lines,1) if needle in s),1)
 findings.append(dict(file=p.relative_to(R).as_posix(),question_no=n,line=ln,question=q,reason=reason,recommendation=fix))
add(4,'Matematika',"003_Ko'p xonali*",19,'Kalit xato: 50000 + 4000 + 3000 = 57000. B (56000) belgilangan.','Kalitni C (indeks 2) ga almashtirish.')
add(4,'Matematika','008_Uzunlik*',23,'A va B variantlari aynan bir xil: 26 m 74 cm. To‘g‘ri javob C (25 m 74 cm).','Takror noto‘g‘ri variantlardan birini boshqa qiymat bilan almashtirish.')
add(6,'Matematika','003_Sonning*',11,'C: 2 × 3 × 2 va D: 2² × 3 — ikkalasi ham 12 ning tub ko‘paytuvchilarga yoyilmasi. Savol darajali yozuvni talab qilmagan.','Savolda darajalar yordamida yozishni aniq talab qilish yoki C variantini almashtirish.')
add(6,'Matematika','003_Sonning*',14,'A: 3 × 3 × 5 va B: 3² × 5 — ikkalasi ham 45 ning tub ko‘paytuvchilarga yoyilmasi.','Savolda darajalar yordamida yozishni aniq talab qilish yoki A variantini almashtirish.')
add(3,'Ingliz tili','003_Unit*',2,'Savol matnga tayanadi, lekin JSON ichida manba matni yo‘q. Kasblar orasiga “Voqea” kiritilgan.','Asl matnni biriktirish, variantlarni mazmunan qayta tuzish.')
add(4,'Ingliz tili','010_Unit*',26,'“nechta kunni to‘liq yurakda ish qilish kerak” jumlasi tushunarsiz; beshta harakatdan beshta kun degan javob kelib chiqmaydi. Jadval ilova qilinmagan.','Jadvalni qo‘shish va savolni aniq qayta yozish.')
add(5,'Adabiyot','001_Adabiyot*',26,'Iqtibos va variantlar grammatik jihatdan buzilgan: “loy-kulgacha”, “plastilində”, “yasay ekan”, “Bolalar faqat o‘yn yasadi”.','Asl parcha bilan taqqoslab qayta tahrirlash.')
add(6,'Adabiyot (2-qism)','001_Said*',20,'Savol va chalg‘ituvchi variantlar tushunarsiz: “chap-chunkur”, “O‘tirib qo‘q”, “Yutib o‘yin”.','Asl hikoya asosida savol va barcha variantlarni qayta yozish.')
for n in [1,7,11,22]:add(4,'Musiqa','001_Vatanimiz*',n,'“shå’riy”/“Shå’riy” ko‘rinishidagi buzilgan yozuv mavjud.','“she’riy”/“She’riy” ko‘rinishiga tuzatish.')
(O/'tasdiqlangan_topilmalar.json').write_text(json.dumps(findings,ensure_ascii=False,indent=2),encoding='utf-8')
issues=json.loads((O/'fayl_muammolari.json').read_text(encoding='utf-8'))
contexts=Counter()
for line in (O/'savollar_holati.jsonl').open(encoding='utf-8'):
 x=json.loads(line)
 if x.get('source_context_may_be_needed'):contexts[x['grade']]+=1
s=['# Nashr oldidan qayta tekshiruv — 2026-09-28','', '**Xulosa: hozirgi holatda to‘liq tayyor test banki sifatida nashr qilish tavsiya etilmaydi.**','', '3–9-sinflarning barcha alohida mavzu JSON fayllari avtomatik tekshirildi. Shubhali signallar va har bir sinfdan tanlangan savollar mazmunan ko‘rildi. Barcha savollar birma-bir darslik bilan solishtirilgani yoki xatosizligi tasdiqlangani yo‘q. Test fayllari o‘zgartirilmadi; ushbu tekshiruv natijalari alohida saqlandi.','', '| Sinf | Mavzu fayli | Savol | Qayta hisoblangan arifmetik savol | Manbaga ishora signali* |','|---|---:|---:|---:|---:|']
for g,v in stats['grades'].items():s.append(f"| {g} | {v['files']} | {v['questions']} | {v['arithmetic_calculated']} | {contexts[g]} |")
s+=['',f"Jami: **{sum(v['files'] for v in stats['grades'].values())} mavzu, {sum(v['questions'] for v in stats['grades'].values())} savol**. Arifmetik shablon bilan {sum(v['arithmetic_calculated'] for v in stats['grades'].values())} savol qayta hisoblandi.",'','*Manbaga ishora — matn, rasm, she’r yoki jadval kabi so‘zlar bo‘yicha avtomatik signal; ularning barchasi xato yoki manbasiz degani emas.','', '## Tasdiqlangan muammolar','']
for i,x in enumerate(findings,1):
 p=R/x['file'];q=x['question'];s += [f"### {i}. {x['file']} — {x['question_no']}-savol",'',f"[Faylni ochish](<{p.as_posix()}:{x['line']}>)",'',q['savol'],'', ' | '.join(f"{'ABCD'[j]}) {v}" for j,v in enumerate(q['variantlar'])),'',f"Belgilangan javob: {'ABCD'[q['togri']]}",'',x['reason'],'', '**Tavsiya:** '+x['recommendation'],'']
s+=['## Jamlanma va qamrov muammolari','']
for x in issues:
 if x['code']!='duplicate_topic_number':s.append('- '+x['file']+': '+x['detail'])
s+=['','5 ta fan jamlanmasida jami 85 ta alohida mavzu mazmuni yo‘q. Jamlanmadan import qilinsa, ular nashrga tushmaydi. 204 ta fan/mavzu-raqami guruhida raqam takrorlangan; to‘plam versiyasi yoki noyob identifikator bilan farqlash lozim. Bu 204 ta noto‘g‘ri savol degani emas.','', '## Avtomatik tekshiruvning ijobiy natijalari','', '- JSON ochilish xatosi, bo‘sh savol, variantlar soni va javob indeksi xatosi topilmadi.','- Tekshirilgan alohida JSON va TXT nusxalari o‘zaro mos.','- Bir fan ichida aynan bir xil savol va variantlar to‘plami uchun turlicha javob kaliti topilmadi.','- 50 ta son qiymati tengligi signalining barchasi xato emas. Yuqoridagi 6-sinf 11- va 14-savollarida esa ikki to‘g‘ri javob borligi tasdiqlandi.','- 7-sinfdagi Å belgisi va 8-sinfdagi Adèle ismi o‘z-o‘zidan kodlash xatosi emas.','', '## Sinflar bo‘yicha qaror','', '- 3-sinf: matnsiz savollar, tahrir, yetishmayotgan Ona tili testlari va jamlanma muammolari hal qilinishi kerak.','- 4-sinf: noto‘g‘ri kalit, takror variant, buzilgan yozuv va jamlanmalar tuzatilishi kerak.','- 5-sinf: ko‘rilgan adabiyot savolida mazmunli tahrir zarur.','- 6-sinf: ikki to‘g‘ri javobli savollar va tushunarsiz adabiyot savoli qayta ishlanishi kerak.','- 7–9-sinflar: joriy avtomatik qoidalar aniq kalit xatosini ko‘rsatmadi; bu barcha javoblar mazmunan to‘g‘ri ekanini tasdiqlamaydi.','', '## Nashrga chiqarishdan oldin','', '1. Yuqoridagi tasdiqlangan muammolarni tuzatish va JSON/TXT/jamlanmani birga yangilash.','2. Parallel to‘plamlar qaysi darslik/nashrga tegishli ekanini belgilash, mavzu identifikatorlarini aniqlashtirish.','3. Matn/rasm/jadval talab qiluvchi testlarga tegishli manbani biriktirish.','4. Qolgan savollarni fanlar bo‘yicha mazmunan tekshirish; hozirgi avtomatik tekshiruvni to‘liq ekspertiza deb qabul qilmaslik.','', 'Avvalgi TEKSHIRUV_HISOBOTI.md dagi 3 338 mavzu / 99 123 savol va “0 xato” natijasi hozirgi fayllarga to‘liq mos kelmaydi. Yangi tekshiruv shu sabab alohida saqlandi.']
(O/'NASHR_XULOSASI.md').write_text('\n'.join(s)+'\n',encoding='utf-8')
print('Report:',O/'NASHR_XULOSASI.md');print('TOTAL',sum(v['questions'] for v in stats['grades'].values()),sum(v['files'] for v in stats['grades'].values()));print('confirmed',len(findings))
