"""
Istifadəçidən istifadəçi adı və şifrə alın. Yazacağınız kod istifadəçi adı və şifrəni yoxlayıb müxtəlif şərtlər və mesajlar göstərməlidir. Tapşırıq həm string, həm də şərt strukturlarını və əhatə edir.Şərtlər:
Əgər adın uzunluğu 3 simvoldan qısadırsa, "Ad çox qısadır." mesajını göstərin.
Əgər adın uzunluğu 15 simvoldan uzundursa, "Ad çox uzundur." mesajını göstərin.
Əks halda, "Ad qəbul edildi." yazdırın.
Şifrə ən azı 8 simvol olmalıdır. Əgər deyilirsə, "Şifrə çox qısadır." mesajını göstərin.
Əgər şifrə tamamilə rəqəmlərdən ibarətdirsə, "Şifrə tam rəqəm ola bilməz." mesajını yazdırın.
Şifrənin ilk hərfi böyük hərf olmalıdır. Əgər deyilirsə, "Şifrənin ilk hərfi böyük olmalıdır." yazdırın.
Şifrənin sonunda "!" işarəsi olmalıdır. Əgər deyilirsə, "Şifrə '!' ilə bitməlidir." mesajını göstərin.
"Qeydiyyat uğurla tamamlandı!" yazdırın.
"""

account = str(input("Istifadeci adi: "))

if len(account) < 3:
    print("Ad cox qisadir.")
elif len(account) > 15:
    print("Ad cox uzundur.")
else:
    print("Ad qebul edildi.")
    password = input("Sifre: ")
    if len(password) <= 8:
        print("Sifre cox qisadir.")
    if password.isdigit() == True:
        print("Sifre tam reqem ola bilmez.")
    if password.istitle() != True:
        print("Sifrenin ilk herfi boyuk olmalidir.")
    if password[-1] != "!":
        print("Sifre '!' ile bitmelidir.")
    else:
        print("Qeydiyyat ugurla tamamlandi!")