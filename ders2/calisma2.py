"""
İstifadəçidən r radiusu oxumaqla başlayan proqram yazın.
Proqramınız radiusu r olan
    - dairənin sahəsini (πr^2)
    - kürənin həcmini (4/3 πr^3) hesablasın, tapılan dəyəri və həcm dəyişkənin data tipini terminalda göstərsin.


Hesablamalarınızda pi-ni sabit kimi tanımlayın və dəyərini 3.14 olaraq verin.
Çalışın kodunuzu kommentlərlə izah edin - çox qısa şəkildə.
"""

PI = 3.14
r = int(input("radius: "))
s = PI*(r**2)
h = 4/3*PI*(r**3)
print(s, type(s), h, type(h))

