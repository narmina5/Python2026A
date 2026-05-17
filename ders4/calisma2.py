"""
İstifadəçinin Yaşına Əsasən Mesaj Göstərin

İstifadəçidən yaşını daxil etməsini istəyin.
Yaşa əsasən kateqoriya təyin edin:
    0-12: “Uşaqsınız.”
    13-19: “Gəncsiniz.”
    20-59: “Böyüksünüz.”
    60 və yuxarı: “Ahılsınız.”
"""
yas = int(input("Yasinizi daxil edin: "))

if 60 <= yas:
    print("Ahilsiniz")
elif 59 >= yas >= 20:
    print("Boyuksunuz")
elif 19 >= yas >= 13:
    print("Gencsiniz")
elif 12 >= yas >= 0:
    print("Usaqsiniz")
else:
    print("Yas uygun deyil")