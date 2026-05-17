"""
Tapşırıq:
Sizə tələbə adlarının və onların ballarının olduğu siyahı verilir. Sizdən tələb olunur:

1- enumerate() istifadə edərək: Hər tələbənin adını, balını və siyahıdakı mövqeyini (1-dən başlayaraq) çap edin
- hər tələbə məlumatı 1 sətirdə

2- Siyahı anlayışı (List Comprehension) istifadə edərək: Yalnız 50 və ya daha çox bal toplayan
tələbələrin adlarını və ballarını çap edin.

3- Bütün tələbələrin orta balını hesablayın.

4- Ən çox bal yığan tələbənin adını, balını və list indeksini göstərin (0-dan başlayaraq).
"""

students = ["Farid", "İlkin.C", "Oghuz", "İlkin.M", "Aydan", "Nadirshah", "Rakif", "Umid", "Ravan", "Huseyn"]
notes = [30, 85, 82, 93, 85, 35, 27, 80, 90, 86]

for index, student in enumerate(students):
    print(student, notes[index], index)

print("==" * 100)

passed_student = [(students[index], notes[index]) for index in range(len(students)) if notes[index] >= 50]
print(passed_student)

print("==" * 100)

print(sum(notes)/len(notes))

print("==" * 100)

max_score = max(notes)
index = notes.index(max_score)

print(max_score)
print(students[index])
print(index)