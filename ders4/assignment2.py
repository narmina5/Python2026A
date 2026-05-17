"""
İstifadəçidən havanın temperaturunu (tam ədəd olaraq) daxil etməsini istəyin.
 Əgər daxil edilən dəyər arasında deyilsə, proqram :
 "Girdiyiniz temperatur dəyəri uyğun deyil. Zəhmət olmasa, -30 ilə 50 arasında dəyər daxil edin."
Əks halda daxil edilən temperatur dəyərinə görə geyim tövsiyəsi verin:

Temperatur Aralığı:

35 – 50:
“Çöldə hava çox istidir! Sərin paltarlar geyin və bol su için.”
25 – 34:
“İsti hava. Yüngül paltarlar geyinmək tövsiyə olunur.”
15 – 24:
“Hava normaldır. Rahat geyinə bilərsiniz.”
5 – 14:
“Hava bir az sərin ola bilər. Yüngül gödəkcə geyinmək yaxşı olar.”
-10 – 4:
“Soyuq havadır. İsinmək üçün qalın geyinməlisiniz.”
-30 – -11:
“Hava dondurucudur! Evdən çıxmaq risklidir, çox isti geyin!”


Göstərilən temperatur aralığında uyğun mesajı çap etdikdən sonra əlavə olaraq bu mesaj da verilsin:
"Sistem tövsiyəsi: Səhiyyə baxımından uyğun geyinmək vacibdir.
"""

temp = int(input("Havanin temperaturu: "))
if not -30 <= temp <= 50:
    print("Girdiyiniz temperatur dəyəri uyğun deyil. Zəhmət olmasa, -30 ilə 50 arasında dəyər daxil edin.")
else:
    if 50 >= temp >= 35:
        print("Çöldə hava çox istidir! Sərin paltarlar geyin və bol su için.")
    elif temp >= 25:
        print("İsti hava. Yüngül paltarlar geyinmək tövsiyə olunur.")
    elif temp >= 15:
        print("Hava normaldır. Rahat geyinə bilərsiniz.")
    elif temp >= 5:
        print("Hava bir az sərin ola bilər. Yüngül gödəkcə geyinmək yaxşı olar.")
    elif temp >= -10:
        print("Soyuq havadır. İsinmək üçün qalın geyinməlisiniz.")
    elif temp >= -30:
        print("Hava dondurucudur! Evdən çıxmaq risklidir, çox isti geyin!")

    print("Sistem tövsiyəsi: Səhiyyə baxımından uyğun geyinmək vacibdir.")
