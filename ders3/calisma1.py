"""
İstifadəçidən sadəcə adını alın. String metodları, əməliyyatları edərək:

1- Adının ilk hərfini böyük hərf edin, capitalize() funksiyası ilə. Alınan dəyəri eyni dəyişkəndə tutun.
2. Adının ilk 2 hərfini çap edin
3. Adının son hərfini çap edin
"""

name = input("Adiniz: ")
print(name.capitalize())
print(name[0:2])
print(name[-1])