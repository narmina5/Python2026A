"""
----------------------------------------LİSTLƏR----------------------------------------------
Yeni data tip: list()
Dəyər [] əhatə olunur və elemntlər bir birilə , -lə ayrılır.

Məs.:
empty_list = []
my_int_list = [12, 15, 105, 0, -5]
my_str_list = ["salam", "hello", "hallo"]
my_mixed_list = [15, "hello", True]
"""

fibonacci_reqemleri = [1.5, 1, 2.5, 3, 5, 8, 13]
my_boolean_list = [True, False, True, True]
qarisiq_list = ["Alma", 35, True]

# my_list2 = list()
my_list3 = []

"""
Hər hansı elementi onun indeksi ilə əldə edə bilərik. 
Məs.: print(my_mixed_list[1])

Həm də istənilən indeksdəki dəyəri dəyişmək mümkündür.
Məs.: my_str_list[1] = "salam"
"""
my_str = "SalamNecesen"
print(my_str[0])
print(my_str[::])


mashinlar = ["_Mercedes", "BMW", "Ferrari", "Volvo", "a", "b", "c", "BMW"]

print(mashinlar[2])
print(mashinlar[-2:])
print(mashinlar[::-1])


"""
count()
append()
extend()
pop()                   -> __index attribute-u -> pop(3)
sort()                  -> reverse attribute-u -> sort(reverse=True)
"""
print("=" * 100)
print(mashinlar.count("BMW"))
print(mashinlar.pop(2))
print(mashinlar)
print(mashinlar.index("Volvo"))
mashinlar.append("Fiat")
print(mashinlar)
mashinlar.extend(["Porsche", "Jeep", "VW"])
print(mashinlar)
mashinlar.remove("Jeep")

mashinlar_kopyasi = mashinlar.copy()

mashinlar.append("Zaporojie")

print("mashinlar", mashinlar)
print("mashinlarin kopyasi", mashinlar_kopyasi)


"""
0x0000   "SalamNecesen"  -> my_str
0x0008   "Mercedes"   -> mashinlar  , 
0x000f    "BMW"
0x0010     "Ferrari",
0x0018     Zaporojie
0x001f

0x0020    "Mercedes"  mashinlar_kopyasi
..        "BMW"
"""

print(mashinlar[::-1])
# mashinlar.reverse()
print(mashinlar)
mashinlar.sort()
print(mashinlar)
mashinlar.clear()
print(mashinlar)



"""
Pythonda listlər üçün bəzi vacib built-in funksiyalar:
len()
max()
min()
sum()
"""


fibonacci_reqemleri = [1, 1, 2, 3, 5, 8, 13, 21]

print(len(fibonacci_reqemleri))
print(max(fibonacci_reqemleri))
print(min(fibonacci_reqemleri))
print(sum(fibonacci_reqemleri))

