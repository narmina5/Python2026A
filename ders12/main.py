"""
-----------------------------------------DICT-----------------------------------------------
- Çox geniş istifadə yerləri
- Böyük datalarda sürətli proses (açarlarla indeks)
- Dəyişdirilə bilən (mutable)
"""

my_dict = {
    "A": 1,
    "B": [1,2,3],
    "C": True
}

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
        "yash": 27,
        "telefon": "+23423352435",
        "boy": 175
    }
}
"""
print(our_students["Shahin"]["yash"])
print(our_students["Narmin"]["yash"])
print(our_students["Farid"]["yash"])
print(our_students["Oghuz"]["yash"])
"""
# print(our_students.items())

for acar, deyer in our_students.items():
    if "yash" in deyer:
        print(f'{acar}: {deyer["yash"]}')

for acar in our_students.keys():
    print(acar)

for deyer in our_students.values():
    print(deyer)

# our_students["Rajab"] = {"yash": 22}
our_students.update(
    {
        "Rajab": {
            "soyad": "Mailova",
            "yash": 22,
            "telefon": "+23423352435",
            "boy": 170
        }
    }
)
print("===" * 30)

our_students["9002"]["email"] = "narmin@gmail.com"
print(our_students)

"""
---------------------------------------None data tipi-------------------------------------------
"""

a = 15
a = "Salam"
a = None



"""
Hansı vəziyyətlərdə hansını seçməliyik?

Tuple:
    Məlumatlar dəyişməz olmalı və sırası önəmli olduğu zaman. 
    Məsələn, koordinatlar, tarixlər, funksiya nəticələrinin qruplaşdırılması.
Set: 
    Təkrarlanmayan unikal elementlərin saxlanılması və ya hesablama əməliyyatlarının edilməsi lazım olduqda. 
    Məsələn, unikal qiymətlər, verilənlər üzərində kəsişmə əməliyyatı.
Dictionary: 
    Açar-dəyər cütləri ilə verilənlərin saxlanılması və tez bir şəkildə verilənlərə daxil olmaq lazım olduğunda. 
    Məsələn, istifadəçi məlumatları, məhsul kataloqu.
NoneType: 
    Heç bir dəyər göstərilmədikdə və ya funksiyaların heç bir nəticə qaytarmadığı zaman istifadə olunur. 
    Məsələn, funksiyaların geri dönüş növü yoxdur və ya başlanğıc dəyər olaraq None təyin edilir.
"""


"""
indiyə qədər öyrəndiyimiz data tipləri:

int
float
str
bool
list
+
set (frozenset)
tuple
dict
None
"""

"""
Mutable (dəyişdirilə bilən), Immutable (dəyişdirilə bilməyən) Data tipləri

Mutable:
    - list
    - dict
    - set

Immutable:
    - int
    - float
    - str
    - bool
    - tuple

Dict'lərin keyləri mütləq immutable olmalıdır!
"""

