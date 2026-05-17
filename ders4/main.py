"""
--------------------------------MÜQAYİSƏ OPERATORLARI-----------------------------------
Şərt ifadələrində müqayisə operatorlarından istifadə olunur:
`==`, `!=`, `>`, `<`, `>=`, `<=`
"""
a = 5
b = 7

print(a != b)
my_str = "salam"
my_str2 = "salam"

print(my_str != "")



"""
---------------------------------MƏNTİQİ OPERATORLAR------------------------------------
and, or, not
"""
print(a > 8 and not b > 10)



"""---------------------------------ŞƏRT BLOKLARI--------------------------------------"""

"""
if şərt bloku
"""
print("=" * 100)
if a > 6 and not b > 10:
    print("salam")
    print("necesen")

    if my_str == "salam":
        print("2ci defe salam")

print("Sagol!")


"""
else bloku
"""
print("==============")
a = 15
if a < 10:
    print("10-dan kichik")
else:
    print("10-dan boyuk")


a = 28
print("=" * 100)
if a > 100:
    print("100 den boyuk")
elif a > 10:
    print("50 den boyuk, 100den kichik")
    if a > 20:
        print("20den boyuk, 50den kichik")
        if a == 28:
            print("a 28dir")
else:
    print("20den kichik")

"""
elif 
"""


"""
iç içə if,else
"""


"""
Tez-tez edilən xətalar:
    - : unutmaq
    - İndentasiya
    - Məntiqi xətalar: and, or birləşmələri
"""