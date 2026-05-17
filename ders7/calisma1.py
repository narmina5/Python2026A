"""
Müəyyən bir zoopark qonağın yaşına əsasən biletin qiymətini müəyyən edir.

 - 2 yaş və daha kiçik qonaqlar ödənişsiz qəbul edilir.
 - 3-12 yaş arası uşaqlar 14.90 dollara başa gəlir.
 - 65 yaşdan yuxarı yaşlılar üçün 18.90 dollara başa gəlir.
 - Bütün digər qonaqlar üçün giriş 23.90 dollardır.

Hər sətirdə bir yaş daxil edilməklə, istifadəçidən qrupdakı bütün qonaqların yaşlarını oxumaqla başlayan proqram yaradın.
İstifadəçi qrupda artıq qonaq olmadığını bildirmək üçün boş sətir (enter və ya space) daxil edəcək.

Sonra proqramınız müvafiq mesajla qrup üçün biletlərin ümumi qiymətini göstərməlidir.
Son qiymət nöqtədən sonra iki onluq rəqəmdən istifadə etməklə göstərilməlidir (Məs. 89.70)

Qaynaq: The Python Workbook, Ben Stephenson
"""

qonaqlar = []
hesab = 0
while True:
    qonaq = input("Yasiniz necedir? \n")
    if qonaq.strip() == "":
        break
    else:
        qonaqlar.append(int(qonaq))
for i in qonaqlar:
    if i > 65:
        hesab += 18.90
    elif 3 <= i < 12:
        hesab += 14.90
    elif i <= 2:
        pass
    else:
        hesab += 23.90

print(f"Umumi hesab: {hesab}$")