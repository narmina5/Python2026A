"""
================================================================================
DƏRS 24 — DƏRS01–DƏRS23 ÜMUMİ XÜLASƏ (yalnız başlıqlar + qısa şərhlər)
================================================================================
Qeyd: repoda ders13 qovluğu yoxdur; nömrələmə ders12 → ders14 davam edir.
"""


# ------------------------------- DƏRS01 — print / input / tip çevirmə -------------------------------
# print(), input(), int()/float() — istifadəçi məlumatı və çıxış.
# Əsas nöqtə: input() həmişə str qaytarır; riyazi əməliyyat üçün int/float.
#a = int(input("shahinin nece yasi var?:"))
#print(a*2)

# ------------------------------- DƏRS02 — kommentlər / dəyişənlər / sabitlər -------------------------
# # və """ çoxsətirli komment; snake_case; sabitlər üçün SCREAMING_CASE adət.
# Əsas nöqtə: Python-da "sabit" texniki məcburiyyət deyil — adətə riayət edin.

# koment
"""
koment
"""
# ------------------------------- DƏRS03 — sətirlər (str) / f-string ----------------------------------
# indeks, dilim, upper/lower, split, replace; f"{x}" formatı.
# Əsas nöqtə: str immutable — my_str[0] = "A" işləmir; TypeError.
#b = "shahin qeder yasi var"


#print(f"Shahin {a} qeder yasi var")

#print(b.capitalize())

# ------------------------------- DƏRS04 — müqayisə / məntiq / if-elif-else ---------------------------
# ==, !=, >, <, and, or, not; if/elif/else; iç-içə şərtlər.
# Əsas nöqtə: ":" unutmaq, indentasiya, "if a == 1 or 2" məntiqi səhv (həmişə True).
"""
pul = int(input("Meblegi daxil edin: "))
if pul > 10:
    print("10 man dan cox pulum var")

elif pul>15:
    print("Pulum coxdu")
else:
    print("10 man dan az pulum var")
"""

# ------------------------------- DƏRS05 — list -------------------------------------------------------
# [], indeks, append/extend/pop/remove/sort/copy; dilimlər.
# Əsas nöqtə: sort() in-place; sorted() yeni list; copy() vs eyni obyektə istinad.
"""
my_list = [1, 23,5, 56,8, 79,9]
my_list.append(17)
my_list.remove(23)
my_list.sort()
my_list.pop()
print(my_list)
"""


# ------------------------------- DƏRS06 — for / range -------------------------------------------------
# for element in iterable; range(start, stop, step).
# Əsas nöqtə: range(10) 0..9; stop daxil deyil; mənfi step üçün start > stop.
"""
c = int(input("Reqem daxil edin: "))

for reqem in range(0,11,2):
    print(reqem)

for n in range(0,c,2):
    print(n)

"""


# ------------------------------- DƏRS07 — while / break / continue / pass / else ---------------------
# while şərt; break/continue; loop+else (break olanda else işləmir).
# Əsas nöqtə: while-də şərti yeniləməmək → sonsuz döngü; else-in for/while semantics.
"""
while True:
    yas = input("Yasinizi daxil edin: ")
    if yas == int(yas):
        print(yas)
        break
    else:
        print("Duzgun deyer daxil et")
"""






# ------------------------------- DƏRS08 — tuple / enumerate / list comprehension --------------------
# tuple immutable; enumerate(); [expr for x in data if cond].
# Əsas nöqtə: tək elementli tuple: (1,) — vergül; one-liner if-else sırası: [a if c else b for x in ...].
"""
my_list = [1, 2, 3]
#my_tuple_list =(1, 2, 3)

my_square_list = [n**2 for n in my_list]
print(my_square_list)
"""



# ------------------------------- DƏRS09 — alqoritm / pseudocode --------------------------------------
# addım-addım plan; kod əvvəl düşüncə; sərhəd və hal şərtləri.
# Əsas nöqtə: aralıqın daxil olub-olmaması (5000–10000); və (&) vs və ya (|) şərtləri.



# ------------------------------- DƏRS10 (recap) — təkrar / sadə ədədlər nümunəsi -------------------

# böyük məsələni kiçik addımlara bölmək; iç-içə döngülər.
# Əsas nöqtə: O(n²) həddi; performans və aydın dəyişən adları.


# ------------------------------- DƏRS11 — set --------------------------------------------------------
# unikal element; &, |, -; add/remove/discard; list ↔ set çevrilməsi.
# Əsas nöqtə: {} boş dict yaradır — boş set: set(); remove KeyError, discard yox.
"""
A = {1,2,3,4}
B = {4,5,6}
print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.union(B))
"""





# ------------------------------- DƏRS12 — dict / None ------------------------------------------------
# açar-dəyər; .items/.keys/.values; nested dict; None.
# Əsas nöqtə: mövcud olmayan açar → KeyError; .get() təhlükəsiz; None falsy-dir.


our_students = {
    "9001": {
        "ad": "Shahin",
        "soyad": "Iskenderov",
        "yash": 35,
        "telefon": {
            "country_code": 994,
            "extension": 87952112
        },
        "boy": 185,
        "is_employed": True
    },
    "9002":  {
        "ad": "Narmin",
        "soyad": "Mailova",
        "yash": 22,
        "telefon": "+23423352435",
        "boy": 170
    },
    "9003":  {
        "ad": "Farid",
        "soyad": "Huseynov",
        "telefon": "+23423352435",
        "boy": 174
    },
    "9004":  {
        "ad": "Oghuz",
        "soyad": "Madinali",
        "yash": 26,
        "telefon": "+23423352435",
        "boy": 175
    }
}


"""
print(our_students
["9002"] ["yash"]
)


print(our_students["9003"]["soyad"])
"""


# ------------------------------- DƏRS14 — funksiyalar / return / *args / **kwargs / lambda ------------

# def, parametrlər, default; return; *args, **kwargs; lambda.
# Əsas nöqtə: mutable default (def f(x, L=[]):) təhlükəsi; kwargs açar sözlərdir.
"""
x = 5
my_function = lambda x: x**2
print(my_function(x))
"""

# ------------------------------- DƏRS15 — built-in: map, filter, zip, any, all, sorted --------------
# yüksək səviyyəli iterasiya; all/any qısa şərt yoxlamaları.
# Əsas nöqtə: map obyekti bir dəfə istehlak olunur; iteratorları təkrar oxumaq.
"""

str_ededler = ["0", "2","4","6","7", "8","10"]

int_ededler = list(map(int, str_ededler))
"""



# ------------------------------- DƏRS16 — OOP: class, self, __init__ ---------------------------------
# sinif, atribut, metod; obyekt vəziyyəti.
# Əsas nöqtə: self unudulması; class atributu vs instance atributu qarışması.


# ------------------------------- DƏRS17 — irsilik (inheritance) / super() ---------------------------
# alt sinif; super().__init__(); metodun yenidən yazılması.
# Əsas nöqtə: super() çağırış ardıcıllığı; parent init-in qaçırılması.


# ------------------------------- DƏRS18 — polimorfizm / enkapsulasiya --------------------------------
# eyni interfeys, fərqli davranış; _protected, __name mangling.
# Əsas nöqtə: hasattr(); "private" konvensiyadır; _ClassName__field.


# ------------------------------- DƏRS19 — abstraksiya (ABC / abstractmethod) ------------------------
# şablon sinif; konkret siniflər metodu implement etməlidir.
# Əsas nöqtə: ABC instansiya etmək olmaz; unudulan abstract metod.


# ------------------------------- DƏRS20 — modul / import / pip / venv --------------------------------
# import math, datetime; pip; virtualenv izolyasiyası.
# Əsas nöqtə: qlobal və lokal Python; paket versiyalarının toqquşması.


# ------------------------------- DƏRS21 — fayllar (open / with / encoding) ----------------------------
# r/w/a; read/readline; with open() avtomatik close; utf-8.
# Əsas nöqtə: fayl mövqeyi — read() sonrası boş read; encoding unudulması.


# ------------------------------- DƏRS22 — xəta idarəetməsi (try/except/finally) ----------------------
# spesifik Exception; else/finally; raise.
# Əsas nöqtə: çılpaq except: — debug-u çətinləşdirir; düzgün Exception tipi.


# ------------------------------- DƏRS23 — git əsasları -----------------------------------------------
# status, add, commit, push, pull, branch, merge, .gitignore.
# Əsas nöqtə: böyük fayllar/secrets repoya düşməsin; conflict həlli intizamı.


#git add .
#git commit -m "yeni deyisiklikler"
#git push

"""
Tez-tez ümumi xətalar (bütün kurs üzrə):
    - Tip uyğunsuzluğu (str + int)
    - Off-by-one və range(stop) sərhədləri
    - İdentasiya / blok səhviyyəsi
    - None / boş list / boş dict ilə işləmə
    - Fayl və iteratorları təkrar oxumaq
    - Döngüdə şərti yeniləməmək
"""