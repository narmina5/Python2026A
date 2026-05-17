"""
İstifadəçidən adını alın.

- Adın bütün hərflərini əksinə düzülmüş şəkildə çap edin. ([::-1] slicing istifadə edin)
- Adın içində neçə dəfə "a" hərfi keçdiyini tapın.
- Adı ilk hərfi böyük formatında (title()) çap edin.
"""

name = input("Ad: ")
print(name[::-1])
print(name.count("a"))
print(name.title())