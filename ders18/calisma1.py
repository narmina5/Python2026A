"""
Kitabxana Sistemi
Tələblər:

 - Kitab adlı bir sinif yaradın.

Sinifdə aşağıdakı private (__) atributlar olmalıdır:
    __ad – Kitabın adı.
    __müəllif – Kitabın müəllifi.
    __səhifə_sayı – Kitabın səhifə sayı.

Aşağıdakı metodları yazın:
    __init__(self, ad, müəllif, səhifə_sayı) – Kitabın atributlarını təyin etsin.
    kitab_məlumatı(self) – Kitabın adını, müəllifini və səhifə sayını qaytarsın.
    səhifə_sayıni_dəyiş(self, yeni_sayı) – Yeni səhifə sayı təyin etsin, amma əgər səhifə sayı 0 və ya mənfidirsə, dəyişməsin və xəbərdarlıq versin.

Private atributlara birbaşa giriş olmasın!

Həmin class bu cür işlədilib comment hissəsindəki kimi output alacaq şəkildə yazılmalıdır.

kitab = Kitab("1984", "George Orwell", 328)
print(kitab.kitab_məlumatı())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 328
kitab.səhifə_sayıni_dəyiş(-50)  # Səhifə sayı 0 və ya mənfi ola bilməz!
kitab.səhifə_sayıni_dəyiş(400)
print(kitab.kitab_məlumatı())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 400

"""

class Kitab:
    def __init__(self, ad, muellif, sehife_sayi):
        self.__ad = ad
        self.__muellif = muellif
        self.__sehife_sayi = sehife_sayi

    def kitab_melumati(self):
        return f"Kitab: {self.__ad}\nMuellif: {self.__muellif}\nSehife sayi: {self.__sehife_sayi}"

    def sehife_sayini_deyis(self, yeni_sayi):
        if yeni_sayi <= 0:
            print("Sayi 0 ve ya menfi ola bilmez")
        else:
            self.__sehife_sayi = yeni_sayi

kitab = Kitab("1984", "George Orwell", 328)
print(kitab.kitab_melumati())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 328
kitab.sehife_sayini_deyis(-50)  # Səhifə sayı 0 və ya mənfi ola bilməz!
kitab.sehife_sayini_deyis(400)
print(kitab.kitab_melumati())  # Kitab: 1984, Müəllif: George Orwell, Səhifələr: 400