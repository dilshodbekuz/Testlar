"""Build explicitly partial reports from recorded evidence, without changing tests."""
from pathlib import Path
from collections import Counter, defaultdict
import json, re

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'audit'
reviews=json.loads((OUT/'manual_reviews.json').read_text())
auto=[json.loads(line) for line in (OUT/'avtomatik_topilmalar.jsonl').read_text().splitlines()]
file_issues=json.loads((OUT/'fayl_muammolari.json').read_text())
stats=json.loads((OUT/'statistika.json').read_text())
labels={'xato':'Xato yoki bir ma’noli javob yo‘q','tahrir':'Tahrir / shartni aniqlashtirish','manba_kerak':'Manba yoki rasm kerak','tekshirildi':'Ko‘rildi, muammo qayd etilmadi'}
source_cache={}

def source(file):
    if file not in source_cache:
        p=ROOT/file
        raw=p.read_text()
        lines=[n for n,line in enumerate(raw.splitlines(),1) if re.match(r'^\s*"savol"\s*:',line)]
        source_cache[file]=(json.loads(raw),lines)
    return source_cache[file]

def link(file,question=None):
    p=ROOT/file
    line=''
    if question is not None:
        _,lines=source(file)
        if len(lines)>=question:line=f':{lines[question-1]}'
    label=file+(f' — {question}-savol' if question else '')
    return f'[{label}](<{p}{line}>)'

def links(text):
    return re.sub(r'https://[^\s;]+',lambda m:f'[Manba]({m.group(0)})',text)

def qblock(file,number):
    d,_=source(file);q=d['savollar'][number-1]
    text=['Savol: '+q['savol'].replace('\n',' / '),'']
    text += [f"- {'ABCD'[i]}) {v}"+(' **← kalit**' if i==q['togri'] else '') for i,v in enumerate(q['variantlar'])]
    return text+['']

findings=[r for r in reviews if r['status']!='tekshirildi']
lines=['# Mazmuniy tekshiruv: qayd etilgan topilmalar','',
       'Bu yakuniy hisobot emas. Quyidagi savollar o‘qib ko‘rilgan; tekshirilmagan savollar bu ro‘yxatga kiritilmagan. Manba kerak holati javobning to‘g‘riligi tasdiqlanmaganini bildiradi.', '']
for status in ['xato','manba_kerak','tahrir']:
    rows=sorted((r for r in findings if r['status']==status),key=lambda r:(r['file'],r['question_no']))
    lines += [f'## {labels[status]} — {len(rows)} ta','']
    for r in rows:
        lines += ['### '+link(r['file'],r['question_no']),'']
        lines += qblock(r['file'],r['question_no'])
        lines += ['Izoh: '+' '.join(links(n) for n in r['notes']),'']
(OUT/'MAZMUNIY_TOPILMALAR.md').write_text('\n'.join(lines)+'\n')

auto_labels={'arithmetic_wrong':'Sodda hisobdagi kalit nomuvofiqligi','arithmetic_multiple':'Bir nechta sonli javob to‘g‘ri','duplicate_options':'Aynan bir xil variantlar','equivalent_numeric_options':'Qiymati teng ifodalar — mazmuniy tekshiruv kerak','text_encoding':'G‘ayrioddiy belgilar — tekshirish kerak'}
lines=['# Avtomatik tekshiruv topilmalari','',
       'Avtomatik signal mazmuniy xato degani emas. Teng qiymatli kasrlar ayrim savollarda ataylab turli shaklda berilgan bo‘lishi mumkin. Chet tillaridagi ayrim diakritik belgilar ham to‘g‘ri bo‘lishi mumkin. Ular shubhali holat sifatida ajratildi.', '',
       'Variantlar takrorini aniqlashda katta-kichik harf va bo‘sh joylar saqlandi: AA/Aa/aa, R/r hamda dastur chiqishidagi bo‘sh joylar bir xil deb olinmadi. TXT sarlavhalari va ko‘p qatorli savollar nusxa farqi deb hisoblanmadi.','']
for code,title in auto_labels.items():
    fs=[f for f in auto if f['code']==code]
    lines += [f'## {title} — {len(fs)} ta signal','']
    for f in fs:
        lines += ['- '+link(f['file'],f['question_no'])+': '+f['detail']]
    lines += ['']
(OUT/'AVTOMATIK_TOPILMALAR.md').write_text('\n'.join(lines)+'\n')

lines=['# Fayl va jamlanma holatlari','',
       'Bir xil raqamli ikki mavzu yoki jamlanmaga kirmagan fayl avtomatik ravishda o‘chirilmasligi kerak: ular boshqa nashr yoki versiyaga tegishli bo‘lishi mumkin. Qaysi nashr asosiy ekanini darslik bilan aniqlash zarur.','']
for f in file_issues:
    lines += ['- '+link(f['file'])+': '+f['detail']]
(OUT/'FAYL_TOPILMALARI.md').write_text('\n'.join(lines)+'\n')

by_subject=defaultdict(lambda:Counter())
for line in (OUT/'savollar_holati.jsonl').open():
    r=json.loads(line);s=by_subject[(r['grade'],r['subject'])];s['jami']+=1
    s['korildi']+=r['semantic_status']!='tekshirilmagan'
    s['manba_kerak']+=r['semantic_status']=='manba_kerak'
    s['qolgan']+=r['semantic_status']=='tekshirilmagan'
lines=['# Fanlar bo‘yicha tekshiruv qamrovi','',
       'Ko‘rildi: savol matni, variantlari va kaliti mazmunan o‘qilgan. Manba kerak bo‘lgan savollar ham o‘qilganlar soniga kiradi, lekin javobi tasdiqlangan hisoblanmaydi. Avtomatik tekshiruv ushbu ustunga kiritilmagan.','',
       '| Sinf | Fan | Jami | Mazmunan ko‘rildi | Manba kerak | Mazmunan ko‘rilmagan |',
       '|---|---|---:|---:|---:|---:|']
for (grade,subject),s in sorted(by_subject.items()):
    lines += [f"| {grade} | {subject} | {s['jami']} | {s['korildi']} | {s['manba_kerak']} | {s['qolgan']} |"]
(OUT/'TEKSHIRUV_QAMROVI.md').write_text('\n'.join(lines)+'\n')

counts=Counter(r['status'] for r in reviews)
total=sum(s['questions'] for s in stats['grades'].values())
pending=total-len(reviews)
lines=['# Testlar tekshiruvi — ORALIQ HISOBOT','',
       '**Holat: to‘liq mazmuniy tekshiruv yakunlanmagan. Bu yakuniy hisobot emas.**','',
       f"Jami {total:,} ta savolning har biri avtomatik tuzilish tekshiruvidan o‘tdi. Shundan {len(reviews):,} ta savol matni, barcha variantlari va kaliti birma-bir o‘qib ko‘rildi. {pending:,} ta savolning mazmuniy tekshiruvi hali bajarilmagan.", '',
       '3-sinf matematika bo‘yicha 83 ta mavzu faylidagi 2 477 ta savol va Musiqa bo‘yicha 30 ta savol to‘liq o‘qildi. Odobnoma bo‘yicha 001–006 mavzulardagi 180 ta savol ham birma-bir o‘qildi. Boshqa fan/sinflarda avtomatik topilgan 21 ta savol alohida ko‘rildi. Manba talab qiladigan savollar javobi hali tasdiqlanmagan.','',
       'Asl JSON/TXT testlar o‘zgartirilmadi. Hisob alohida mavzu JSON fayllari bo‘yicha; _TOLIQ.json va TXT nusxalari qayta sanalmagan.','',
       '## Ko‘rilgan savollar natijasi','',
       '| Holat | Savollar soni |','|---|---:|']
for status in ['xato','tahrir','manba_kerak','tekshirildi']:
    lines += [f'| {labels[status]} | {counts[status]} |']
lines += ['', 'Muammo qayd etilmagani barcha tarixiy, biologik yoki o‘quv dasturiga oid faktlar tashqi manbalar bilan tasdiqlandi degani emas. Matematik savollarda hisob, mantiq, yetarli shart va variantlarning bir ma’noliligi ko‘rildi. Imlo bo‘yicha lug‘at bilan to‘liq solishtirish bajarilmadi.','',
          '## Muhim misollar','',
          '- 3-sinf, Matematika, 024-mavzu, 17 va 25-savollar: 10, 20, 10 sm tomonli uchburchak mavjud emas; 10+10=20.',
          '- 3-sinf, Matematika, 073-mavzu, 15-savol: chorshanbadan 32 kun oldin shanba bo‘ladi. Kalitdagi yakshanba xato.',
          '- 3-sinf, Matematika, 036-mavzu, 30-savol: “ulardan 5 marta kam” shartiga ko‘ra jami 84 ko‘chat; 77 kaliti boshqa shartga mos.',
          '- 3-sinf, Matematika, 034-mavzu, 20-savol: 29 minut 66 sekund va 30 minut 6 sekund teng; ikki javobni to‘g‘ri olish mumkin.',
          '- 5-sinf, Matematika (2-qism), 006-mavzu, 23-savol: 19/21−16/21+7/21=10/21. Kalit 11/21 noto‘g‘ri.',
          '- 6-sinf, Matematika, 006-mavzu, 30-savol: 2+(−5)×2=−8. Kalit −6 noto‘g‘ri.',
          '- Odobnoma, 002-mavzu, 13-savol: Humo qushiga xavfsizlik va tinchlik ma’nosi berilgan; to‘g‘ri javob baxt va erksevarlik. 005-mavzudagi 17 va 30-savollarda Arastuning so‘zlari uning o‘g‘liga noto‘g‘ri nisbat berilgan.',
          '- Musiqa: 30 ta savolning barchasi musiqa mavzusiga mos emas. Ayrimlarida kalit, ma’no va imlo xatolari ham bor.',
          '- Eyfel minorasi balandligi haqidagi 320 m qiymati davrsiz berilgan. Hozirgi antenna bilan balandlik 330 m; unga bog‘liq hisoblar yangilanishi kerak. [Eyfel minorasi rasmiy manbasi](https://www.toureiffel.paris/en/news/events/eiffel-tower-grows-330-meters-tall).','',
          '## Sinflar bo‘yicha qamrov','',
          '| Sinf | Mavzu fayllari | Savollar | Mazmunan ko‘rildi | Mazmunan ko‘rilmagan |','|---|---:|---:|---:|---:|']
for grade,s in stats['grades'].items():
    lines += [f"| {grade} | {s['files']} | {s['questions']} | {s['semantic_reviewed']} | {s['semantic_pending']} |"]
lines += ['', '## Avtomatik tekshiruv chegarasi','',
          '- Barcha mavzu JSON fayllari ochildi. Savol va variantlarning bo‘shligi, 4 ta variant mavjudligi, javob indeksining 0–3 oralig‘ida bo‘lishi tekshirildi. Ushbu tuzilish buzilishlari aniqlanmadi.',
          '- TXT nusxalar savol matni, variantlar va javob belgisi bo‘yicha JSON bilan solishtirildi. Mazmuniy nusxa farqi aniqlanmadi.',
          '- Aynan takroriy variantli 14 ta savol topildi. Oldingi dastlabki hisobot katta-kichik harflarni tenglashtirgani uchun biologiyadagi AA/Aa/aa kabi variantlarni noto‘g‘ri belgilagan; o‘sha hisoblar ushbu hisobot bilan almashtirildi.',
          '- 92 ta teng son qiymatli variant holati va 616 ta g‘ayrioddiy belgi signali bor. Bularning hammasi xato deb tasdiqlanmagan.',
          '- Oddiy arifmetik shablonga mos '+str(sum(s['arithmetic_calculated'] for s in stats['grades'].values()))+' ta savol avtomatik hisoblandi; 2 ta noto‘g‘ri kalit va 6 ta bir nechta to‘g‘ri sonli variant topilib, qo‘lda ham tekshirildi.',
          '- 17 ta fan papkasida alohida mavzu testlari yo‘q. 3-sinfning 4 fanida jamlanma va alohida fayllar tarkibi farq qiladi; 124 ta mavzu raqami bir nechta faylda ishlatilgan.','',
          '## Batafsil fayllar','',
          '- [Savol, variant, kalit va tuzatish izohlari](<'+str(OUT/'MAZMUNIY_TOPILMALAR.md')+'>)',
          '- [Fanlar bo‘yicha qamrov](<'+str(OUT/'TEKSHIRUV_QAMROVI.md')+'>)',
          '- [Avtomatik signallar](<'+str(OUT/'AVTOMATIK_TOPILMALAR.md')+'>)',
          '- [Fayl va jamlanma muammolari](<'+str(OUT/'FAYL_TOPILMALARI.md')+'>)',
          '- [Har bir savolning alohida holati — JSONL](<'+str(OUT/'savollar_holati.jsonl')+'>)','',
          '## Qolgan ish','',
          f'{pending:,} savolni ketma-ket mazmunan o‘qish, manba/rasm talab qiladigan savollarni asl darslik bilan tekshirish, qolgan 92 ta teng qiymat signali va matn buzilishlarini kontekstda saralash kerak. Shundan keyingina yakuniy umumiy xulosa berish mumkin.']
report='\n'.join(lines)+'\n'
(OUT/'ORALIQ_HISOBOT.md').write_text(report)
(ROOT/'TEKSHIRUV_HISOBOTI.md').write_text(report)
print(f'Report generated: reviewed={len(reviews)}, pending={pending}, findings={len(findings)}')
