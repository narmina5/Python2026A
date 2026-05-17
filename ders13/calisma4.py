# =============================================================================
# TAPŞIRIQ 4 — Dərs 8–10: tuple, enumerate, list comprehension, iç-içə döngü
# =============================================================================
"""
"Filmlər siyahısı".

1) Ən azı 5 elementdən ibarət siyahı yaradın: hər element (film_adı, il) tuple olsun,
   məs: ("Inception", 2010).

2) enumerate istifadə edərək hər filmi nömrə ilə çap edin: "1. Inception (2010)".

3) List comprehension ilə yalnız 2010 və ya daha yeni filmlərin adlarının
   siyahısını yaradın və çap edin.
"""

filmler = [
    ("Inception", 2010),
    ("Interstellar", 2014),
    ("Matrix", 1999),
    ("Dune", 2021),
    ("Blade Runner 2049", 2017),
    ("Get Out", 2017),
]


for num, (film, year) in enumerate(filmler, start=1):
    print(f'{num}. {film} ({year})')


yeni_filmler = [tuples[0] for tuples in filmler if tuples[1] >= 2010]
print(yeni_filmler)
