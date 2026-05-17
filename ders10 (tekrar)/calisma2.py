"""
Tapşırıq 2: Alış-Veriş Siyahısı
Bir proqram yazın:

1) Boş bir list yaradın.
2) İstifadəçidən məhsul adları alın və listə əlavə edin.
3) İstifadəçi "stop" yazanda məhsul əlavə etmə dayansın.
4) Daha sonra listdəki bütün məhsulları sıra nömrəsi ilə birlikdə çap edin.
5) Sonda:
   - neçə məhsul daxil edildiyini göstərin
   - ən uzun adlı məhsulu tapıb çap edin
   - əgər siyahı boşdursa, uyğun mesaj verin

Qeyd:
- while ilə məlumat alın
- for ilə listi gəzin
- str və list istifadə edin
- if-else ilə boş siyahını yoxlayın
"""

siyahi = []

while True:
    mehsul_adlari = input("mehsul: ")
    if mehsul_adlari == "stop":
        break
    siyahi.append(mehsul_adlari)

for index, mehsul in enumerate(siyahi):
    print(f'{index}. mehsul: {mehsul}')




print(f'Umumi mehsul sayi: {len(siyahi)}')

if siyahi == []:
    print("Siyahi bosdur")
else:
    uzun_mehsul = siyahi[0]
    for string in siyahi:
        if len(string) > len(uzun_mehsul):
            uzun_mehsul = string
    print(f'En uzun mehsul: {uzun_mehsul}')
