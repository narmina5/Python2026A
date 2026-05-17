# =============================================================================
# TAPŞIRIQ 1 — Dərs 1–3: giriş/çıxış, ədədlər, sətir və f-string
# =============================================================================
"""
"Kitabxana borcu" mini-proqramı yazın.

1) İstifadəçidən kitabın adını (mətn), günlük gecikmə haqqını (float və ya int)
   və gecikdiyi gün sayını soruşun. Adı input ilə götürüb .strip() ilə boşluqları
   təmizləyin; məbləği və günü uyğun tipə çevirin.

2) Cəmi gecikmə məbləğini hesablayın: günlük_haqq * gun_sayi

3) nəticəni f-string ilə çap edin; kitab adı .title() ilə göstərilsin.
   Məsələn: "Kitab: 'Python Esaslari', umumi gecikme: 12.50 AZN"

"""

kitab = input("Kitabin adi: ").strip()
gecikme_haqqi = float(input("Gunluk gecikme haqqi: "))
gecikdiyi_gun = int(input("Gecikme gunu: "))

umumi_gecikme = gecikme_haqqi * gecikdiyi_gun

print(f'{kitab.title()}, {umumi_gecikme}')