"""
Problem:
Bir şirkətin işçiləri haqqında məlumatlar verilmişdir.

- Hər bir işçinin adı, yaşı və şöbəsini saxlayan bir dictionary list yaradın.
- İstifadəçiyə bir işçinin adını daxil etməyi istəyin və həmin işçinin məlumatlarını ekrana çıxarın.
    - Əgər işçinin adı siyahıda yoxdursa, "Bu adlı işçi tapılmadı." mesajını göstərin.
- Unikal işçi adlarını çap edin

Dict'də ən az 3 işçi olmalıdır.
"""

my_dict = {
    "farid": {
        "yash": 56,
        "sobe": "IT"
    },
    "sahin": {
        "yash": 35,
        "sobe": "Customs"
    },
    "narmin": {
        "yash": 22,
        "sobe": "telebe"
    }
}

axtarilan_ad = input("Ad daxil edin: ")
if axtarilan_ad in my_dict:
    print(my_dict[axtarilan_ad])
else:
    print("Bu adli isci tapilmadi")

"""
OR WITH A LIST:
"""

info = [
    {
        "ad": "farid",
        "yash": 56,
        "sobe": "IT"
    },
    {   "ad": "sahin",
        "yash": 35,
        "sobe": "Customs"
    },
    {
        "ad": "narmin",
        "yash": 22,
        "sobe": "telebe"
    }
]

isci_tapildi = False
axtarilan_ad_2=input("name: ")

for isci in info:
    if isci["ad"] == axtarilan_ad_2:
        print(isci)
        isci_tapildi = True


if not isci_tapildi:
    print("Bu adlı işçi tapılmadı.")
