"""
---------------------------------- TAPŞIRIQ 2: KİTABXANA INVENTARI ----------------------------------------

Ssenari:
    LocalKitabxana fiziki və rəqəmsal kitab fondunu set-lərdə saxlayır.
    Kitabların adları təkrarlanmadan izlənildiyi üçün set strukturu ideal seçimdir.

Başlanğıc məlumatları:
    fiziki_kitablar = {"Python 101", "Data Vizualizasiya", "Algoritmlərə giriş", "Rəqəmsal Marketinq"}
    ebooklar = {"Algoritmlərə giriş", "Maşın Öyrənməsi", "Python 101", "Bulud Texnologiyaları"}

Tapşırıqlar:
    1. Yeni gələn kitabları fiziki fonda əlavə edin:
        yeni_gelenler = {"Süni İntellektə giriş", "Rəqəmsal Marketinq"}
    2. Eyni adlı kitabların həm fiziki, həm də e-book variantlarının mövcudluğunu yoxlayın.
       (Hər iki set-də olanları "iki formatda mövcuddur" mesajı ilə göstərin.)
    3. Yalnız e-book formatında olan kitabların siyahısını yaradın və çap edin.
    4. Set comprehension istifadə edərək adı "Python" ilə başlayan kitabların ayrıca set-ni qurun.
    5. İstifadəçinin daxil etdiyi kitabın hansı formatda olduğunu bildirin.
    6. Fiziki fond ebooklar-ın alt toplusudursa əlavə mesaj çap edin, əks halda fərqləri göstərin.

"""

FIZIKI_KITABLAR = {"Python 101", "Data Vizualizasiya", "Algoritmlərə giriş", "Rəqəmsal Marketinq"}
EBOOKLAR = {"Algoritmlərə giriş", "Maşın Öyrənməsi", "Python 101", "Bulud Texnologiyaları"}
YENI_GELENLER = {"Süni İntellektə giriş", "Rəqəmsal Marketinq"}


# 1. Yeni gələn kitablar
# TODO: yeni_gelenler set-indəki kitabları FIZIKI_KITABLAR set-inə əlavə edin
# print("Yenilənmiş fiziki fond:", FIZIKI_KITABLAR)
FIZIKI_KITABLAR.update(YENI_GELENLER)
print("Yenilənmiş fiziki fond:", FIZIKI_KITABLAR)

# 2. Hər iki formatda olan kitablar
# TODO: iki_formatda adlı set yaradın və intersection() nəticəsini çap edin
# for kitab in iki_formatda:
#     print(f"{kitab} - iki formatda mövcuddur")
IKI_FORMATDA = FIZIKI_KITABLAR.intersection(EBOOKLAR)
for kitab in IKI_FORMATDA:
    print(f'{kitab}')

# 3. Yalnız e-book
# TODO: yalnız_ebook adlı set yaradın və difference() ilə tapın
# print("Yalnız e-book formatında olanlar:", yalnız_ebook)
yalniz_ebook = EBOOKLAR.difference(FIZIKI_KITABLAR)
print(yalniz_ebook)

# 4. "Python" ilə başlayan kitablar
# TODO: python_kitablar adlı set comprehension yazın
# print("Python ilə başlayanlar:", python_kitablar)
python_kitablar = {kitab for kitab in FIZIKI_KITABLAR.union(EBOOKLAR)}
print("Python ilə başlayanlar:", python_kitablar)

# 5. İstifadəçi sorğusu
# kitab_ad = input("Kitab adını daxil edin: ")
# TODO: daxil edilən adın fiziki, ebook və ya hər iki set-də olub-olmadığını yoxlayın
# Məsələn:
#   - Hər ikisindədirsə → "Bu kitab hər iki formatda mövcuddur!"
#   - Yalnız birindədirsə uyğun mesaj verin.
#   - Heç birində deyilsə bunu bildirin.
kitab_ad = input("Kitab daxil edin: ")
yalniz_birinde = FIZIKI_KITABLAR.symmetric_difference(EBOOKLAR)
if kitab_ad in IKI_FORMATDA:
    print("Bu kitab hər iki formatda mövcuddur!")
elif kitab_ad in yalniz_birinde:
    print("Her ikisinde deyil")
else:
    print()


# 6. Alt toplusu yoxlaması
# TODO: FIZIKI_KITABLAR set-i EBOOKLAR set-inin alt toplusudurmu?
if FIZIKI_KITABLAR.issubset(EBOOKLAR):
    print("Fiziki fond digital fondun alt toplusudur.")
else:
    print(FIZIKI_KITABLAR.difference(EBOOKLAR))
#     # TODO: fərqləri (difference) hesablayın və çap edin