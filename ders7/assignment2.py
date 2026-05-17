"""
İstifadəçidən bir tam ədəd (n) alın və bu ədədin bütün rəqəmlərini əks istiqamətdə çevirərək yeni bir ədəd yaradın.

Sonra həmin yeni ədədin tək və ya cüt olduğunu yoxlayın.

Məs.
n = 3588
Əksinə çevrilmiş ədəd: 8853
Təkdir
"""

tam_eded = input("Tam eded daxil edin: ")
for n in tam_eded:
    tam_eded = tam_eded[::-1]
    print(f'Eksine cevrilmis eded: {tam_eded}')
    break

if int(tam_eded) % 2 == 0:
    print("Cutdur")
else:
    print("Tekdir")