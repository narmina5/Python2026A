"""
try
except
else - except-ə daxil olmazsa (exceptsiz else yazila bilmez)
finally - hər halda
"""
a = 5
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("Bolme emeliyyati olmadi, yeqin ki 0 bolendedir")
except TypeError:
    print("Deyerlerden en az birinin data tipi yanlishdir")


"""
while True:
    op = input("ops")

    if op=="x":
        break

    a = int(input("1ci deyer"))
    b = int(input("2ci deyer"))

    if op=="/":
        try:
            print(a/b)
        except:
            print("Bolme emeliyyati olmadi, yeqin ki 0 bolendedir")
    elif op=="*":
        print(a*b)
"""

"""
while True:
    try:
        my_var = input()
        print(5/my_var)
    except:
        print("Bolme mumkun deyil")
"""


"""
ZeroDivisionError - 0 a bölmə
TypeError - tip xətası
ValueError - dəyər xətası
FileNotFoundError - fayl tapılmadı xətası
IndexError - İndeks xətası
KeyError - Dict: acar xetasi
"""

my_list = [1,2,3]
# print(my_list[500])


"""
raise error
"""

a = 20
if a == 20:
    raise ValueError("Deyer 20 qetiyyen olmamalidir!!")