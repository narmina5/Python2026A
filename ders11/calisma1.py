"""
---------------------------------- TAPŞIRIQ 1: FESTİVAL QRUPLARI ----------------------------------------

Ssenari:
    Şirkət iki paralel təlim təşkil edir: "Python Bootcamp" və "Data Science Workshop".
    İştirakçıların adları set şəklində saxlanılır.

Tapşırıqlar:
    1. İki qrupun birləşməsini tapın. Bütün iştirakçıların siyahısını ekrana çıxarın.
    2. Hər iki qrupa qatılanları çıxarın (kəsişmə).
    3. Yalnız Python təlimində olan, lakin Data Science-ə qatılmayanları göstərin.
    4. Yalnız Data Science-də olan iştirakçıların sayı çoxdursa "Yeni data komandası qur!" mesajını çap edin.
    5. İstifadəçidən ad alaraq həmin şəxsin hansı qruplara aid olduğunu yoxlayın.

Bonus ideyası:
    - İstəsəniz nəticələri lüğət (dictionary) şəklində toplayıb yekun hesabat çap edə bilərsiniz.

İpucu:
    - union(), intersection(), difference(), symmetric_difference() metodlarından istifadə edin.
    - "in" operatoru ilə set üzərində axtarış rahatdır.
"""

PYTHON_BOOTCAMP = {"Aysel", "Murad", "Rashid", "Lalə", "Elvin"}
DATA_SCIENCE_WORKSHOP = {"Murad", "Nihad", "Lalə", "Turan", "Sevinc"}


# 1. Birləşmə
# TODO: butun_istirakchilar adlı dəyişən yaradın və union() ilə hər iki set-i birləşdirin
# print("Bütün iştirakçılar:", butun_istirakchilar)

# 2. Kəsişmə
# TODO: ortaq_istirakchilar adlı dəyişən yaradın və intersection() nəticəsini çap edin

# 3. Yalnız Python qrupu
# TODO: yalnız_python adlı dəyişən yaradın və difference() istifadəsi ilə nəticəni çıxarın

# 4. Yalnız Data Science qrupu
# TODO: yalnız_data adlı dəyişən yaradın
# TODO: yalnız_data set-inin ölçüsü (len) 3-dən böyükdürsə "Yeni data komandası qur!" mesajını print edin

# 5. İstifadəçi sorğusu
# ad = input("Ad daxil edin: ")
# TODO: daxil edilən adın hansı set-lərdə olduğunu yoxlayın və uyğun mesajları çap edin
# Məsələn:
#   - Hər iki qrupdadırsa → "Bu iştirakçı hər iki təlimdədir."
#   - Yalnız birindədirsə uyğun mesaj verin.
#   - Heç birində deyilsə bunu da bildirin.


print(PYTHON_BOOTCAMP.union(DATA_SCIENCE_WORKSHOP))
print(PYTHON_BOOTCAMP.intersection(DATA_SCIENCE_WORKSHOP))
print(PYTHON_BOOTCAMP.difference(DATA_SCIENCE_WORKSHOP))
yalnız_data = DATA_SCIENCE_WORKSHOP.difference(PYTHON_BOOTCAMP)
if len(yalnız_data) > 3:
    print("Yeni data komandasi qur!")

ad = input("Adi daxil edin: ")
if ad in PYTHON_BOOTCAMP.intersection(DATA_SCIENCE_WORKSHOP):
    print("Bu iştirakçı hər iki təlimdədir.")
elif ad in PYTHON_BOOTCAMP.symmetric_difference(DATA_SCIENCE_WORKSHOP):
    print("Yalniz birindedir")
else:
    print("Hec birinde deyil")