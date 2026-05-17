"""
10 ədəd integer elementi olan bir list təyin edin.
    - Listin uzunluğunu çap edin
    - Listi böyükdən kiçiyə sıralayın
    - Ən böyük və kiçik ədədi çap edin
"""

my_list = [2, 5, 7, 9 ,12, 16, 23, 29, 30, 34]
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print(min(my_list))
print(max(my_list))

reqemler = ""