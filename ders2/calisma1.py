"""
Almaniyada insanları təkrar emal etməyə təşviq etmək üçün içki qablarına kiçik bir depozit əlavə olunur (Refund).

Şüşə içki qabları üçün 0,08 avro;
Plastik içki qabları üçün isə 0,25 avro depozit var.

Elə proqram yazın ki:
    - İstifadəçidən hər tipdə qabların sayını alsın
    - Həmin qabların qaytarılması üçün alınacaq pulu hesablayıb istfadəçiyə göstərsin.
    - Çıxışı elə formatlayın ki, avro işarəsi əlavə edilsin və məbləğdə həmişə iki onluq yer göstərilsin.

Məsələn:
Şüşə qabların sayı: ...
Plastik qabların sayı: ...

Cəmi qaytarılacaq məbləğ - 2.25 €
"""

suse = 0.08
plast = 0.25
s = int(input("Suse qab sayi: "))
p = int(input("Plastik qab sayi: "))
refund = s*suse + p*plast
print(refund, "€")