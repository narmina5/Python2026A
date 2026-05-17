"""
Döngüdən istifadə edərək 0-dan 100-ə qədər olan tam ədədlərdən:
5-ə tam bölünən ədədləri
15-ə tam bölünən ədədləri
Kvadratı 50 və 200 arasında olan tam ədədləri (böyükdən kiçiyə sıralı)
çap edin (terminala yazdırın)

İpucular:
Əvvəlcə for-un çölündə boş list(lər)inizi təyin edin. Məs: beshe_bölünən_ədədlər = []
for döngüsünün içində .append() funksiyasından istifadə edərək həmin listlərə dəyərlər əlavə edin (əlbəttə if, else ve ya elif istifadə edərək kontrol etməlisiniz)
for döngü bloklarının içində if-else-elif və digər öyrəndiyimiz bilgiləri istifadə edə bilərsiniz
köməklik edəcək bəzi açar sözlər: for, if, else, elif, reverse, append, print, range
"""

bese_bolunen_ededler = []
onbese_bolunen_ededler = []
kv_elli_ikiyuz_arasinda_ededler = []

for n in range(0, 101):
    if n % 5 == 0:
        bese_bolunen_ededler.append(n)
    if n % 15 == 0:
        onbese_bolunen_ededler.append(n)
    if 50 <= n**2 <= 200:
        kv_elli_ikiyuz_arasinda_ededler.append(n)

print("5e bolunen ededler: ", bese_bolunen_ededler)
print("15e bolunen ededler: ", onbese_bolunen_ededler)
print("kvadrati 50 ve 200 arasinda olan ededler: ", kv_elli_ikiyuz_arasinda_ededler)
