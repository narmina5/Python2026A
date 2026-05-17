# =============================================================================
# TAPŞIRIQ 3 — Dərs 6–7: for, range, while, break və ya continue
# =============================================================================
"""
"Cüt rəqəmlər və menyu".

Hissə A — for və range:
  50-dən 150-yə qədər (150 daxil olmaqla) yalnız 4-ə qalıqsız bölünən ədədləri
  çap edin. Neçə ədəd olduğunu da sonda göstərin.

Hissə B — while və şərt:
  İstifadəçidən 1 ilə 10 arasında (hər iki sərhəd daxil) gizli bir rəqəm təyin edin
  (kodda sabit: məs. gizli = 7). İstifadəçi yanlış daxil etdikcə yenidən soruşun.
  Düzgün tapanda "Duzgun!" yazıb döngüdən çıxın (break istifadə edə bilərsiniz).

İstəyə bağlı: yanlış cəhdlərdə continue ilə əlavə mesaj göstərin.
"""

# Hisse A
yalniz_4e_bolunenler = []
for a in range(50, 151):
    if a % 4 == 0:
        yalniz_4e_bolunenler.append(a)
print(f'Yalniz 4e qaliqsiz bolunen ededler: {yalniz_4e_bolunenler}, \nEdedlerin sayi: {len(yalniz_4e_bolunenler)}')

# Hisse B
gizli = 7
while True:
    eded = int(input("1 ile 10 arasinda eded daxil et: "))
    if eded in range(1, 11):
        if eded == gizli:
            print("Duzgun!")
            break
        else:
            print("Yanlis cehd!")
            continue
    else:
        print("Eded 1 ile 10 arasinda olmalidir!")
        continue