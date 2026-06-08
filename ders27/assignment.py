"""
1. Aşağıdakı Python sözlüyünü yaradın:
   student = {
       "name": "Elvin",
       "age": 21,
       "grades": [90, 85, 78],
       "is_enrolled": True,
       "projects": None
   }

2. student obyektini JSON fayla yazın (json.dump) və faylı oxuyub yenidən Python dict olaraq geri alın (json.load).

3. JSON formatına çevrilmiş student obyektini string olaraq da saxlayın (json.dumps) və ekrana çıxarın.

4. Faylı açıb məlumatları oxuyun və tələbənin yaşını ekrana çıxarın.

💡 Bonus: Faylda olmayan açar üçün get metodu ilə default dəyər çıxarın:
   student.get("hobby", "Unknown")
"""
import json
#1
student = {
       "name": "Elvin",
       "age": 21,
       "grades": [90, 85, 78],
       "is_enrolled": True,
       "projects": None
   }

#2
with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    file_data = json.load(file)
    print("Result:", file_data)

#bonus
hobby_status = file_data.get("hobby", "Unknown")
print("Hobby from file:", hobby_status)

#3
my_str = json.dumps(student)
print(my_str)

#4
data = json.loads(my_str)
print(data['age'])
