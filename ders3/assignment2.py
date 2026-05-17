"""
Tam adınızı (ad boşluq soyad) saxlayan tam_ad dəyişəni yaradın.

Sətir metodlarından istifadə edərək:
Ad və Soyadınızın yalnız ilk hərfini böyük hərfə çevirin, çap edin.
Tam adınızı tamamilə böyük və kiçik hərflərə çevirin, çap edin.
Tam adınızda müəyyən bir hərfin neçə dəfə təkrarlandığını hesablayın, çap edin.
Tam adınızdakı istədiyiniz hərfi başqa hərflə əvəz edin, çap edin.
Tam adınızın uzunluğunu göstərin (nəzərə alaq ki tam_ad dəyişkəni ad boşluq soyad, məs.: Fərid Hüseynov kimi daxil edilmişdir, uzunluq = 14)
Kəsim (slicing) edərək:
Tam adınızın ilk üç hərfini göstərin.
Tam adınızın son hərfini göstərin.
Tam adınızın son 3 hərfini göstərin.
Tam adınızı tərsinə göstərin (vonyesüH dirəF)
"""

name = input("Ad: ")
lname = input("Soyad: ")
tam_ad = name + " " + lname
print(tam_ad.title())
print(tam_ad.upper())
print(tam_ad.lower())
print(tam_ad.count("a"))
print(tam_ad.replace("a", "e"))
print(len(tam_ad))
print(tam_ad[:3])
print(tam_ad[-1])
print(tam_ad[-3:])
print(tam_ad[::-1])