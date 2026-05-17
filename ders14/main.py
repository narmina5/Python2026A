"""
-----------------------------------FUNKSİYALAR------------------------------------
def açar sözü
"""
"""
f(x) = x + 1
f(5) = 5 + 1 = 6

f(x,y) = x**2 + y**2

f(x, y:str) = x + len(y)
f(5, "salam") = 5 + len("salam") = 10

"""
def f(x):
    return x+1

y = f(7)
print(y)
print("------")

def uc_reqemi_topla(a,b,c):
    cem = a+b+c
    return cem

def butun_riyazi_emeller(a,b):
    return a+b, a-b, a*b, a/b

cem, ferq, hasil, qismet = butun_riyazi_emeller(15,3)
print(ferq)

def uc_dilde_salamla():
    print("Hello")
    print("Salam")
    print("Hallo")

"""
return açar sözü
çoxsaylı return dəyəri
"""


"""
Parametrlər
Defolt dəyər
"""

print("--"*50)

def toplama(a,b,c=0):
    print(a+b+c)

toplama(5,4)

print("--"*50)

def hasil2(a:int,b:int=5) -> int:
    return a*b




"""
*args - tuple kimi davranış
**kwargs - dict kimi davranış
"""


"""-----------------------args - bir ulduz - tuple kimi davranir-------------------------"""


"""----------------------kwargs - iki ulduz - dict kimi davranir------------------------"""


"""
main funksiyası
"""
def yari_toplama(a, *menim_arq):
    cem = 0
    for reqem in menim_arq:
        cem += reqem / 2
    return cem + a

def yari_toplama(a, **menim_arq):
    print(menim_arq)

if __name__=='__main__':
    print(yari_toplama(5, yash=15, email="hferid", adres="Baku"))

"""----------------------lambda funksiyaları (ananonim funksiyalar)--------------------------"""
"""
my_func = lambda b,c: b*c
my_func(1, 2)
"""
my_func = lambda x: x+1
my_func(7)



"""
global dəyişkənlər
"""
print("----")

x = 10

def my_function():
    print(x)

my_function()
print(x)