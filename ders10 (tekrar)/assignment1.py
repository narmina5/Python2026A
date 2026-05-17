"""
Sezar şifrəsi ən sadə və ən məşhur şifrləmə üsullarından biridir. Bu, hərflərin müəyyən sayda irəli sürüşdürülməsi ilə işləyən əvəzetmə şifrəsidir. Məsələn, 3 (addım) vahid irəli sürüşdürmə ilə 'A' 'D' olur, 'B' 'E' olur və s. Bu prosesi tərsinə çevirərək şifrəli mətni yenidən orijinal formaya qaytarmaq mümkündür.

Tapşırıq:
1. Əlifbanı Python string və ya listi kimi təyin edin. (ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
2. İstifadəçidən bir mətn və bir şifrləmə addımı (rəqəm) daxil etməsini istəyin.
3. Sezar şifrələmə metodunu tətbiq edərək mətnin hərflərini irəli sürüşdürün.
4. Əlifbada olmayan simvolları dəyişmədən saxlayın.
5. Nəticəni ekranda çap edin.

Əlavə olaraq:
Şifrələnmiş teksti deşifrə edin və çap edin.
Sezar şifrəsi haqqında daha ətraflı oxuyun: https://az.wikipedia.org/wiki/Sezar_%C5%9Fifr%C9%99si
"""

"""
1. metnden herfi al
2. hemin herfin indexini elifbadan al
3. hemin indexin uzerine stepi gel -> yeni herfin indexi
4. elifbadan yeni herf indexindeki herfi al ve shifrelenmish stringine elave et
"""


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
METN = input("Metn daxil et: ")
ADDIM = int(input("Reqem daxil et: "))
sifrelenmis = ""


for herf in METN:
    index = ALPHABET.find(herf.upper())
    if index != -1:
        yeni_index = index + ADDIM
        yeni_herf = ALPHABET[yeni_index % len(ALPHABET)]
        sifrelenmis += yeni_herf
    else:
        sifrelenmis += herf

print(sifrelenmis)


desifrelenmis = ""

for herf in sifrelenmis:
    index = ALPHABET.find(herf.upper())
    if index != -1:
        yeni_index = index - ADDIM
        yeni_herf = ALPHABET[yeni_index % len(ALPHABET)]
        desifrelenmis += yeni_herf
    else:
        desifrelenmis += herf

print(desifrelenmis)