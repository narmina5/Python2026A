"""--------------------------Built-In Python funksiyaları----------------------------"""

"""
len()
enumerate()
any()
all()
map()
filter()
zip()

"""
def mukemmel_eded(n):
    bolenler_list = []
    for bolenler in range(1, n):
        if n % bolenler == 0:
            bolenler_list.append(bolenler)

    if sum(bolenler_list) == n:
        return True
    return False


my_list1 = [True, True, False]
print(len(my_list1))
print(list(enumerate(my_list1)))
print(int(4.567))

print(any(my_list1))
print(all(my_list1))
print("-------")
print(all([mukemmel_eded(reqem) for reqem in range(1, 21)]))

print("-------")

def ikiye_vur(n):
    return n*2

def tekdirmi(n):
    if n%2 == 0:
        return False
    return True
def cutdurmu(n):
    return True if n%2 == 0 else False

str_ededler = ["0", "2","4","6","7", "8","10"]
int_ededler = list(map(int, str_ededler))

ikiye_vurulmush_ededler = list(map(ikiye_vur, int_ededler))
print(ikiye_vurulmush_ededler)

print(list(filter(tekdirmi, int_ededler)))
print(list(filter(cutdurmu, int_ededler)))

print(list(zip([5000,2000,3000], ["BMW", "Mercedes", "Volvo", "Fiat"])))


"""
for i in my_list2:
    my_list_int.append(int(i))
    """



"""
# BUTUN EDEDLERIN CUT OLUB OLMADIGINI YOXLAYAN KOD
cavablar = []
for eded in ededler:
    if eded%2==0:
        cavablar.append(True)
    else:
        cavablar.append(False)
"""
"""
print(all(True if i%2==0 else False for i in ededler))

print(all(not i%2 for i in ededler))

str_ededler = ["0", "2","4","6","7", "8","10"]
inte_chevrilmish_ededler = list(map(int, str_ededler))

print("Filterlənmiş:", list(filter(lambda a:a<5, ededler)))

"""


"""
sum()
max()
min()
sorted()
reversed()
"""
print("===="*50)
print(sum([3,45,6,7]))
print(min([3,45,6,7]))
print(max([3,45,6,7]))
print(sorted([3,45,6,7], reverse=True))
print(list(reversed([3,45,6,7])))




"""
my_sum = 0
for i in my_str:
    my_sum+=i  # 0 + "1"
"""


"""
print("my max", max(my_list))
print("my min", min(my_list))
print("my sum", sum(my_list))
print("my sorted", sorted(my_list))
print("my reversed", list(reversed(my_list)))

sorted_list = sorted(my_list)
"""


"""
type()
isinstance()
id()
"""

print(type(int_ededler))
print(isinstance(int_ededler, list))
print(id(int_ededler))


"""
print("===================")
print(type("Hello"))
print(type(my_list))
print(type(False))

print(isinstance(sorted_list, (bool, str, int)))
"""

"""
print()
input()
"""

"""
int()
float()
str()
bool()
set()
list()
dict()
tuple()
None
"""