# 3-sinf testlari bo‘yicha to‘liq hisobot

Hisobot sanasi: 2026-09-27.

## Yakuniy xulosa

3-sinf testlari hali to‘liq tayyor emas. Mavjud 9 fandagi fayllar texnik jihatdan ochiladi va JSON/TXT nusxalari mos, lekin amaldagi savollarda tahrir hamda manba bilan tekshirish talab qiladigan muammolar qolgan. Musiqa va Ona tili papkalarida alohida mavzu testlari yo‘q. To‘rtta fanning `_TOLIQ.json` jamlanmasi alohida mavzu fayllarining hammasini qamramaydi.

Oldingi tekshiruv jurnallari barcha mavjud mavzular ko‘rib chiqilganini qayd etadi. Ushbu qayta audit esa o‘sha tuzatishlar amaldagi fayllarga qo‘llanganini tekshirdi va o‘zgarishsiz qolgan muammoli savollarni ajratdi. Shu sababli ‘ko‘rib chiqilgan’ holati ‘barcha xatolar bartaraf etilgan’ degani emas.

## Umumiy raqamlar

- Fan papkalari: 11 ta.
- Test mavjud fanlar: 9 ta.
- Alohida mavzu JSON fayllari: 530 ta.
- Alohida mavzu fayllaridagi savollar: 15,778 ta.
- Tuzatish jurnalidagi 3-sinf yozuvlari: 2,471 ta; alohida savollar: 2,435 ta.
- Haqiqiy o‘zgarish kiritilgan alohida savollar: 2,418 ta.
- Eng so‘nggi jurnal qiymati amaldagi faylga mos savollar: 2,435/2,435 ta.
- O‘zgarishsiz qolgan tasdiqlangan muammo: 186 ta.
- Jamlanmaga kirmagan alohida fayllar: 136 ta; ulardagi savollar: 4,035 ta.

## Fanlar bo‘yicha holat

| Fan | Mavzu fayli | Savol | Haqiqiy tuzatilgan savol | Qolgan tahrir | Manba kerak | Jamlanmada yo‘q savol | Holat |
|---|---:|---:|---:|---:|---:|---:|---|
| Ingliz tili | 67 | 1998 | 71 | 2 | 0 | 0 | Tuzatish kerak |
| Matematika | 83 | 2477 | 99 | 36 | 15 | 0 | Tuzatish kerak |
| Musiqa | 0 | 0 | 0 | 0 | 0 | 0 | Test yo‘q |
| Odobnoma | 24 | 716 | 255 | 122 | 0 | 0 | Tuzatish kerak |
| Ona tili | 0 | 0 | 0 | 0 | 0 | 0 | Test yo‘q |
| O‘qish | 164 | 4865 | 26 | 1 | 0 | 2574 | Tuzatish kerak |
| Rus tili | 24 | 717 | 119 | 2 | 0 | 0 | Tuzatish kerak |
| Tabiatshunoslik | 72 | 2148 | 727 | 1 | 0 | 926 | Tuzatish kerak |
| Tarbiya | 21 | 621 | 261 | 3 | 0 | 29 | Tuzatish kerak |
| Tasviriy san’at | 45 | 1340 | 514 | 2 | 0 | 506 | Tuzatish kerak |
| Texnologiya | 30 | 896 | 346 | 2 | 0 | 0 | Tuzatish kerak |

## Qolgan muammolar

Quyidagi jadvalda amaldagi savol izi oldingi muammo qaydidagi iz bilan aynan mos bo‘lgan savollar berilgan. Demak, ular qayddan keyin o‘zgartirilmagan. `Tahrir` — savol, variant yoki kalitni tuzatish kerakligini; `manba_kerak` — darslik, rasm yoki ishonchli manbasiz yakuniy hukm berib bo‘lmasligini bildiradi.

| № | Fan | Fayl | Savol | Holat | Muammo/tavsiya |
|---:|---|---|---:|---|---|
| 1 | Ingliz tili | 001_Unit 1 Lesson 1 I have two sisters.json | 3 | tahrir | «Opalar yoki singililar» → «Opalar yoki singillar»; C variantidagi «ukalari» ham parallel shaklda «ukalar» bo‘lishi kerak. |
| 2 | Ingliz tili | 001_Unit 1 Lesson 1 I have two sisters.json | 8 | tahrir | «Akalar yoki ukalari» → «Akalar yoki ukalar». |
| 3 | Matematika | 001_Ikki va uch xonali sonlarni xonadan o'tib qo'shish va ayiris.json | 9 | tahrir | Qo‘shish usullari faqat ikkita emas. Savolni 'Sonlarni xonalar bo‘yicha tagma-tag yozib qo‘shish usuli qanday ataladi?' deb aniqlashtirish kerak. |
| 4 | Matematika | 001_Ikki va uch xonali sonlarni xonadan o'tib qo'shish va ayiris.json | 10 | manba_kerak | Savol hisoblash ko‘nikmasini tekshirmaydi; mavzuga aloqasi darslik bilan aniqlashtirilishi kerak. Poyezd nomi tashqi manba bilan bu tekshiruvda tasdiqlanmadi. |
| 5 | Matematika | 013_Yig'indini songa bo'lish.json | 5 | manba_kerak | 'Namunada' deyiladi, lekin namuna keltirilmagan. 86 uchun 80+6 dan tashqari 70+16 va 60+26 ham to‘g‘ri yoyilmalar. Namunani qo‘shish yoki xona qo‘shiluvchilari shartini aytish kerak. |
| 6 | Matematika | 014_Ikki xonali sonni songa bo'lish.json | 2 | tahrir | Ko‘paytmani noldan farqli ko‘paytuvchiga bo‘lish mumkinligini ko‘rsatish kerak; nol ko‘paytuvchi bilan bu usul ishlamaydi. |
| 7 | Matematika | 015_Uch va undan ortiq ko'paytuvchilarni ko'paytirish.json | 1 | tahrir | Ko‘paytuvchilarni istalgan tartibda va guruhda hisoblash uchun o‘rin almashtirish bilan birga guruhlash xossasi ham tilga olinsin. |
| 8 | Matematika | 016_Qoldiqli bo'lish.json | 5 | tahrir | To‘g‘ri chiziqni undagi ikkita nuqtaning bosh harflari bilan ham belgilash mumkin (AB). Kichik harf bilan belgilash savolini aniqroq yozish kerak. |
| 9 | Matematika | 016_Qoldiqli bo'lish.json | 6 | tahrir | Alohida nuqtalarni ketma-ket qo‘yish to‘liq to‘g‘ri chiziq ta’rifi emas. Chiziqning ikki tomonga cheksiz davom etishi va to‘g‘riligi aniq ifodalansin. |
| 10 | Matematika | 030_2163 ko'rinishidagi ifodalar.json | 1 | tahrir | 'Nechta yuzlik va o‘nlik birga olinadi?' o‘rniga '2 yuzlik va 1 o‘nlik jami nechta o‘nlik?' yozilsin. Javob: 21 o‘nlik. |
| 11 | Matematika | 032_Sonning bo'luvchi va karralilarini aniqlash.json | 4 | tahrir | 3 ni 3,6,9,... ga ko‘paytirish ham 3 ga karrali sonlarni beradi. 'Barcha musbat karralilarni ketma-ket olish uchun' deb aniqlashtirish kerak. |
| 12 | Matematika | 032_Sonning bo'luvchi va karralilarini aniqlash.json | 21 | tahrir | Ko‘paytuvchilar natural sonlar ekani aniq yozilsin. Shunda 1×72,2×36,3×24,4×18,6×12,8×9 — 6 juft. |
| 13 | Matematika | 033_Ikki xonali songa ko'paytirish.json | 1 | manba_kerak | 15 uchun 15+0 va 12+3 ham to‘g‘ri yoyilmalar. Namuna ko‘rsatilmagan; 'xona qo‘shiluvchilari' sharti yozilsin. |
| 14 | Matematika | 035_Uchburchaklarning turlari.json | 1 | tahrir | Teng tomonli uchburchak kamida ikki teng tomonga ega, ya’ni keng ta’rifda teng yonli ham. Eng aniq nom so‘ralsin yoki tasnif ta’rifi ko‘rsatilsin. |
| 15 | Matematika | 040_To'rt xonali sonlarni taqqoslash.json | 10 | manba_kerak | Qadimgi Misrda abak qo‘llanganiga oid darslik va tarixiy manba kerak; bu tarixiy da’vo tasdiqlanmadi. |
| 16 | Matematika | 042_10000 ichida sonlarni ustun shaklida qo'shish.json | 5 | tahrir | Ustun qo‘shish usuli 100 ichida ham, 100000 ichida ham bir xil xona tamoyiliga asoslanadi. Oldingi o‘rganilgan bo‘lim aniq ko‘rsatilsin. |
| 17 | Matematika | 042_10000 ichida sonlarni ustun shaklida qo'shish.json | 6 | manba_kerak | 1018 ta xarita emas, katalogga kiritilgan yulduzlar soni nazarda tutilgan bo‘lishi mumkin. Kuzatilgan va katalogga kiritilgan yulduzlar sonini farqlab, darslik bilan tekshirish kerak. |
| 18 | Matematika | 042_10000 ichida sonlarni ustun shaklida qo'shish.json | 20 | tahrir | 1437−1394=43 — yillar ayirmasi. Aniq yosh sana bilan bog‘liq; shu yilda necha yoshga to‘lgan deb so‘rash aniqroq. |
| 19 | Matematika | 043_10000 ichida sonlarni ustun shaklida ayirish.json | 3 | tahrir | Xonalar bo‘yicha ayirish 100 va 100000 ichida ham o‘xshash. Savol aynan qaysi oldingi bo‘lim bilan qiyoslanayotganini aytsin. |
| 20 | Matematika | 043_10000 ichida sonlarni ustun shaklida ayirish.json | 6 | manba_kerak | Asar nomi ko‘rsatilmagan; 1030-yil va Amerika haqidagi bashorat birlamchi manba bilan tasdiqlanmadi. Sana uchun manba kerak. |
| 21 | Matematika | 043_10000 ichida sonlarni ustun shaklida ayirish.json | 25 | tahrir | 1030+462=1492 hisob to‘g‘ri. Amerika kashf etildi o‘rniga Kolumb Amerikaga yetib bordi deyilishi tarixan aniqroq; Beruniy asari haqidagi shart manba bilan tekshirilsin. |
| 22 | Matematika | 045_Rim raqamlari.json | 6 | tahrir | I,X,C,M ko‘pi bilan uch marta; V,L,D takrorlanmaydi. Qoidani barcha rim belgilariga bir xil qo‘llanadigandek bermaslik kerak. |
| 23 | Matematika | 045_Rim raqamlari.json | 10 | tahrir | MMMCMXCIX=3999 to‘g‘ri; eng katta son jumlasi faqat cheklangan yozuv qoidasi uchun aytilsin. |
| 24 | Matematika | 045_Rim raqamlari.json | 29 | tahrir | 4000 ni mutlaqo yozib bo‘lmaydi deyish to‘g‘ri emas; savol darslikda qo‘llangan ustki chiziqsiz qoidaga ko‘ra deb chegaralansin. |
| 25 | Matematika | 046_Og'zaki ko'paytirish va bo'lish.json | 10 | manba_kerak | 827-yil va Yer o‘lchamini aynan al-Xorazmiy hisoblagani haqidagi da’vo uchun darslik va tarixiy manba kerak. Qidiruvda ishtiroki ehtimoliy deb berilgan, sana tasdiqlanmadi. |
| 26 | Matematika | 049_10000 ichida yozma bo'lish.json | 1 | tahrir | Ma’lum ko‘paytuvchi noldan farqli ekanligi sharti aytilsin; nolga bo‘lish mumkin emas. |
| 27 | Matematika | 051_Ko'paytirishni tekshirish.json | 24 | manba_kerak | Hisob 2000×2+2000×5=14000 m to‘g‘ri. Barcha laylak, turna va lochinlar aynan shu balandlikda uchishi haqidagi umumiy da’vo tasdiqlanmadi; bu shartli masala ekani aytilsin. |
| 28 | Matematika | 052_Uzunlik o'lchov birliklari.json | 8 | tahrir | Bir xil birlikka keltirish qo‘shish, ayirish va taqqoslash uchun. Barcha amallar deb umumlashtirilmasin: turli kattaliklarni ko‘paytirish yoki bo‘lish ham mumkin. |
| 29 | Matematika | 056_Tenglamalar.json | 5 | manba_kerak | Bir odamning sutkalik havosi doim 22 kg deb olinmaydi; miqdor uchun darslik manbasi va taxminiy sharoit kerak. |
| 30 | Matematika | 056_Tenglamalar.json | 8 | tahrir | Qoldiqli degani musbat qoldiqli bo‘lish deb tushunilsa 0 ham mumkin emas. Natural sonni 3 ga bo‘lgandagi qoldiq deb so‘ralsin; 0≤r<3. |
| 31 | Matematika | 057_Masalalar yechish.json | 2 | manba_kerak | Transportlarning tezliklari keltirilmagan. Avtomobil ham, mototsikl ham 120 km/soat yurishi mumkin; jadvalga ko‘ra degan shart va jadval kerak. |
| 32 | Matematika | 057_Masalalar yechish.json | 3 | manba_kerak | Sutkalik havo massasi uchun 22 kg qiymatining manbasi va taxminiy sharoiti ko‘rsatilsin. |
| 33 | Matematika | 057_Masalalar yechish.json | 7 | tahrir | C dagi bo‘linuvchidan qoldiqni ayirib bo‘luvchiga bo‘lish ham bo‘linmani tekshirishga xizmat qiladi. Savolni bo‘linuvchini tiklab tekshirish deb aniqlashtirish kerak. |
| 34 | Matematika | 057_Masalalar yechish.json | 10 | manba_kerak | Ifodada urug‘ turi ko‘rsatilmagan. 3×150 g uchta 150 g paketning massasi; aynan sabzi ekanini bilish uchun masala matni kerak. |
| 35 | Matematika | 060_Simmetriya.json | 5 | tahrir | Simmetriya o‘qi kesma emas, to‘g‘ri chiziq. Diametr yotgan to‘g‘ri chiziq deb aniqlashtirilsin. |
| 36 | Matematika | 060_Simmetriya.json | 7 | tahrir | Nuqta o‘qda bo‘lsa uning tasviri o‘zi bilan ustma-ust tushadi. O‘qda yotmaydigan ikki simmetrik nuqta deb so‘ralsin. |
| 37 | Matematika | 060_Simmetriya.json | 10 | tahrir | Burchaklar emas, mos uchlar yoki burchak uchlari kesma bilan tutashtiriladi. |
| 38 | Matematika | 060_Simmetriya.json | 15 | tahrir | Kesmaning o‘zini tutuvchi chiziq ham simmetriya o‘qi. O‘rta perpendikular haqida so‘ralayotgani aniqlashtirilsin. |
| 39 | Matematika | 061_Kasr tushunchasi.json | 28 | tahrir | Bo‘yalmagan qism 3/12=1/4. Surat 3 bo‘lishi uchun maxraji 12 holida yozilgan kasr deb aniqlashtirish kerak. |
| 40 | Matematika | 064_To'g'ri va noto'g'ri kasrlar.json | 6 | tahrir | Aralash son butun qism va to‘g‘ri kasr qismdan iborat deb aniqlashtirilsin. |
| 41 | Matematika | 070_Yuzalarni taqqoslash.json | 1 | tahrir | Bir xil kattaliklarda o‘rniga bir xil o‘lchov birliklarida deb yozilsin. |
| 42 | Matematika | 073_Kalendar.json | 6 | tahrir | O‘tkir burchak 0° dan katta va 90° dan kichik deb aniqlashtirilsin. |
| 43 | Matematika | 073_Kalendar.json | 7 | tahrir | O‘tmas burchak 90° dan qat’iy katta, 180° dan qat’iy kichik. Gacha ifodasi chegarani kiritadigandek tushunilishi mumkin. |
| 44 | Matematika | 073_Kalendar.json | 22 | tahrir | Boshlanish va tugash kunlari ham sanalishi aniq yozilsin; 21+28+20=69. |
| 45 | Matematika | 073_Kalendar.json | 23 | tahrir | Boshlanish va tugash kunlari ham sanalishi aniq yozilsin; 21+29+20=70. |
| 46 | Matematika | 075_Sodda o'nli kasrlar.json | 4 | tahrir | O‘nli kasrga o‘tkazish qoidasida maxraj 10,100,... bo‘lishi va kerak bo‘lsa surat oldiga nollar qo‘yilishi aytilsin. Aks holda 5/100 ni 0,5 deb yozishga olib keladi. |
| 47 | Matematika | 077_O'nli kasrlarni taqqoslash va tartiblash.json | 3 | tahrir | Keyingi xona deganda o‘ngdagi xona nazarda tutilishi aniq yozilsin. |
| 48 | Matematika | 078_Takrorlash.json | 8 | tahrir | Bo‘lishni teskari bo‘lish bilan ham tekshirish mumkin (nol bo‘lmagan bo‘linmaga bo‘lib). Savolni bo‘linma va bo‘luvchi yordamida bo‘linuvchini tiklash uchun qaysi amal deb aniqlashtirish kerak. |
| 49 | Matematika | 079_Fazoviy figura – piramida.json | 1 | tahrir | Piramidaning uchi har qanday joylashuvda eng yuqorida bo‘lavermaydi. Asos tekisligidan tashqaridagi, yon qirralar tutashadigan uch deb tariflansin. |
| 50 | Matematika | 079_Fazoviy figura – piramida.json | 7 | manba_kerak | Teng tomonli uchburchakni o‘rta chiziqlar bo‘ylab buklash andazasi berilsa javob tushunarli. Hozir qaysi buklash chiziqlari ekani yo‘q; darslik rasmi kerak. |
| 51 | Matematika | 080_Konus va boshqa fazoviy figuralar.json | 2 | manba_kerak | Konus va aylantiriladigan uchburchak chizmasi berilmagan. To‘g‘ri burchakli uchburchak bir kateti atrofida aylantirilishi yozilsin; ikkinchi katet radiusga teng. |
| 52 | Matematika | 083_Yakuniy takrorlash.json | 4 | manba_kerak | Sonli piramidalarda turli qoidalar bo‘ladi. Rasm yoki ko‘paytma qoidasi berilmagan; ustidagi son doim pastdagilar ko‘paytmasi emas. |
| 53 | Matematika | 083_Yakuniy takrorlash.json | 24 | tahrir | Darsliklarning nimasi 3,4,5 bilan baholangani tushuntirilsin (masalan, saqlanish holati). Aks holda o‘quvchi yoki ish o‘rniga darslik yozilgandek ko‘rinadi. |
| 54 | Odobnoma | 001_O‘zbekiston Respublikasi — mustaqil davlat.json | 25 | tahrir | «Kechroq» kalendar sanami yoki kattaroq yoshmi — noaniq. «Ro‘yxatga ko‘ra, Javohir Sindorovdan kattaroq yoshda grossmeyster bo‘lgan» deb yozilsin. |
| 55 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 3 | tahrir | «Qanday qushi» → «qaysi qush»; Burut va Qazoq kabi ma’nosiz chalg‘ituvchilarni almashtirish. |
| 56 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 4 | tahrir | «nekning», «tinchliq» → «nimaning», «tinchlik»; variantlarni mazmunli qayta tuzish. |
| 57 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 5 | tahrir | 65 metr bayroq matosining o‘lchami emas. Matndagi Xalqlar do‘stligi maydonidagi bayroq ustuni nazarda tutilgani aniq yozilsin. |
| 58 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 6 | tahrir | «Madhiyani yangraganda» → «Madhiya yangraganda». |
| 59 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 8 | tahrir | Uch chalg‘ituvchi savoldagi harakatga javob bermaydi: kasb/odam/soha nomlari berilgan. Bir xil grammatik shakldagi harakatlar qo‘yilsin. |
| 60 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 9 | tahrir | Kalitdagi «hurmati ifodalaymiz» grammatik xato. «Yurtga muhabbat va hurmatni ifodalash» deb yozilsin. |
| 61 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 10 | tahrir | «Qaysi bayrami» → «qaysi bayram»; «Tilga shukorlik» kabi buzilgan variantlar tahrirlansin. |
| 62 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 11 | tahrir | «Nima bildiradi» → «nimani bildiradi»; «Saogat» ma’nosiz variant. |
| 63 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 12 | tahrir | «Tushrili narsalar» buzilgan. Savol «nimani anglatadi?» shaklida tuzilsin. |
| 64 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 14 | tahrir | «Ramzlaringa» → «ramzlariga». |
| 65 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 17 | tahrir | «G‘aliblar», «Bayroq yuqori», «Raqasa chamadilar» tahrirlansin; marosimdagi harakat aniq tasvirlansin. |
| 66 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 18 | tahrir | «Bayroq yo‘q kerak», «Bayroq oynasi» kabi chalg‘ituvchilar ma’nosiz. |
| 67 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 20 | tahrir | «Nima qilishga qarang dedi» buzilgan. «Jaloliddin katta bo‘lgach nima qilishini aytdi?» deb yozilsin. |
| 68 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 21 | tahrir | Savol va kalit grammatik jihatdan buzilgan: «ramzlaringa», «birlashushi»; mazmunli sabab sifatida qayta yozilsin. |
| 69 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 22 | tahrir | To‘g‘ri javobdagi «tayiniy belgisi», chalg‘ituvchilardagi «sadolik», «Musaviy» so‘zlari buzilgan; milliy birlik va davlat mustaqilligi mazmunida qayta tuzilsin. |
| 70 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 23 | tahrir | «Bayroq ko‘taram deya qarang dedi» ifodasi tushunarsiz; «bayroqni yuksaklarga ko‘tarishni orzu qildi» shaklida yozilsin. |
| 71 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 25 | tahrir | Savol mantiqan buzilgan; kalitdagi «tarixini va azamini ta’minlaydi» javob bermaydi. «buydoq», «madhiya qora» kabi variantlar bilan birga to‘liq qayta tuzilsin. |
| 72 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 27 | tahrir | «Bildirapmiz», «sevgi va hurmati», «Surpa ko‘rsatish» tahrirlansin. |
| 73 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 28 | tahrir | «Ta’tiflarda» va inkor-so‘roq shakli tushunarsiz; «Davlat ramzlarini qachon hurmat qilish kerak?» deb aniq yozilsin. |
| 74 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 29 | tahrir | «Tarixiy sabab va milliy qadriyatlar» juda umumiy; qolgan variantlar ham buzilgan. Muayyan mazmunli sabab va mos chalg‘ituvchilar kerak. |
| 75 | Odobnoma | 002_Davlat ramzlari — milliy iftixorimiz.json | 30 | tahrir | «Rasmi hamasi», «Shuvi rang» ma’nosiz; kalit va variantlar bir xil grammatik shaklda qayta yozilsin. |
| 76 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 1 | tahrir | «Tashkent» → «Toshkent». |
| 77 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 2 | tahrir | «Tashkent» → «Toshkent». |
| 78 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 4 | tahrir | Xivaning 2500 yilligi 1997-yilda nishonlangan. Savol vaqtga bog‘liq «tarixi qancha yil» emas, yubiley haqida aniq so‘rasin. |
| 79 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 5 | tahrir | «Gumbaji qancha metrdan ortiq» o‘lchanayotgan kattalikni aytmaydi. Darslikda gumbaz oralig‘i nazarda tutilgan. «Ravog‘ining oralig‘i» deb aniqlashtirilsin. |
| 80 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 9 | tahrir | «Maydonda nechta madrasalar» → «maydonida nechta madrasa». |
| 81 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 10 | tahrir | «Qanday haqida» → «nima haqida». |
| 82 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 11 | tahrir | «Uchta muhtasham madrasalar» → «uchta muhtasham madrasa». |
| 83 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 12 | tahrir | «Bajarad» → «bajaradi»; «rolni bajaradi» o‘rniga «vazifani bajaradi». |
| 84 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 13 | tahrir | «Minorasi» → «minorasini»; «gumbaji» → «gumbazi». |
| 85 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 14 | tahrir | «Kuchli va ijodi qobiliyatini» buzilgan; qudrati va bunyodkorlik mahorati deb ifodalansin. |
| 86 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 17 | tahrir | «Qutlanish» → «nishonlanish»; variantlar bir xil grammatik shaklda yozilsin. |
| 87 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 18 | tahrir | «Tashkent» → «Toshkent». |
| 88 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 20 | tahrir | «Eng muhtasham» subyektiv, qaysi manba yoki obida nazarda tutilganini belgilash kerak; «Tashkent» → «Toshkent». |
| 89 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 22 | tahrir | Kalitdagi «gumbaji 22 metrdan ortiq» o‘lchov turi yo‘q. Farq minora va saroy ekani bilan ifodalansin yoki ravoq oralig‘i aniqlashtirilsin. |
| 90 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 23 | tahrir | «Eng quyi taas» ma’nosiz variant; savol grammatikasi tahrirlansin. |
| 91 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 24 | tahrir | «Imkoniat» → «imkoniyat»; «Faqat yangi bino qilish» grammatik jihatdan tahrirlansin. |
| 92 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 26 | tahrir | «Qiymatini», «kuchli ijodi va inshoot qobiliyati» noto‘g‘ri birikmalar; qudrat va bunyodkorlik mahorati deb yozilsin. |
| 93 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 28 | tahrir | Savoldagi «qo‘li» va kalitdagi «mas’ul tuguni o‘zyni sanjaydi» buzilgan; kalitni «Davlat yodgorliklarni saqlash va himoya qilish uchun mas’ul» deb qayta tuzish. |
| 94 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 29 | tahrir | «Faqat yangi turlar» ma’nosiz chalg‘ituvchi; kalitdagi takroriy qaratqichlarni qisqartirish. |
| 95 | Odobnoma | 003_Tarixiy obidalar — madaniy boyligimiz.json | 30 | tahrir | Savol sun’iy va tushunarsiz, minorani ko‘rmay ketish amalda mumkin; «Matnda bu ibora nimani ta’kidlaydi?» shakliga keltirish. |
| 96 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 1 | tahrir | kimsi → kimi |
| 97 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 2 | tahrir | qanday nomi bilan → qanday nom bilan; Ayyoqa kabi buzilgan variantlar |
| 98 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 3 | tahrir | Eronga → Erondan |
| 99 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 4 | tahrir | Saroj → saroy; hikoyaga ko‘ra deb belgilash |
| 100 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 5 | tahrir | necha talabalar → nechta talaba; Beshyuzga → besh yuzga |
| 101 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 6 | tahrir | yo‘nib ishlay turgan → yo‘nib yuborgan |
| 102 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 7 | tahrir | Devalar → tuyalar; savolda hayvon turi so‘ralsin |
| 103 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 8 | tahrir | Saroj → saroy; hikoyaga ko‘ra deb belgilash |
| 104 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 9 | tahrir | Kokga → ko‘kka; Shugunga ma’nosiz variant |
| 105 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 10 | tahrir | Xind → Hind; Shahistar ma’nosiz variant |
| 106 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 11 | tahrir | Aql-u zakovat tengsiz → aql-u zakovati tengsiz |
| 107 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 12 | tahrir | Variantlar grammatik jihatdan parallel emas; Armiya boshlamoq buzilgan |
| 108 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 13 | tahrir | Taror ishlari ma’nosiz variant |
| 109 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 16 | tahrir | Ishchilarni javobgarchi qildi ma’nosiz variant |
| 110 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 17 | tahrir | Keng maydonida → keng maydonda; Tog‘lilar va Saroj variantlari buzilgan |
| 111 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 18 | tahrir | Ziyonda olib keladi → zarar keltiradi |
| 112 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 19 | tahrir | O‘zbekistoniga → O‘zbekistonga; O‘rta turmush uchun ma’nosiz; turli tashrif sabablari mumkinligi uchun matnga ko‘ra deyilishi kerak |
| 113 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 20 | tahrir | Masjidni va madrasasi grammatik jihatdan mos emas; o‘tgan zamon bir xilda yozilsin |
| 114 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 21 | tahrir | Savol juda uzun; boshqarab va charchaqqan buzilgan; aniq bitta sababni so‘rash |
| 115 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 23 | tahrir | Tarixiy mohorati va qaytishiga joy berish ma’nosiz; sovg‘a niyati haqida aniq savol kerak |
| 116 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 24 | tahrir | mamlakatingiz barkatini → mamlakat daromadini; grammatik tuzilmani soddalashtirish |
| 117 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 25 | tahrir | tez-tez kuzata bergani matndan asoslanmagan; aql-zakovat va bunyodkorlikni qadrlash mazmunida qayta yozish |
| 118 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 26 | tahrir | Tarixiy to‘plam, o‘yg‘otadi buzilgan; sodda sabab-oqibat savoliga keltirish |
| 119 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 27 | tahrir | Uchta-beshta talabalar tilgan edi buzilgan; ta’limdagi ahamiyatini so‘rash, davlat rahbarlarini yetishtirishni isbotsiz majburiy natija qilmaslik |
| 120 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 28 | tahrir | Kalit savolga to‘g‘ridan-to‘g‘ri javob bermaydi: hayvonlar og‘ir yuk tashishga xizmat qilganini ifodalash |
| 121 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 29 | tahrir | Ishchilarni shartli qildi buzilgan; kalitni ish tezlashdi deb soddalashtirish |
| 122 | Odobnoma | 004_Amaliy mashg‘ulot. Men yashayotgan hududdagi tarixiy obidala.json | 30 | tahrir | kokga, maydonida, iradasi → ko‘kka, maydonda, irodasi; savol/kalitni yoshga mos qisqartirish |
| 123 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 1 | tahrir | Barcha variantdagi chorchlash → chorlash |
| 124 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 2 | tahrir | shujoatlik → shijoat; Avestoning barcha mavzulari emas, darslikdagi jihati so‘ralsin |
| 125 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 3 | tahrir | Qodimiy Romaning kitob ma’nosiz variant |
| 126 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 4 | tahrir | qaysi fanlarini → qaysi fanlarni |
| 127 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 5 | tahrir | Rivoyatga ko‘ra deb qo‘shish; hozirgi zamon o‘rniga o‘tgan zamon |
| 128 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 6 | tahrir | qaysi ilmga shug‘ullanadi → qaysi ilm bilan shug‘ullangan |
| 129 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 8 | tahrir | sozi nima anglatadi → so‘zi nimani anglatadi |
| 130 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 9 | tahrir | kimdir → kim; Ilm fan rivojlantirgan → ilm-fanni rivojlantirgan |
| 131 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 10 | tahrir | Qaysi musobaqa ekani aytilmagan. Maktab o‘quvchilari o‘rtasidagi xalqaro matematika musobaqasi va umumjamoa hisobi aniqlashtirilsin |
| 132 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 11 | tahrir | Hikoyada fanni yoqtirmagani, o‘rganmaganligi emas. «Dastlab matematikani nega yoqtirmagan?» deb yozish |
| 133 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 12 | tahrir | Tug‘ma shahri, yuzini yuvib-taranib buzilgan; rivoyat konteksti yozilsin |
| 134 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 14 | tahrir | yili davomida → yil davomida; rivoyatga ko‘ra |
| 135 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 15 | tahrir | ask arini/ boylarni bor kabi grammatik nuqsonlar; matnga ko‘ra ta’limning ahamiyati so‘ralsin |
| 136 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 16 | tahrir | nima dars → qanday saboq; kalit oxiridagi haqida ortiqcha |
| 137 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 18 | tahrir | Rasadxona ilmiy kuzatuv inshooti. «Darslikda rasadxonaga qanday baho berilgan?» deb so‘ralsa kalit mos keladi |
| 138 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 20 | tahrir | natijasidan → natijasida; bog‘langan insonlar va qorov kuchi ma’nosiz variantlar |
| 139 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 21 | tahrir | bo‘ylik → boylik; qiymatlar → qadriyatlar |
| 140 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 22 | tahrir | Ibn Sinodan kelib chiqqan dars → Ibn Sino haqidagi hikoyadan qanday saboq olish mumkin; oqitilmasa → o‘qitilmasa |
| 141 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 23 | tahrir | Kalit uzun va grammatik buzilgan; vaqtni qadrlash mazmunida qayta yozish |
| 142 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 25 | tahrir | yoshlarida → yoshlariga; universitetlarida → universitetlarda; chalg‘ituvchilarni grammatik tuzatish |
| 143 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 26 | tahrir | Hamma vaqtni xatotim qo‘lda ma’nosiz variant |
| 144 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 27 | tahrir | Ilmni o‘rganak, nazorat ko‘rsatish orqali buzilgan kalit; ilm o‘rganish va uni qo‘llash deb yozish |
| 145 | Odobnoma | 005_Ma’rifatparvarlik ajdodlarimizdan meros fazilat.json | 29 | tahrir | qaratilmoqdagi → qaratilishidan; ko‘rishish noto‘g‘ri fe’l; ilm taraqqiyotining maqsadini aniq so‘rash |
| 146 | Odobnoma | 006_Odob-axloq me’yorlari.json | 1 | tahrir | Ababosidan, Oqilmand kishisidan buzilgan variantlar |
| 147 | Odobnoma | 006_Odob-axloq me’yorlari.json | 2 | tahrir | Kuchlik, Jahvot, buziqchilik buzilgan variantlar |
| 148 | Odobnoma | 006_Odob-axloq me’yorlari.json | 3 | tahrir | Halal → halol; ta’rif aynan shu so‘zni takrorlaydi, rostgo‘ylik va haqqoniy mehnat bilan izohlash; Hiya-xandalak ma’nosiz |
| 149 | Odobnoma | 006_Odob-axloq me’yorlari.json | 4 | tahrir | uzoqlash haqida → uzoqlashish haqida |
| 150 | Odobnoma | 006_Odob-axloq me’yorlari.json | 5 | tahrir | Ehtiyotkorlikning umumiy ta’rifi tartib-intizom bilan aynan teng emas; «Donishmand ehtiyotkorlikka oid qanday nasihat bergan?» deb so‘rash |
| 151 | Odobnoma | 006_Odob-axloq me’yorlari.json | 6 | tahrir | Yolg‘on hech qachon aytish, Oxorida qayt fikrlaash, bermash buzilgan variantlar |
| 152 | Odobnoma | 006_Odob-axloq me’yorlari.json | 7 | tahrir | ko‘rpa katta, xushkul, pul ko‘p buzilgan variantlar |
| 153 | Odobnoma | 006_Odob-axloq me’yorlari.json | 8 | tahrir | Dunya qilib, gapib → oshkor qilib, gapirib |
| 154 | Odobnoma | 006_Odob-axloq me’yorlari.json | 9 | tahrir | Do‘stlikda muhim narsa haqiqiy do‘stlik deyish aylana ta’rif; do‘stlikdan manfaat kutmaslikni so‘rash |
| 155 | Odobnoma | 006_Odob-axloq me’yorlari.json | 10 | tahrir | Savolni «Kaykovus yangi do‘st topganda eski do‘stga qanday munosabatda bo‘lishni aytgan?» deb qayta tuzish; buzoqlash ma’nosiz |
| 156 | Odobnoma | 006_Odob-axloq me’yorlari.json | 11 | tahrir | e’tiroz uyg‘otsa va shaxs/fe’l moslashuvini tuzatish; qora qilishim noaniq |
| 157 | Odobnoma | 006_Odob-axloq me’yorlari.json | 12 | tahrir | Halol mehnat faqat kishi uchun tugallanmagan variant |
| 158 | Odobnoma | 006_Odob-axloq me’yorlari.json | 13 | tahrir | dega → degan; shukovat, erkabpoklik ma’nosiz |
| 159 | Odobnoma | 006_Odob-axloq me’yorlari.json | 14 | tahrir | dega → degan; kalitni ishni to‘liq bajarish uchun deb yozish |
| 160 | Odobnoma | 006_Odob-axloq me’yorlari.json | 15 | tahrir | asosiy qaysi → asosan qaysi; buzashtirish ma’nosiz |
| 161 | Odobnoma | 006_Odob-axloq me’yorlari.json | 16 | tahrir | Foyda va sevgi o‘latiga ma’nosiz variant |
| 162 | Odobnoma | 006_Odob-axloq me’yorlari.json | 17 | tahrir | Savol buzilgan; ilmli kishilardan qanday ibrat olish mumkin deb tuzish; keakligini → kerakligini |
| 163 | Odobnoma | 006_Odob-axloq me’yorlari.json | 18 | tahrir | savol so‘z tartibi, saqlab turish va do‘stlar ko‘payishi kaliti tahrirlansin |
| 164 | Odobnoma | 006_Odob-axloq me’yorlari.json | 19 | tahrir | keakligini → kerakligini; Dushmanni to‘kkalash ma’nosiz |
| 165 | Odobnoma | 006_Odob-axloq me’yorlari.json | 20 | tahrir | hammas nasihatlari hammasida → barcha nasihatlarida; Dunyo bo‘lishni o‘zgartirish ma’nosiz |
| 166 | Odobnoma | 006_Odob-axloq me’yorlari.json | 21 | tahrir | dega → degan; Buzoqlash ma’nosiz |
| 167 | Odobnoma | 006_Odob-axloq me’yorlari.json | 22 | tahrir | buyragi → nasihati; qiymat → qadriyat; adolat aniq kalit sifatida berilsin |
| 168 | Odobnoma | 006_Odob-axloq me’yorlari.json | 23 | tahrir | mehnati sevish → mehnatni sevish |
| 169 | Odobnoma | 006_Odob-axloq me’yorlari.json | 24 | tahrir | Tartibi va ehtiyotkorlikni barcha ishda rioya qilish grammatik buzilgan; oylar qilish ma’nosiz |
| 170 | Odobnoma | 006_Odob-axloq me’yorlari.json | 25 | tahrir | Hammas → hammasi; bahar → bahor; xususiyat → xususiyatlar |
| 171 | Odobnoma | 006_Odob-axloq me’yorlari.json | 26 | tahrir | Do‘stni xira qilmaslik → do‘stini xijolat qilmaslik; O‘zi biladimi yashirish ma’nosiz |
| 172 | Odobnoma | 006_Odob-axloq me’yorlari.json | 27 | tahrir | Savol eng yaxshisini so‘raydi, kalit uchalasini aytadi. «Kimlar bilan do‘st bo‘lish tavsiya etilgan?» deb tuzish |
| 173 | Odobnoma | 006_Odob-axloq me’yorlari.json | 28 | tahrir | dega → degan; qiymati → ma’naviy tayanchi; yarim pul ma’nosiz |
| 174 | Odobnoma | 006_Odob-axloq me’yorlari.json | 29 | tahrir | harakatlashgan, yoshar, xayir buzilgan; sababni ortiqcha umumlashtirmay, sodda vaziyatli savol tuzish |
| 175 | Odobnoma | 006_Odob-axloq me’yorlari.json | 30 | tahrir | hammas, kuchliki, hammas xul, mehnati, yoshash buzilgan; savol va variantlarni to‘liq adabiy tilda qayta yozish |
| 176 | O‘qish | 005_Mahallam ajib ko'rkam.json | 8 | tahrir | «bilalar», «Ko‘zbiyallag‘ich, båkinmachiq va siqqa» buzilgan. O‘yin nomlari asl matn bilan solishtirib tiklansin. |
| 177 | Rus tili | 001_В школе.json | 2 | tahrir | «Feruza kimdir?» → «Feruza kim?»; «O‘quvchisidir» → «O‘quvchi». |
| 178 | Rus tili | 001_В школе.json | 9 | tahrir | «Shkolning direktyori kimdir?» jumlasi adabiy o‘zbekchada «Maktab direktori kim?» shaklida yozilsin. |
| 179 | Tabiatshunoslik | 001_Tabiatshunoslik nimani o'rganadi.json | 6 | tahrir | «Cho‘lla» → «Cho‘llar». |
| 180 | Tarbiya | 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json | 5 | tahrir | Belgilangan «Muhim damda, o‘zgarlik ko‘rsatishda» javobi tushunarsiz. Savol darslikdagi ‘o‘ng qo‘l qoidasi’ mazmuniga ko‘ra qayta tuzilsin. |
| 181 | Tarbiya | 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json | 6 | tahrir | «Nima qilmaslik kerak?» savoliga «xalaqit qilmaslik» javobi ikki inkor hosil qiladi; savol va variantlar bir xil mantiqiy shaklga keltirilsin. |
| 182 | Tarbiya | 001_2-SINFDA O'RGANGANLARIMIZNI TAKRORLAYMIZ.json | 8 | tahrir | «Jarohalarishlashning» → «Jarohatlanishning». |
| 183 | Tasviriy san’at | 001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json | 7 | tahrir | «To‘g‘ri o‘tirish qanday? — To‘g‘ri» aylana ta’rif; to‘g‘ri holat belgilari aniq yozilsin. |
| 184 | Tasviriy san’at | 001_Rasm ishlash uchun joy hozirlash va narsalarning o'lchamini.json | 10 | tahrir | Kalitdagi «tuza va ishlaydigan» grammatik buzilgan; «San’at asarlarini yaratadi» shakli mos. |
| 185 | Texnologiya | 001_«Kuz» manzarasini applikatsiya usulida yasash.json | 8 | tahrir | «Detalllarni» → «Detallarni»; savol «Applikatsiya yasash qaysi bosqichdan boshlanadi?» shaklida yozilsin. |
| 186 | Texnologiya | 001_«Kuz» manzarasini applikatsiya usulida yasash.json | 9 | tahrir | «Rang tutirib» buzilgan chalg‘ituvchi variant; mazmunli variant bilan almashtirilsin. |

## Jamlanma muammolari

| Fan | `_TOLIQ.json`ga kirmagan fayl | Ulardagi savol | Takror ishlatilgan mavzu raqami |
|---|---:|---:|---:|
| Ingliz tili | 0 | 0 | 0 |
| Matematika | 0 | 0 | 0 |
| Musiqa | 0 | 0 | 0 |
| Odobnoma | 0 | 0 | 0 |
| Ona tili | 0 | 0 | 0 |
| O‘qish | 87 | 2574 | 75 |
| Rus tili | 0 | 0 | 0 |
| Tabiatshunoslik | 31 | 926 | 31 |
| Tarbiya | 1 | 29 | 1 |
| Tasviriy san’at | 17 | 506 | 17 |
| Texnologiya | 0 | 0 | 0 |

Jamlanmaga kirmagan fayllarning to‘liq ro‘yxati `3_SINF_JAMLANMAGA_KIRMAGAN_FAYLLAR.csv` faylida. Bir xil mavzu raqami ishlatilishi avtomatik ravishda dublikat degani emas: ko‘p joyda `a/b` yoki turli matnli mavzular bor. Shu sababli ular avtomatik o‘chirilmadi.

## Texnik tekshiruv

- 530 ta alohida JSON fayl ochildi.
- Har bir savolda 4 ta bo‘sh bo‘lmagan variant va 0–3 oralig‘idagi javob indeksi bor.
- Barcha mavjud mavzu TXT nusxalari JSON savol, variant va javob kalitiga mos.
- Aynan bir xil variantli savol topilmadi.
- Oddiy arifmetik shablonga mos 578 savol qayta hisoblandi; noto‘g‘ri kalit signali topilmadi.
- 13 ta teng son qiymatli variant signali qo‘lda ko‘rildi. Ko‘pchiligi savolning shakli sababli xato emas; Matematika 013:5 va 033:1 savollariga kontekst qo‘shish kerak.
- O‘qish fanida 559 ta g‘ayrioddiy belgi signali bor. Signal soni xatolar soni emas, ammo `Vàtàn`, `o‘chîg‘i`, `båkinmachiq` kabi real matn buzilishlari qolgan.

## Hisobot fayllari

- `3_SINF_TUZATISHLAR.csv` — tuzatish jurnalidagi 2 435 ta alohida savolning eski va yangi ko‘rinishi.
- `3_SINF_QOLGAN_MUAMMOLAR.csv` — o‘zgarishsiz qolgan barcha tahrir/manba qaydlari, amaldagi savol va belgilangan javob bilan.
- `3_SINF_JAMLANMAGA_KIRMAGAN_FAYLLAR.csv` — `_TOLIQ.json` jamlanmalarida yo‘q barcha alohida mavzu fayllari.

## Chegara

Bu hisobot mavjud audit dalillari va amaldagi fayllarning qayta texnik tekshiruviga asoslangan. Tarixiy, adabiy va darslikka bog‘liq har bir da’vo asl darslik bilan boshidan oxirigacha qayta tasdiqlanmagan. `Manba kerak` holatidagi savollar shuning uchun tayyor deb hisoblanmaydi. Musiqa va Ona tili testlari yaratilmaguncha 3-sinfning barcha fanlari to‘liq tayyor bo‘ldi deb bo‘lmaydi.
