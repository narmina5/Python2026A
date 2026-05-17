"""
Tapşırıq 1: Gizli Ədədi Tap
Bir proqram yazın:

1) Proqram daxilində gizli bir ədəd təyin edin. Məsələn: 17
2) İstifadəçidən bu ədədi tapmağa çalışmasını istəyin.
3) İstifadəçinin maksimum 7 cəhdi olsun.
4) Hər dəfə istifadəçi ədəd daxil etdikdə:
   - əgər doğru tapıbsa: "Təbriklər, gizli ədədi tapdınız!" yazılsın və döngü dayansın
   - əgər daxil etdiyi ədəd kiçikdirsə: "Daha böyük ədəd daxil edin"
   - əgər daxil etdiyi ədəd böyükdürsə: "Daha kiçik ədəd daxil edin"
5) İstifadəçi 7 cəhdin sonunda tapa bilməsə:
   - "Uduzdunuz. Gizli ədəd 17 idi" yazılsın
6) Sonda istifadəçinin neçə cəhd istifadə etdiyi də göstərilsin

Qeyd:
- while döngüsü istifadə edin
- if-else istifadə edin
- int və bool ilə işləyin
"""

gizli_eded = 26
count = 0

while count < 7:
    ferz = int(input("Gizli ededi tap: "))
    if ferz == gizli_eded:
        count += 1
        print("Tebrikler, gizli ededi tapdiniz!")
        break
    else:
        if ferz < gizli_eded:
            print("Daha boyuk eded daxil edin")
        elif ferz > gizli_eded:
            print("Daha kicik eded daxil edin")
        count += 1


else:
    print(f'Uduzdunuz. Gizli eded {gizli_eded} idi')

print(f'{count} cehd istifade etdiniz')

