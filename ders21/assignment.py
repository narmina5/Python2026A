"""
OBYEKT YÖNÜMLÜ PROQRAMLAMA (CLASS) İLƏ YAZMAĞA ÇALIŞIN, OLMAZSA NORMAL QAYDADA (FUNKSİYALAR MÜTLƏQDİR!)

Bu tapşırıqda siz istifadəçilərin kontakt məlumatlarını saxlayan, idarə edən və axtarış edə bilən bir Python proqramı hazırlayacaqsınız. Proqram kontaktları faylda saxlayacaq və istifadəçi ilə interaktiv işləyəcək.

Yeni kontakt əlavə et
İstifadəçidən ad, telefon nömrəsi və e-poçt ünvanını daxil etməyi tələb edin.
Bu məlumatları contacts.txt faylına a rejimində əlavə edin.
Hər əlaqə yeni sətirdə saxlanmalıdır:Ad: Elvin, Telefon: +994501234567, E-poçt: elvin@example.com

Bütün kontaktları göstər
contacts.txt faylındakı bütün əlaqələri oxuyub ekrana çıxarın.
Əgər fayl mövcud deyilsə və ya boşdursa, uyğun mesaj göstərin.

Kontakta görə axtarış et
İstifadəçidən bir ad və ya telefon nömrəsi daxil etməsini istəyin.
contacts.txt faylını oxuyaraq uyğun gələn kontaktı tapıb göstərməlidir.
Əgər uyğun kontakt tapılmazsa, mesaj verin:Bu adda kontakt tapılmadı!

Kontaktı sil
İstifadəçidən bir ad daxil etməsini istəyin.
Əgər həmin adla kontakt mövcuddursa, onu fayldan silin.
Əgər əlaqə tapılmazsa, uyğun mesaj göstərin.

İstifadəçi aşağıdakı seçimlərdən birini edə bilər:
1. Yeni kontakt əlavə et
2. Bütün kontaktları göstər
3. Kontakta görə axtarış et
4. Kontaktı sil
5. Çıxış

---------------------------------------------------------------------------
📌
Adı daxil edin: Aysel
Telefon nömrəsini daxil edin: +994501112233
E-poçt ünvanını daxil edin: aysel@example.com
Kontakt uğurla əlavə edildi!


📌
📞 Kontakt Siyahısı:
 1. Ad: Elvin, Telefon: +994501234567, E-poçt: elvin@example.com
 2. Ad: Aysel, Telefon: +994501112233, E-poçt: aysel@example.com


📌
Axtarmaq istədiyiniz ad və ya telefon nömrəsini daxil edin: Aysel
🔍 Tapılan kontakt:
Ad: Aysel, Telefon: +994501112233, E-poçt: aysel@example.com


📌
Silinəcək adı daxil edin: Elvin
✅ Kontakt uğurla silindi!
"""

class ContactManager:
    def __init__(self, filename):
        self.filename = filename

    def add_contacts(self):
        ad = input("Adı daxil edin: ")
        telefon = input("Telefon nömrəsini daxil edin: ")
        e_poct = input("E-poçt ünvanını daxil edin: ")

        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(f'{ad}, {telefon}, {e_poct}\n')

        print("✅ Kontakt uğurla əlavə edildi!")

    def display_contacts(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if not lines:
                    print("Fayl boşdur!")
                else:
                    print("📞 Kontakt Siyahısı: ")
                    for line in lines:
                        print(line.strip())

        except FileNotFoundError:
            print("Fayl tapılmadı!")

    def search_contacts(self):
        search = input("Axtarmaq istədiyiniz ad və ya telefon nömrəsini daxil edin: ").lower()

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if search in line.lower()]
            if lines:
                for line in lines:
                    print(f'🔍 Tapılan kontakt: {line.strip()}')
            else:
                print("Bu adda kontakt tapılmadı!")

        except FileNotFoundError:
            print("Fayl tapılmadı!")


    def delete_contacts(self):
        silinecek_ad = input("Silinəcək adı daxil edin: ").lower()
        found = False
        updated_lines = []

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line in lines:
                if silinecek_ad not in line.lower():
                    updated_lines.append(line)
                else:
                    found = True

            if found:
                with open(self.filename, 'w', encoding='utf-8') as f:
                    f.writelines(updated_lines)
                print("✅ Kontakt uğurla silindi!")
            else:
                print("Bu adda kontakt tapılmadı!")

        except FileNotFoundError:
            print("Fayl tapılmadı!")



if __name__ == "__main__":
    manager = ContactManager("contacts.txt")
    while True:
        print("""
    1. Yeni kontakt əlavə et
    2. Bütün kontaktları göstər
    3. Kontakta görə axtarış et
    4. Kontaktı sil
    5. Çıxış
    """)

        secim = input("Seçiminizi daxil edin: ")

        if secim == "1":
            manager.add_contacts()
        elif secim == "2":
            manager.display_contacts()
        elif secim == "3":
            manager.search_contacts()
        elif secim == "4":
            manager.delete_contacts()
        elif secim == "5":
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim! Zəhmət olmasa 1-5 arası seçim edin.")
