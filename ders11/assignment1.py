"""
Sən gizli bir cəmiyyətin giriş nəzarət sistemini idarə edirsən.

Hər gün qr-kodla daxil olan üzvlərin adları sistemə düşür, amma sistem çox qarışıqdır:
- adlar böyük/kiçik hərflərlə qarışıq yazılıb
- vergüllər çoxdur
- boş adlar var
- təkrarlanan adlar var
- saxta ID-lər var
- qadağan olunmuş şəxslər var
- bir yerdə görünməsi qadağan olunan “cütlüklər” var

Sənin işin: bütün bu qarışıq məlumatı SET-lərlə təmizləmək və analiz etməkdir.

=====================================================
📌 VERİLƏN MƏLUMAT (bunları eynilə kodda saxla)
=====================================================

day1_raw = "  ali,   Lale, ,RENA,,  Farid, ali,    MILAN, , ,   Elvin "
day2_raw = "Rena, Samir,,   farid, ,Lale ,Huseyn, milan, ,"
day3_raw = "Kamran, ,  Lale,   Aytac, AYtAC ,  samir"

restricted_people = {"Milan", "Kamran"}
fake_ids = {"", " ", "  "}
banned_pairs = {("Lale", "Samir"), ("Farid", "Milan")}

=====================================================
📝 TAPŞIRIQLAR
=====================================================

1️⃣ Hər günün məlumatını təmizlə
Qaydalar:
- vergüllərə görə split et
- boşluqları strip et
- kiçik hərfə çevir
- fake_ids daxil olan boş adları sil
- set-ə çevirib təkrarlananları təmizlə
- sonra döngü ilə hər adın ilk hərfini böyük hərf et

Çap et:
Day 1 clean: ...
Day 2 clean: ...
Day 3 clean: ...

-----------------------------------------------------

2️⃣ Üç günün hamısında gələnləri tap (kəsişmə – triple intersection)

-----------------------------------------------------

3️⃣ DƏQİQ OLARAQ 2 gün gələnləri tap
Yəni: bir adam 3 gün yox, tam 2 gün gəlməlidir.

-----------------------------------------------------

4️⃣ “Ghost visitors” tap
Yalnız 3-cü gün gələnlər:

-----------------------------------------------------

5️⃣ Bütün nəticələrdən restricted_people sil

-----------------------------------------------------

6️⃣ QADAĞAN OLUNMUŞ CÜTLÜKLƏRİ YOXLA
Hər qadağan olunmuş cütlük eyni gündə görünübsə, xəbərdarlıq yaz:

Nümunə çıxış:
Banned pair detected on Day 2: Farid & Milan
Banned pair detected on Day 1: Lale & Samir

İPUCU: yalnız döngü + set membership istifadə etmək olar.

-----------------------------------------------------

7️⃣ “Sadiqlik cədvəli” qur (SCOREBOARD)

Qaydalar:
- all_people = day1 ∪ day2 ∪ day3
- Hər insan üçün 1 gün = 1 bal
- Döngü ilə say
- Nəticəni list of tuples kimi saxla:
    ("Rena", 3)
    ("Farid", 2)
    ("Aytac", 1)
- Sonra sırala

-----------------------------------------------------

8️⃣ “Elit üzvləri” tap
Qaydalar:
- skor ≥ 2
- restricted_people daxilində olmamalıdır
- adın uzunluğu ≥ 4
- banned_pairs daxil olan heç bir cütlükdən biri olmamalıdır
- 1-ci və ya 3-cü gün gəlmiş olmalıdır

Yalnız SET-lər + döngülərlə.

-----------------------------------------------------

9️⃣ Set-lərlə müəyyən et:

“1-ci gün gəlməyənlər”  ⊇  “yalnız 3-cü gün gələnlər” ?

Çap et:
Superset check: True   # və ya False
"""

day1_raw = "  ali,   Lale, ,RENA,,  Farid, ali,    MILAN, , ,   Elvin "
day2_raw = "Rena, Samir,,   farid, ,Lale ,Huseyn, milan, ,"
day3_raw = "Kamran, ,  Lale,   Aytac, AYtAC ,  samir"

restricted_people = {"Milan", "Kamran"}
fake_ids = {"", " ", "  "}
banned_pairs = {("Lale", "Samir"), ("Farid", "Milan")}

"""
1️⃣ Hər günün məlumatını təmizlə
"""
day1_raw = [day1_raw.strip().lower() for day1_raw in day1_raw.split(",")]
day2_raw = [day2_raw.strip().lower() for day2_raw in day2_raw.split(",")]
day3_raw = [day3_raw.strip().lower() for day3_raw in day3_raw.split(",")]
day1_clean = set(day1_raw)
day2_clean = set(day2_raw)
day3_clean = set(day3_raw)

for dataset in (day1_clean, day2_clean, day3_clean):
    for ad in set(dataset):
        if ad in fake_ids:
            dataset.remove(ad)
print(f'Day 1 clean: {day1_clean}')
print(f'Day 2 clean: {day2_clean}')
print(f'Day 3 clean: {day3_clean}')

print("=" * 100)

"""
2️⃣ Üç günün hamısında gələnləri tap (kəsişmə – triple intersection)
"""
print(day1_clean.intersection(day2_clean, day3_clean))

print("=" * 100)

"""
3️⃣ DƏQİQ OLARAQ 2 gün gələnləri tap
"""
print(day1_clean.intersection(day2_clean).difference(day3_clean))

print("=" * 100)

"""
4️⃣ “Ghost visitors” tap
Yalnız 3-cü gün gələnlər:
"""
print(day3_clean.difference(day1_clean, day2_clean))

print("=" * 100)

"""
5️⃣ Bütün nəticələrdən restricted_people sil
"""
restricted_people = {ad.lower() for ad in restricted_people}
for dataset in (day1_clean, day2_clean, day3_clean):
    for ad in set(dataset):
        if ad in restricted_people:
            dataset.remove(ad)
print(f'Day 1 clean: {day1_clean}')
print(f'Day 2 clean: {day2_clean}')
print(f'Day 3 clean: {day3_clean}')

print("=" * 100)

"""
6️⃣ QADAĞAN OLUNMUŞ CÜTLÜKLƏRİ YOXLA
"""
for pair in banned_pairs:
    a = pair[0]
    b = pair[1]
    if a in day1_clean and b in day1_clean:
        print(f'Banned pair detected on Day 1: {a} & {b}')

for pair in banned_pairs:
    a = pair[0]
    b = pair[1]
    if a in day2_clean and b in day2_clean:
        print(f'Banned pair detected on Day 2: {a} & {b}')

for pair in banned_pairs:
    a = pair[0]
    b = pair[1]
    if a in day3_clean and b in day3_clean:
        print(f'Banned pair detected on Day 3: {a} & {b}')

print("=" * 100)

"""
7️⃣ “Sadiqlik cədvəli” qur (SCOREBOARD)
"""
all_people = day1_clean.union(day2_clean.union(day3_clean))
scoreboard = []

for person in all_people:
    day_count = 0
    if person in day1_clean:
        day_count += 1
    if person in day2_clean:
        day_count += 1
    if person in day3_clean:
        day_count += 1

    scoreboard.append((person.title(), day_count))

print(scoreboard)

print("=" * 100)

"""
8️⃣ “Elit üzvləri” tap
Qaydalar:
- skor ≥ 2
- restricted_people daxilində olmamalıdır
- adın uzunluğu ≥ 4
- banned_pairs daxil olan heç bir cütlükdən biri olmamalıdır
- 1-ci və ya 3-cü gün gəlmiş olmalıdır
"""
elit_uzvler = set()
for dataset in (day1_clean, day2_clean, day3_clean):
    for ad in dataset:
        for name, score in scoreboard:
            if name.lower() == ad and score >= 2:
                elit_uzvler.add(ad)
            if ad not in restricted_people:
                elit_uzvler.add(ad)
            if len(ad) >= 4:
                elit_uzvler.add(ad)
            if ad not in banned_pairs:
                elit_uzvler.add(ad)
            if ad in day1_clean.intersection(day3_clean):
                elit_uzvler.add(ad)

print(elit_uzvler)

print("=" * 100)

"""
9️⃣ Set-lərlə müəyyən et:
“1-ci gün gəlməyənlər”  ⊇  “yalnız 3-cü gün gələnlər” ?
"""
print(f'Superset check: {day2_clean.union(day3_clean).difference(day1_clean).issuperset(day3_clean.difference(day1_clean, day2_clean))}')
