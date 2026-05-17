"""
Restoranın menyusunu idarə edən sinif yaradın. Siz yeməkləri əlavə edib silə bilərsiniz və bütün menyunu göstərə bilərsiniz.

Tapşırıqın detalları:
RestaurantMenu adlı sinif yaradın.Sinifdə menyu dictionary'si saxlayın.Aşağıdakı metodları yaradın:
add_meal(name, price): Yeni yemək adi ilə qiyməti əlavə edir.
delete_meal(name): Menyudan yeməyi silir.
show_price(): Bütün menyunu çap edir.
get_price(): Verilən yeməyin qiymətini qaytarır
Bir neçə restoranlar yaradıb üzərində əməliyyatlar edin.
İstərsəniz, özünüzdən əlavə funksionallıqlar da yaza bilərsiniz.

İstifadəçiyə sonsuz menyu göstərin və bir əməliyyat etməsi üçün hərf daxil etməsini istəyin:

- i: Məlumatları gör (bütün məlumatları versin)
- +: Balansı artır (istifadəçi yazdığı məbləğ qədər balansı artırsın)
- -: Pul çıxartmaq (istifadəçi yazdığı məbləğ qədər balansı azaltsın)
- b: Balansı göstər
- x: Çıxış
"""

class RestaurantMenu:
    def __init__(self):
        self.menu = {}

    def add_meal(self, name, price):
        name = name.strip().casefold()
        self.menu[name] = price
        print(f'{name}: {float(price)} AZN - menyuya elave edildi!')

    def delete_meal(self, name):
        if name in self.menu:
            del self.menu[name]
            print(f'{name} menyudan silindi')
        else:
            print("Bu yemek adi movcud deyil")

    def show_price(self):
        print(self.menu)

    def get_price(self, name):
        name = name.strip().casefold()
        if name in self.menu:
            print(f'{name}: {self.menu[name]} AZN')
        else:
            print("Menyuda olan yemeyi daxil edin")



if __name__ == "__main__":

    restaurant1 = RestaurantMenu()

    while True:
        print("i: Menyunu gor")
        print("+: Mehsul elave et")
        print("-: Mehsul cixar")
        print("s: Qiymeti goster")
        print("x: Çıxış")

        secim = input("Emeliyyati sec: ").casefold()
        if secim == "i":
            restaurant1.show_price()
        elif secim == "+":
            mehsul = input("Mehsulun adini daxil edin: ")
            mebleg = float(input("Qiymeti daxil edin: "))
            restaurant1.add_meal(mehsul, mebleg)
        elif secim == "-":
            mehsul = input("Mehsulun adini daxil edin: ")
            restaurant1.delete_meal(mehsul)
        elif secim == "s":
            mehsul = input("Mehsulun adini daxil edin: ")
            restaurant1.get_price(mehsul)
        elif secim == "x":
            print("Emeliyyat bitdi. Ana sehifeye kecid olunur...")
            break
        else:
            print("Yalnis secim etdiniz, yeniden cehd edin")


    restaurant1.add_meal("dolma", 8)
    restaurant1.add_meal("coban salati", 3.2)
    restaurant1.add_meal("tike kabab", 15)
    restaurant1.show_price()
    restaurant1.get_price("coban salati")
    restaurant1.get_price("pizza")
    restaurant1.delete_meal("coban salati")
    restaurant1.delete_meal("pizza")

