"""
Fayllarla işləmə

open() funksiyası
    - r (oxumaq, yoxdursa xəta)
    - a (var olan contenti deyishmeden əlave etmək, fayl yoxdursa yarat)
    - w (contenti sifirla ve fayla yaz, fayl yoxdursa yarat)
    - x (yarat, varsa xəta)

    - + (super modu, hem read, hem write)
    - t (tekst modu)
    - b (binary modu)
"""

f = open("reqemler.txt")
print(sum(list(map(int, f.read().strip().split("\n")))))
f.close()

f = open("reqemlerasdasd.txt", "a+")
f.write("45\n1000\n")
my_str_new = f.read()
f.close()

f = open("reqemler_new.txt", "w")
f.write(my_str_new)
f.close()


# f = open("reqemler_python_kursu.txt", "x")

f = open("image.png", "rb")
my_image_str = f.read()
f.close()
print(my_image_str)



"""
read()
readline()
readlines()
write()
close()
"""

f = open("data.txt", "r")
# print(f.read())
print("====" * 50)
print(f.readline())
print(list(map(str.strip, f.readlines())))
bakililar = ""
for student in f.readlines():
    name, age, city = student.strip().split(", ")
    if city == "Bakı":
        bakililar += name + "\n"

f = open("data_bakililar.txt", "w")
f.write(bakililar)
print(bakililar)
f.close()


"""
with:
    with open("data.txt", "r", encoding="utf-8") as file:
"""
with open("data.txt", "r") as file:
    file.read()
    print(bakililar)

print("asd")


"""
import os
os.remove("data2.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("Bele fayl movcud deyil")
    """
"""
import os

if os.path.exists("ders18/data/data2.txt"):
    os.remove("ders18/data/data2.txt")


if not os.path.exists("ders18/data/data4.txt"):
    open("ders18/data/data4.txt", "x")

print("----")
"""

import os
os.remove("reqemler_python_kursu.txt")

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("Bele fayl movcud deyil")