# =============================================================================
# TAPŞIRIQ 5 — Dərs 11–12: set, dict, None, unikal dəyərlər
# =============================================================================
"""
"Kurs iştirakçıları".

1) İki siyahı verilmiş kimi fikirləşin: python_qrupu və web_qrupu — adlar təkrar
   oluna bilər.

2) Hər iki qrupun ortaq adlarını (kəsişmə) və yalnız bir qrupda olan adları
   (simmetrik fərq və ya difference — istədiyiniz əməliyyatı izah edin) çap edin.

3) dict istifadə edərək tələbə açarı (məsələn, istifadəçi adı) → məlumat
   alt-lüğəti yaradın: {"yash": int, "kurs": str}. Ən azı 3 tələbə əlavə edin.

4) İstifadəçidən tələbə açarı soruşun. .get() ilə axtarın: yoxdursa None qaytarın
   və "Tapilmadi" mesajı verin; varsa yaş və kursu f-string ilə çap edin.

5) Qısa şərh yazın: hansı struktur (list/set/dict) niyə seçilib (dərs 12-dəki
   müqayisə fikrinə uyğun).
"""

python_qrupu = ["Aysel", "Murad", "Aysel", "Nihad", "Leyla"]
web_qrupu = ["Murad", "Rashid", "Nihad", "Nihad"]

python_qrupu_set = set(python_qrupu)
web_qrupu_set = set(web_qrupu)

print(python_qrupu_set.intersection(web_qrupu_set))
print(python_qrupu_set.symmetric_difference(web_qrupu_set)) #her ikisinde olmayanlar(Nihad ve Murad) cixilir, yerde qalanlar ya python, ya webde dir

kurs_dict = {
    "Nihad": {
        "yash": 21,
        "kurs": ("Python", "Web")
    },
    "Leyla": {
        "yash": 23,
        "kurs": "Python"
    },
    "Aysel": {
        "yash": 22,
        "kurs": "Python"

    },
    "Rashid": {
        "yash": 24,
        "kurs": "Web"
    },
    "Murad": {
        "yash": 26,
        "kurs": ("Python", "Web")
    }
}

telebe = input("Telebe daxil et: ")

if kurs_dict.get(telebe) is None:
    print(f'{None}, Tapilmadi :(')
else:
    print(f'Yas: {kurs_dict[telebe]["yash"]}')
    print(f'Kurs: {kurs_dict[telebe]["kurs"]}')

# List: tekrarlanma olaraq ("kirli" data) telebe adlarini saxlamaq ucun
# Set: tekrarlanmani aradan qaldirib, datani uniqe edirik
# Dict: Bu adlara gore daha detalli melumatlari saxlamaq ucun