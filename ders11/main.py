"""
----------------------------------------SET-----------------------------------------------
- Unikal (təkrarlanmayan dəyərlər)
- Dəyişdirilə bilən (mutable)
Hesablama əməliyyatları: kəsişmə (&), birləşmə (|), çıxma (-)
"""

A = {1,2,3,4}
B = {4,5,6}
print(A)
print(A.intersection(B))
print(A.union(B))
A.update({2,3,3,3,3,5})
print(A)

print(A.symmetric_difference(B))
C = {4,4,5}
print(C.issubset(B))
A.add(8)
print(A)
print(A.issuperset(B))

print("=" * 100)
X = {1,2,3}
Y = {3,4,5}
print(X.symmetric_difference(Y))
print(X)
print(Y.difference(X))



"""
----------------------------------SET FUNKSIYALARI----------------------------------------
METOD / FUNKSIYA	            AÇIQLAMA  

add()	                        Set-ə yeni element əlavə edir  
clear()	                        Set-in bütün elementlərini silir  
copy()	                        Set-in surətini çıxarır  
difference()	                İki və ya daha çox set arasındakı fərqi qaytarır  
difference_update()	            Fərqi hesablayır və ilkin set-i yeniləyir  
discard()	                    Verilmiş elementi set-dən silir (əgər varsa)  
intersection()	                İki və ya daha çox set arasında ortaq elementləri qaytarır  
intersection_update()	        Ortaq elementləri hesablayır və ilkin set-i yeniləyir  
isdisjoint()	                İki set-in ortaq elementi olub-olmadığını yoxlayır  
issubset()	                    Bir set-in digərinin alt toplusu olub-olmadığını yoxlayır  
issuperset()	                Bir set-in digərini tam əhatə edib-etmədiyini yoxlayır  
pop()	                        Set-dən təsadüfi bir elementi çıxarır  
remove()	                    Verilmiş elementi set-dən silir (əgər yoxdursa, səhv verir)  
symmetric_difference()	        İki set arasında yalnız birində olan elementləri qaytarır  
symmetric_difference_update()	Simetrik fərqi hesablayır və ilkin set-i yeniləyir  
union()	                        İki və ya daha çox set-in birləşməsini qaytarır  
update()	                    Digər set-in elementlərini mövcud set-ə əlavə edir  
"""



"""
----------------------------------SET YARATMA VƏ ƏSAS XÜSUSİYYƏTLƏR----------------------------------------
- Set-lər {} ilə və ya set() funksiyası ilə yaradılır.
- Elementlər unikal saxlanılır, təkrarlanan dəyərlər avtomatik silinir.
- Sıra (order) qorunmur, ona görə nəticədə elementlər qarışıq görünə bilər.

Nümunələr:
    meyveler = {"alma", "armud", "alma"}
    print(meyveler)  # {'alma', 'armud'}

    bos_set = set()          # boş set yaratmaq üçün
    qarisiq = set("python")  # {'n', 't', 'p', 'y', 'h', 'o'}

    # Set-ə element əlavə etmək
    meyveler.add("banan")
    print("banan" in meyveler)  # True
"""
print("=" * 100)
my_set = set("Salam")
print(my_set)


"""
----------------------------------SET VƏ DİGƏR MƏLUMAT TİPLƏRİ ARASINDA ÇEVİRİŞ----------------------------------------
- list → set : Siyahını unikal elementlərə endirmək üçün.
- tuple → set : Dəyişməz toplusu dəyişdirilə bilən set-ə çevirmək üçün.
- set → list : Unikal dəyərləri yenidən siyahıya salmaq üçün.

Nümunələr:
    telebeler_list = ["Aysel", "Murad", "Aysel", "Rashid"]
    telebeler_set = set(telebeler_list)  # {'Aysel', 'Murad', 'Rashid'}

    reqemler = {1, 2, 3}
    reqemler_list = list(reqemler)       # [1, 2, 3] (sıra fərqli ola bilər)
"""

telebeler_list = ["Aysel", "Murad", "Aysel", "Rashid"]
telebeler_set = set(telebeler_list)  # {'Aysel', 'Murad', 'Rashid'}

"""
----------------------------------SET ƏMƏLİYYATLARI----------------------------------------
Union (birləşmə):
    python_qrupu = {"Aysel", "Murad"}
    data_qrupu = {"Murad", "Nihad"}
    print(python_qrupu.union(data_qrupu))  # {'Aysel', 'Murad', 'Nihad'}

Intersection (kəsişmə):
    ortaq = python_qrupu.intersection(data_qrupu)  # {'Murad'}

Difference (fərq):
    yalnız_python = python_qrupu.difference(data_qrupu)  # {'Aysel'}

Symmetric Difference (simetrik fərq):
    print(python_qrupu.symmetric_difference(data_qrupu))  # {'Aysel', 'Nihad'}
"""


"""
----------------------------------SET ÜZƏRİNDƏ DÖNGÜ VƏ ŞƏRTLƏR----------------------------------------
- for döngüsü ilə hər elementi ayrı yoxlayırıq.
- if şərtləri ilə xüsusi elementləri tapırıq.

Nümunə:
    telebeler = {"Aysel", "Murad", "Nihad"}

    for telebe in telebeler:
        if telebe.startswith("N"):
            print(f"N ilə başlayan: {telebe}")
"""


"""
----------------------------------SET COMPREHENSION----------------------------------------
- Qısa sintaksis ilə yeni set yaratmaq imkanı verir.
- Şərt daxil etmək mümkündür.

Nümunələr:
    kvadratlar = {eded ** 2 for eded in range(1, 6)}  # {1, 4, 9, 16, 25}
    cutler = {eded for eded in range(20) if eded % 2 == 0}  # {0, 2, 4, ...}
"""



"""
----------------------------------SET VƏ FROZENSET----------------------------------------
- set → mutable (dəyişən)
- frozenset → immutable (dəyişməz), element əlavə/silmək mümkün deyil.

Nümunə:
    immutable_qrup = frozenset({"A", "B", "C"})
    # immutable_qrup.add("D")  # AttributeError

Frozenset daha çox dictionary açarı kimi istifadə olunur, çünki hash-lənə bilir.
"""

AA = frozenset({1,2,3,4})