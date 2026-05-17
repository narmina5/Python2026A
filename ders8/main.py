"""
----------------------------------------TUPLE----------------------------------------

    - Dəyişdirilə bilməyən (immutable)
    - Siralı
koordinatlar (x, y, z), doğum tarixi və s.
"""
from dataclasses import asdict

my_list = [1,2,3,4]
my_tuple = (5,1,2,3,4,2,2)

print(my_tuple.index(3))
print(my_tuple.count(2))
print(my_tuple[1])
print(my_tuple[2:5])
print(my_tuple[::-1])

bakinin_koordinati = (40.5324234, 51.5234343)
shahinin_dogum_gunu = (4, 8, 1989)
narminin_dogum_gunu = (22, 6, 2004)

for element in my_tuple:
    print("--", element)


""" 
--------------------------------------------enumerate()-------------------------------------------
"""
my_list2 = ["BMW", "Mercedes", "Ferrari", "Volvo", "Ferrari", "Ferrari"]
print(list(my_list2))
print(list(enumerate(my_list2)))
print("=="*100)
for index, value in enumerate(my_list2):
    if value == "Ferrari":
        print(index)

# print(my_list2.index("Ferrari"))


"""
----------------------------------------LIST COMPREHENSION----------------------------------------

Tək sətirdə list elementləri üzərində əməliyyat (list comprehension)

my_list = [1, 2, 3]
squares = [my_number**2 for my_number in my_list]
print(squares)


klassik metod:

my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    squares.append(my_number**2)
print(squares)
"""
print("==" * 100)

my_list = [1, 2, 3]
squares = []

for my_number in my_list:
    if my_number % 2 == 0:
        squares.append(my_number**2)
    else:
        squares.append(my_number ** 3)
print(squares)

# List comprehension
squares = [my_number ** 2 if my_number % 2 == 0 else my_number ** 3 for my_number in my_list]
squares2 = [my_number ** 2 for my_number in my_list if my_number % 2 == 0]
print(squares)

"""
Tək və ya cütlüyü yoxlayan proqram

my_list = [1, 2, 3, 4, 5, 6]
result = ['Cüt' if my_number % 2 == 0 else 'Tək' for my_number in my_list]
print(result)

klassik metodla:
my_list = [1, 2, 3, 4, 5, 6]
result = []
for my_number in my_list:
    if my_number % 2 == 0:
        result.append("Cüt")
    else:
        result.append("Tək")
print(result)
"""


"""
----------------------------------------NESTED LOOP LIST COMPREHENSION----------------------------------------

Tək sətirdə iç-içə döngüdə list elementləri üzərində əməliyyat (nested loop list comprehension)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in my_list for item in row]
print(flattened)
"""

my_list = [[1, 2, 3, 4, 5], [4, 5, 6, 4], [7, 8, 9]]

flattened = [item for row in my_list for item in row]
print(flattened)

