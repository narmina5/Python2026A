"""
  BankHesabi adlı bir sinif yaradın. Bu sinifdə müştərinin adı, email adresi, hesab nömrəsi və balansı saxlanmalıdır. Hesaba pul yatırmaq, çıxarmaq və balans yoxlamaq üçün metodlar yaradın.

  Tapşırıq:

   - BankHesabi sinifini yaradın və ad, email adresi, hesab_nomresi, balans atributlarını əlavə edin.
   - pul_yatir metodunu yaradın ki, müştəri hesabına müəyyən bir məbləğ yatırsın və balans artsın.
   - pul_cixar metodunu yaradın ki, müştəri hesabından müəyyən bir məbləğ çıxarsın və balans azalsın.
   - balans_goster metodunu yaradın ki, müştərinin cari balansını ekrana çap etsin.
   - tam_melumat metodu yaradın ki, müştərinin bütün məlumatlarını ekrana çap etsin

   İstifadəçiyə sonsuz menyu göstərin və bir əməliyyat etməsi üçün hərf daxil etməsini istəyin:

      - i: Məlumatları gör (bütün məlumatları versin)
      - +: Balansı artır (istifadəçi yazdığı məbləğ qədər balansı artırsın)
      - -: Pul çıxartmaq (istifadəçi yazdığı məbləğ qədər balansı azaltsın)
      - b: Balansı göstər
      - x: Çıxış
"""

class BankHesabi:
    def __init__(self, ad, email_adres, hesab_nomresi, balans=0):
        self.ad = ad
        self.email_adres = email_adres
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def pul_yatir(self, mebleg):
        if mebleg > 0:
            self.balans += mebleg
            print(f"{mebleg} AZN hesaba yatirildi")
        else:
            print("Yatirilan mebleg 0-dan boyuk olmalidir")


    def pul_cixar(self, mebleg):
        if mebleg <= 0:
            print("Yatirilan mebleg 0-dan boyuk olmalidir")
        elif self.balans < mebleg:
            print("Balansda kifayet qeder vesait yoxdur")
        else:
            self.balans -= mebleg
            print(f"{mebleg} AZN hesabdan cixarildi")


    def balans_goster(self):
        print(f'Balans: {self.balans} AZN')


    def tam_melumat(self):
        print(f'Ad: {self.ad}\nEmail adres: {self.email_adres}\nHesab nomresi: {self.hesab_nomresi}\nBalans: {self.balans}')



if __name__ == "__main__":

    hesab1 = BankHesabi("Narmin", "narminmailova5@gmail.com", "4169.......", 50)

    while True:
        print("i: Məlumatları gör")
        print("+: Balansı artır")
        print("-: Pul çıxartmaq")
        print("b: Balansı göstər")
        print("x: Çıxış")

        secim = input("Emeliyyati sec: ").casefold()
        if secim == "i":
            hesab1.tam_melumat()
        elif secim == "+":
            mebleg = float(input("Meblegi daxil edin: "))
            hesab1.pul_yatir(mebleg)
        elif secim == "-":
            mebleg = float(input("Meblegi daxil edin: "))
            hesab1.pul_cixar(mebleg)
        elif secim == "b":
            hesab1.balans_goster()
        elif secim == "x":
            print("Emeliyyat bitdi. Ana sehifeye kecid olunur...")
            break
        else:
            print("Yalnis secim etdiniz, yeniden cehd edin")


    hesab1.tam_melumat()
    hesab1.pul_yatir(150)
    hesab1.pul_cixar(500)
    hesab1.pul_cixar(15)
    hesab1.balans_goster()
