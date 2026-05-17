"""
----------------------------------------FOR DÖNGÜSÜ--------------------------------------------

for <döngü elementi> in <döngü listi, ardıcıllığı>
    <kod bloku>

# step dəyəri həm də mənfi ədəd ola bilər, lakin yalnız o halda ki, start stop-dan böyükdür.
for i in range(0, 10, 2):  # start, stop, step
    print(i)

start default: 0
stop mütləq təyin olunmalıdır
step default: 1
"""
dogum_tarixleri = [1999, 1989, 2005, 1975, 1950, 2000, 2001]
yashlar = []
"""
for il in dogum_tarixleri:
    print(il)
    print("salam")
print("aaaaaaaaa")
"""
for il in dogum_tarixleri:
    if il % 2 == 0:
        print("salam")
    else:
        print("salam")

print("=" * 100)

reqemler = "0123456789"
for reqem in reqemler:
    print(int(reqem)*2)

print("=" * 100)

for reqem in range(21):
    if reqem % 5 == 0:
        print(reqem)

print("=" * 100)
print(list(range(50)))

my_75lik_list = []
for reqem in range(10001):
    if reqem % 75 == 0:
        my_75lik_list.append(reqem)

print(len(my_75lik_list))


print("=" * 100)

my_75lik_list = []
for reqem in range(5000, 10001):
    if reqem % 75 == 0:
        my_75lik_list.append(reqem)

print(len(my_75lik_list))


print("=" * 100)

my_75lik_list = []
for reqem in range(5000,10001,75):
    my_75lik_list.append(reqem)

print(my_75lik_list)

for reqem in reversed(range(50,91)):
    print(reqem)

print("=" * 100)
for reqem in range(90,40,-1):
    print(reqem)

"""
Listlərdə for döngüsü

my_list = ['a', 'b', 'c', 'd']
for item in my_list:
    print(item)


my_list = [12, 15, 1556, 15, -5.14, 323434, 34344]
for element in my_list:
    print(element)
    if element == 15:
        pass
    print("swaqda")

for element in range(15, 0, -1):
    print(element)

my_str = "Salam"

for char in my_str:
    print(char)
"""


"""
string üçün for döngüsü

my_str = 'hello'
for char in my_str:
    print(char)
"""