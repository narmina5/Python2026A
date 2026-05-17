"""
----------------------------------------WHILE DÖNGÜSÜ----------------------------------------

i = 10

while i > 2:
    i = i - 1
    print("Hi")

print("End")
"""
"""
sechim = input("+: pul yatirmaq\n-: pul chekmek\n!: konvertasiya\nx: cixis\n")

while sechim != "x":
    if sechim == "+":
        print("Pul yatirildi")
    elif sechim == "-":
        print("Pul chixarildi")
    elif sechim == "!":
        print("Pul deyishdi")
    else:
        print("yanlish sechim, dogru sechimi daxil edin!")
    sechim = input("+: pul yatirmaq\n-: pul chekmek\n!: konvertasiya\nx: cixis\n")
"""
"""
----------------------------------------break, continue, pass----------------------------------------
"""

for reqem in range(500,1001):
    print(reqem)
    if reqem == 7:
        break

print("-----")


for reqem in range(500,1001):
    if reqem % 57:
        continue
    print(reqem)


for reqem in range(1,11):
    if reqem == 7:
        pass
    print(reqem)

"""
----------------------------------------DÖNGÜLƏRDƏ ELSE---------------------------------------

Tək qayda: Loop icində break etdisə (break sətirinə çatdı və işlətdisə), kod else'ə daxil olmayacaq. 
Əks halda, (break kodda yazılmasına baxmayaraq break'i işlətmədisə) else'ə girəcək

BREAK --> NO ELSE
NO BREAK --> ELSE
"""

for reqem in range(1,11):
    print(reqem)
    if reqem == 4:
        break
else:
    print("reqem tapilmadi")