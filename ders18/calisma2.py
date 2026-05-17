"""
Tapşırıq 2: Oyunçu (Gamer) Sinifi
Tələblər:

Oyunçu adlı bir sinif yaradın.
Sinifdə aşağıdakı private (__) atributlar olmalıdır:
    __ad – Oyunçunun adı.
    __səviyyə – Oyunçunun səviyyəsi (default olaraq 1).
    __xal – Oyunçunun qazandığı xal (default olaraq 0).

Aşağıdakı metodları yazın:
    __init__(self, ad) – Oyunçunun adını təyin etsin, səviyyə və xal isə default olaraq təyin olunsun.
    məlumat_göstər(self) – Oyunçunun adını, səviyyəsini və xalını qaytarsın.
    xal_əlavə_et(self, xal) – Yeni xal əlavə etsin və əgər xal 100 və ya daha çox olarsa, oyunçunun səviyyəsini 1 artırıb, xalı 0-a sıfırlasın.

Private atributlara birbaşa giriş olmasın!

---
Nümunə İstifadə:

oyunçu = Oyunçu("Ali")
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 1, Xal: 0
oyunçu.xal_əlavə_et(50)
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 1, Xal: 50
oyunçu.xal_əlavə_et(60)  # Təbriklər! Ali yeni səviyyəyə keçdi!
print(oyunçu.məlumat_göstər())  # Oyunçu: Ali, Səviyyə: 2, Xal: 0
"""

class Oyuncu:
    def __init__(self, ad):
        self.__ad = ad
        self.__seviyye = 1
        self.__xal = 0

    def melumat_goster(self):
        return f"Oyuncu adi: {self.__ad}\nSeviyye: {self.__seviyye}\nXal: {self.__xal}"

    def xal_elave_et(self, xal):
        self.__xal += xal
        if self.__xal >= 100:
            self.__seviyye += 1 and self.__xal == 0
            print(f"Təbriklər! {self.__ad} yeni səviyyəyə keçdi!")

oyuncu = Oyuncu("Ali")
print(oyuncu.melumat_goster())  # Oyunçu: Ali, Səviyyə: 1, Xal: 0
oyuncu.xal_elave_et(50)
print(oyuncu.melumat_goster())  # Oyunçu: Ali, Səviyyə: 1, Xal: 50
oyuncu.xal_elave_et(160)  # Təbriklər! Ali yeni səviyyəyə keçdi!
print(oyuncu.melumat_goster())  # Oyunçu: Ali, Səviyyə: 2, Xal: 0