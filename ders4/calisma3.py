"""
Valyuta Çevirici

İstifadəçidən valyutanı seçməsini istəyin (məsələn, USD, EUR, TRY).
Müvafiq məzənnəni göstərərək AZN-ə çevirin (kursları əvvəlcədən təyin edin).

Qeyd:
    1 USD = 1.70 AZN
    1 EUR = 1.95 AZN
    1 TRY = 0.04 AZN
"""

val = input("Valyutani sec: ").upper()
mebleg = float(input("Meblegi daxil edin: "))
if val == "USD":
    print(mebleg*1.70, "AZN")
elif val == "EUR":
    print(mebleg*1.95, "AZN")
elif val == "TRY":
    print(mebleg*0.04, "AZN")
else:
    print("Yalniz USD, EUR, TRY ceviririk :D")
