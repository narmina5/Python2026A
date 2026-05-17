"""
Heyvan adlı əsas sinif yaradın (parent class):

ad, yaş, cins (dişi, erkək) atributunu təyin edin.

ses_cixar() adlı metod yaradın və bu metod "Bu heyvan səs çıxarır" mesajını qaytarmalıdır.


İki fərqli törəmə sinif (child classes) yaradın:

İt adlı sinif yaradın və ses_cixar() metodunu “Hav-hav!” qaytaracaq şəkildə yenidən yazın.
Pişik adlı sinif yaradın və ses_cixar() metodunu “Miyov-miyov!” qaytaracaq şəkildə yenidən yazın.

Test edin:
It və Pişik siniflərindən bir neçə obyekt yaradın və onların ses_cixar() metodunu çağıraraq fərqi göstərin.
 🐶 😺
"""

class Heyvan:
    def __init__(self, ad, yas, cins):
        self.ad = ad
        self.yas = yas
        self.cins = cins

    def ses_cixar(self):
        return "Ses cixarir"

class It(Heyvan):
    def __init__(self, ad, yas, cins, sumuk_sayi):
        super().__init__(ad, yas, cins)
        self.sumuk_sayi = sumuk_sayi

    def sumuk_ye(self, sumuk_sayi):
        return f'Yediyi sumuk sayi: {sumuk_sayi}'

    def ses_cixar(self):
        return "Hav-hav!"

class Pisik(Heyvan):
    def __init__(self, ad, yas, cins, big_uzunlugu):
        super().__init__(ad, yas, cins)
        self.big_uzunlugu = big_uzunlugu

    def ses_cixar(self):
        return "Miyav-miyav!"

nerminin_pisiyi = Pisik("Mestan", 1, "disi", 0.2)
nerminin_iti = It("doggy", 2, "erkek", 3)

print(nerminin_iti.ses_cixar())
print(nerminin_pisiyi.ses_cixar())
print(nerminin_iti.sumuk_ye(4))

"""
Əlavə:

It classi uchun indiye qeder yediyi sumuk_sayi attributunu tut
It class uchun sumuk_ye(sumuk_sayi) funksiyasi yarat

Pishik classi uchun big_uzunlugu attribute tut
"""

