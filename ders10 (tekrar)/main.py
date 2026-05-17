"""Ədədə qədər olan sadə ədədlər probleminin həlli"""
"""
0. sade_ededler bosh listi yarat
1. Her hansi bir eded teyin et (1000)
2. Hemin edede qeder olan butun ededlerin her birini al (uzerinden iterasiya et) - her_bir_eded
3. her_bir_ededin_bolenleri bosh listini yarat
4. 2-den her_bir_eded e qeder butun ededleri gotur (bolen) uzerinde iterasiya et
5. her_bir_eded bolene qaliqsiz bolunurmu
6. bolunurse, her_bir_ededin_bolenleri listin icherisinde saxla
7. (bolen) uzerinde iterasiya bitende - hemin her_bir_ededin_bolenleri list boshdursa demeli her_bir_eded sadedir 
8. her_bir_eded sade_ededler listine elave et
"""
sade_ededler = []
max_limit = 1000
for her_bir_eded in range(2,1001):
    her_bir_ededin_bolenleri = []
    for bolen in range(2, her_bir_eded):
        if her_bir_eded % bolen == 0:
            her_bir_ededin_bolenleri.append(bolen)
    if her_bir_ededin_bolenleri == []:
        sade_ededler.append(her_bir_eded)

print(sade_ededler)
print(len(sade_ededler))


"""Dərslərin ümumi təkrarı, suallar"""

"""Hackerrank"""

"""W3 Schools"""