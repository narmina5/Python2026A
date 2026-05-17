"""
OOP nin 4 əsas prinsipi:

1. Irsilik (inheritance) – Mövcud sinifin xüsusiyyətlərini və metodlarını yeni sinfə ötürmək.
2. Polimorfizm
3. Enkapsulasiya
4. Absktraksiya
"""

class NeqliyyatVasitesi:
    def __init__(self):
        self.marka = ""
        self.model = ""
        self.hazirki_suret = 0
        self.reng = ""
        self.qiymet = 0

    def sureti_artir(self, ferq):
        self.hazirki_suret = self.hazirki_suret + ferq

    def sureti_azalt(self, ferq):
        self.hazirki_suret = self.hazirki_suret - ferq


class Mashin(NeqliyyatVasitesi):
    def siqnal_ver(self):
        print("bipp")

class Velosiped(NeqliyyatVasitesi):
    def siqnal_ver(self):
        print("dringggg")


shahinin_mashini = Mashin()
shahinin_mashini.sureti_artir(50)
shahinin_mashini.sureti_azalt(5)
print(shahinin_mashini.hazirki_suret)
shahinin_mashini.siqnal_ver()

nerminin_velosipedi = Velosiped()
nerminin_velosipedi.siqnal_ver()
print("-----")


class Heyvan:
    def __init__(self, yash, ad, chekisi):
        self.yash = yash
        self.ad = ad
        self.chekisi = chekisi
        self.hazirki_suret = 0

    def yemek_ye(self, kal):
        self.chekisi += kal/100

    def ses_cixar(self):
        print("Umumi ses")


class Pishik(Heyvan):
    def __init__(self, yash, ad, chekisi, bigciqlarinin_uzunlugu):
        super().__init__(yash, ad, chekisi)
        self.bigciqlarinin_uzunlugu = bigciqlarinin_uzunlugu
        self.quyruq_uzunlugu = 0.3
    def qach(self, ferq):
        self.hazirki_suret += ferq
    def ses_cixar(self):
        print("Miyau")
    def tuk_tokmek(self, fesil):
        if fesil == "Payiz":
            print("Tuklerin yarisi getdi")

class Dovshan(Heyvan):
    def hoppan(self, ferq):
        self.hazirki_suret += ferq
    def ses_cixar(self):
        print("Cik-Cik")

class Tutuqushu(Heyvan):
    def uch(self, ferq):
        self.hazirki_suret += ferq
    def ses_chixar(self):
        print("Civ-Civ")


class SiyamPishiyi(Pishik):
    def tuk_tokmek(self, fesil):
        print("Bu tip pishiyin tuku tokulkmur")

    def yat(self):
        print("gozu achigam")


feridin_tarantulasi = Heyvan(2, "Tarro", 0.05)

nerminin_dovshani = Dovshan(4, "Bella", 0.9)

shahinin_tutuqushusu = Tutuqushu(12, "Tuktuk", 0.2)

oguzun_pishiyi = Pishik(5, "Mestan", 3, 0.1)

"""
funksiya overwrite
"""
shahinin_tutuqushusu.ses_chixar()
feridin_tarantulasi.ses_cixar()

"""
inheritance (irsilik)

Parent - child
"""


"""
super() funksiyasi

super() funksiyası parent sinfin metodlarını child sinifdə istifadə etməyə imkan yaradır.
mes.: super().__init__()
"""


"""
İrsiliyin Üstünlükləri
 - Kodun təkrar istifadəsinin qarşısını alır.
 - Miras alınan funksiyalari deyishiklik etmeden istifade ede bilirik
 - Siniflər arasında əlaqəni daha səmərəli idarə etməyə kömək edir.
"""