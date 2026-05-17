"""
Tapşırıq: Şirkət İşçi Sistemi (Enkapsulyasiya və Polimorfizm)

Tələblər:

1. 'Isci' (İşçi) adlı əsas sinif yaradın.
   Sinifdə aşağıdakı private (__) atributlar olmalıdır:
       __ad – İşçinin adı
       __vezife – Vəzifəsi (yalnız daxilində təyin olunur)
       __emek_haqqi – Əmək haqqı (birbaşa giriş qadağandır)

   Aşağıdakı metodları yazın:
       __init__(self, ad, emek_haqqi) – Ad və əmək haqqını təyin etsin. Vəzifə subclass tərəfindən verilsin.
       melumat_goster(self) – İşçi haqqında məlumat qaytarsın: Ad, vəzifə, əmək haqqı
       maas_artir(self, faiz) – Əmək haqqını faizlə artırsın
       status(self) – "Ümumi işçi" mesajı qaytarsın

2. Aşağıdakı sinifləri 'Isci' sinifindən törədin:

   a) Mudir sinifi:
       - Əlavə atribut: __departament
       - status() metodunu override edin: "Müdir – şöbə: {departament}"
       - departament_deyis(self, yeni_ad) – şöbəni dəyişmək üçün metod

   b) Muhendis sinifi:
       - Əlavə atribut: __ixtisas
       - status() metodunu override edin: "Mühəndis – ixtisas: {ixtisas}"
       - sertifikat_elave_et(self, sertifikat) – Sertifikat siyahısına yeni sertifikat əlavə etsin

   c) Praktikant sinifi:
       - Əmək haqqı default olaraq 0 olsun
       - status() metodunu override edin: "Praktikant – təcrübə dövründədir"
       - maas_artir() metodunu override edib heç bir dəyişiklik etməsin

3. Aşağıdakı funksiyanı yaradın:
    def statuslari_yoxla(isci_siyahisi):
        # Siyahıdakı bütün işçilərin status() metodunu çağırın

---

Nümunə İstifadə:

mudir = Mudir("Aygün", 5000, "IT")
muhendis = Muhendis("Kamran", 3500, "Elektronika")
praktikant = Praktikant("Rauf")

mudir.maas_artir(10)
muhendis.sertifikat_elave_et("ISO 9001")
praktikant.maas_artir(100)  # Heç bir təsiri olmamalıdır

print(mudir.melumat_goster())       # Ad: Aygün, Vəzifə: Müdir, Əmək haqqı: ...
print(muhendis.melumat_goster())    # Ad: Kamran, Vəzifə: Mühəndis, Əmək haqqı: ...
print(praktikant.melumat_goster())  # Ad: Rauf, Vəzifə: Praktikant, Əmək haqqı: 0

statuslari_yoxla([mudir, muhendis, praktikant])
# Çıxış:
# Müdir – şöbə: IT
# Mühəndis – ixtisas: Elektronika
# Praktikant – təcrübə dövründədir

class Isci:
    def __init__(self, ad, emek_haqqi):
        self.__ad = ad
        self.__vezife = "Umumi isci"
        self.__emek_haqqi = emek_haqqi

    def melumat_goster(self):
        return f"Ad: {self.__ad}\nVezife: {self.__vezife}\nEmek_haqqi: {self.__emek_haqqi}"

    def maas_artir(self, faiz):
        self.__emek_haqqi += self.__emek_haqqi* faiz/100
        return self.__emek_haqqi

    def status(self):
        return "Umumi isci"

class Mudir(Isci):
    def __init__(self, ad, emek_haqqi, department):
        super().__init__(ad, emek_haqqi)
        self.__department = department

    def status(self):
        return f"Müdir – şöbə: {self.__department}"

    def department_deyis(self, yeni_ad):
        self.__department = yeni_ad

class Muhendis(Isci):
    def __init__(self, ad, emek_haqqi, ixtisas):
        super().__init__(ad, emek_haqqi)
        self.__ixtisas = ixtisas
        self.__sertifikatlar = []

    def sertifikat_elave_et(self, sertifikat):
        self.__sertifikatlar.append(sertifikat)

    def status(self):
        return f"Muhendis – ixtisas: {self.__ixtisas}"

class Praktikant(Isci):
    def __init__(self, ad):
        super().__init__(ad, 0)

    def status(self):
        return f"Praktikant – tecrube dovrundedir"

    def maas_artir(self, faiz):
        pass

def statuslari_yoxla(isci_siyahisi):
    for isci in isci_siyahisi:
        print(isci.status())


mudir = Mudir("Nermin", 5000, "IT")
muhendis = Muhendis("Shahin", 3500, "Elektronika")
praktikant = Praktikant("Oguz")

mudir.maas_artir(10)
muhendis.sertifikat_elave_et("ISO 9001")
praktikant.maas_artir(100)  # Heç bir təsiri olmamalıdır

print(mudir.melumat_goster())       # Ad: Aygün, Vəzifə: Müdir, Əmək haqqı: ...
print(muhendis.melumat_goster())    # Ad: Kamran, Vəzifə: Mühəndis, Əmək haqqı: ...
print(praktikant.melumat_goster())  # Ad: Rauf, Vəzifə: Praktikant, Əmək haqqı: 0

statuslari_yoxla([mudir, muhendis, praktikant])
# Çıxış:
# Müdir – şöbə: IT
# Mühəndis – ixtisas: Elektronika
# Praktikant – təcrübə dövründədir

"""

class Isci:
    def __init__(self, ad, emek_haqqi):
        # '_ad' (protected) istifadə edirik ki, alt siniflər buna müraciət edə bilsin
        self._ad = ad
        self._vezife = "Ümumi işçi"
        self._emek_haqqi = emek_haqqi

    def melumat_goster(self):
        return f"Ad: {self._ad}\nVəzifə: {self._vezife}\nƏmək haqqı: {self._emek_haqqi}\n"

    def maas_artir(self, faiz):
        self._emek_haqqi += self._emek_haqqi * faiz / 100
        return self._emek_haqqi

    def status(self):
        return "Ümumi işçi"


class Mudir(Isci):
    def __init__(self, ad, emek_haqqi, department):
        super().__init__(ad, emek_haqqi)
        self._vezife = "Müdir"  # Vəzifəni Mudir sinfi üçün özəlləşdiririk
        self.__department = department

    def status(self):
        return f"Müdir – şöbə: {self.__department}"

    def department_deyis(self, yeni_ad):
        self.__department = yeni_ad


class Muhendis(Isci):
    def __init__(self, ad, emek_haqqi, ixtisas):
        super().__init__(ad, emek_haqqi)
        self._vezife = "Mühəndis" # Vəzifəni Muhendis sinfi üçün özəlləşdiririk
        self.__ixtisas = ixtisas
        self.__sertifikatlar = []

    def sertifikat_elave_et(self, sertifikat):
        self.__sertifikatlar.append(sertifikat)

    def status(self):
        return f"Mühəndis – ixtisas: {self.__ixtisas}"


class Praktikant(Isci):
    def __init__(self, ad):
        super().__init__(ad, 0)
        self._vezife = "Praktikant"

    def status(self):
        return "Praktikant – təcrübə dövründədir"

    def maas_artir(self, faiz):
        # Praktikant üçün maaş artımı funksiyasını pass edirik
        print(f"Sistem: {self._ad} praktikantdır, maaş artımı tətbiq edilmir.")


def statuslari_yoxla(isci_siyahisi):
    print("--- Status Yoxlanışı ---")
    for isci in isci_siyahisi:
        print(isci.status())
    print("------------------------\n")


# --- Nümunə İstifadə ---

# Obyektlərin yaradılması
mudir = Mudir("Nermin", 5000, "IT")
muhendis = Muhendis("Shahin", 3500, "Elektronika")
praktikant = Praktikant("Oguz")

# Əməliyyatlar
mudir.maas_artir(10)
muhendis.sertifikat_elave_et("ISO 9001")
praktikant.maas_artir(100) # Bu heç bir artım etməyəcək

# Məlumatların çapı
print(mudir.melumat_goster())       # Vəzifə: Müdir, Maaş: 5500.0
print(muhendis.melumat_goster())    # Vəzifə: Mühəndis, Maaş: 3500
print(praktikant.melumat_goster())  # Vəzifə: Praktikant, Maaş: 0

# Polimorfizm nümunəsi
statuslari_yoxla([mudir, muhendis, praktikant])