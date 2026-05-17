"""
Tapşırıq 1: Şifrəli Xəzinə Sandığı
Bir proqram yazın:

1) İstifadəçidən gizli şifrə soruşulsun.
2) Doğru şifrə "python123" olsun.
3) İstifadəçinin maksimum 3 cəhd haqqı olsun.
4) Əgər şifrə doğrudursa:
   - "Xəzinə açıldı!" mesajı çap edilsin.
5) Əgər 3 dəfə səhv daxil etsə:
   - "Xəzinə kilidləndi!" mesajı çap edilsin.
6) Hər səhv cəhddən sonra neçə cəhd haqqı qaldığı göstərilsin.

Qeyd:
- while döngüsü istifadə edin
- if-else istifadə edin
- string ilə işləyin
- bool tipindən istifadə edə bilərsiniz
"""

dogru_sifre = "Python123"
count = 0

while count < 3:
    gizli_sifre = input("Gizli sifre? ")
    if gizli_sifre == dogru_sifre:
        print("Xezine acildi!")
        break
    else:
        count += 1
        print(f'{3 - count} cehdiniz qaldi ')

else:
    print("Xezine kilidlendi!")

