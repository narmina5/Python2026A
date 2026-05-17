"""
Sizə bir tam ədədlər siyahısı verilir: numbers = [13, 2, 36, 42, 5, 64, 7, 48, 9, 10]
Sizdən tələb olunur:

1. enumerate() istifadə edərək: Ən böyük ədədin indeksini və dəyərini çap edin.
2. Siyahı anlayışı (list comprehension) istifadə edərək: Yalnız cüt ədədlər olan yeni bir siyahı yaradın və çap edin.
3. Siyahıdakı bütün ədədlərin cəmini hesablayın.
"""

numbers = [13, 2, 36, 42, 5, 64, 7, 48, 9, 10]

for index, value in enumerate(numbers):
    value = max(numbers)
    index = numbers.index(value)

print(f'index: {index}, value: {value}')


cut = [number for number in numbers if number % 2 == 0 ]
print(f'Cut ededler: {cut}')


print(sum(numbers))