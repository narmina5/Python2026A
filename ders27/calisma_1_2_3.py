"""
import random
1-dən 6-ya qədər təsadüfi ədəd çıxaran "dice roll" oyunu yazın.
İpucu: random.randint(1,6) istifadə edin
"""


"""
import random
students = ["Ali", "Aysel", "Murad", "Leyla", "Oghuz"]
Listdən təsadüfi bir tələbə seçin və ekrana çıxarın
İpucu: random.choice(students) istifadə edin
"""


"""
import random
Kompüter 1-10 arası təsadüfi ədəd seçsin
İstifadəçi təxmin etsin
Əgər düz tapdısa -> "Təbriklər!"
Əks halda -> "Yanlış, düzgün cavab {number}"
"""
'''


#1
import random
import json

random_eded = random.randint(1, 6)
print(random_eded)

#2
students = ["Ali", "Aysel", "Murad", "Leyla", "Oghuz"]
print(random.choice(students))

#3
number = random.randint(1, 10)
eded = int(input("Eded daxil et: "))
if eded == number:
    print("Tebrikler!!!")
else:
    print(f'Yanlis, duzgun cavab {number}')
'''
#1
import random
import json
random_num = '''
    {
    "dice_game": {
        "min": 1,
        "max": 6
    }
}
'''
data = json.loads(random_num)

min_number = data['dice_game']['min']
max_number = data['dice_game']['max']
dice = random.randint(min_number, max_number)
print(dice)

#2
random_telebe = '''
    {
    "telebe": {
        "telebeler": ["Nermin", "Shahin", "Ferid", "Icardi", "Oghuz"]
    }
}
'''
melumat = json.loads(random_telebe)

student = melumat['telebe']['telebeler']
get_student = random.choice(student)

print(get_student)


#3
num_to_10 =  '''
    {
    "num": {
        "min": 1,
        "max": 10
    }
}
'''

info = json.loads(num_to_10)

min_num = info['num']['min']
max_num = info['num']['max']
num = random.randint(min_num, max_num)

reqem = int(input("Reqem daxil et: "))
if reqem == num:
    print("Tebrikler!!!")
else:
    print(f'Yanlis, duzgun cavab {num}')