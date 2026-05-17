"""
Polimorfizm

1. Sinif (class) səviyyəsində
2. Funksiya səviyyəsində
"""
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Cat(Animal):
    def __init__(self, breed, name, age, color):
        super().__init__(name, age, color)
        self.breed = breed

    def make_noise(self):
        print("Myauu")

    def increase_age_one_year(self):
        self.age += 10

class Dog(Animal):
    def __init__(self, breed, name, age, color):
        super().__init__(name, age, color)
        self.breed = breed

    def make_noise(self):
        print("Hauu-Hauu")

    def increase_age_one_year(self):
        self.age += 5

heyvanlar = [
    Dog("German Sheperd", "Toplan", 4, "brown"),
    Dog("Pitbull", "Rexx", 4, "gray"),
    Dog("Doberman", "Maxxi", 4, "black"),
    Cat("British", "Mestan", 4, "white"),
    Cat("Swedish", "Kitty", 4, "brown"),
]

for heyvan in heyvanlar:
    heyvan.make_noise()
    heyvan.increase_age_one_year()





"""
hasattr() - obyektin attributeu ve ya methodu oldugunu yoxla
"""
print(hasattr(heyvanlar[0], "jump"))
print("------")




"""
# Obyektlər yaradaq və polimorfizmi test edək
heyvanlar = [It(), Pişik()]

for heyvan in heyvanlar:
    print(heyvan.ses_cixar())  # Eyni metod, fərqli nəticələr
"""


"""
Enkapsulyasiya (qapalılıq)

public
_protected
__private
"""

class Fish:
    def __init__(self, breed, name, age, color):
        self.breed = breed
        self.name = name
        self.__age = age
        self._color = color

    def increase_age_one_year(self):
        self.__age += 5

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

class Trout(Fish):
    def increase_age_one_year(self):
        self._color = "Black"

salmon1 = Fish("Salmon", "tom", 4, "red")
salmon1.set_age(45)
print(salmon1.get_age())
print(salmon1._color)

print(salmon1._Fish__age)







"""
print("-------------------------------")
class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self._color = color     # Protected atribut
        self.__speed = speed   # Private atribut

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

class Sedan(Car):
    def __init__(self, model, color, speed):
        super().__init__(model, color, speed)
        print(self._color)


my_bmw = Sedan("7Serie", "Black", 220)

my_str = "aas"


my_car = Car("Mercedes", "White", 220)
print(my_car.model)
print(my_car._color)   # Çox tövsiyə edilmir (Ancaq mümkündür)
my_car._color = "Black" # Dəyişmək mümkündür, amma qorunan olduğu üçün ehtiyatlı olmaq lazımdır
print(my_car._color)

# print(my_car.__speed)  # Private atributları birbaşa dəyişdirmək və ya birbaşa dəyərlərini almaq mümkün deyil, ancaq sinif daxilindəki metodlarla onları idarə edə bilərik.
print("Getter Speed", my_car.get_speed())
my_car.set_speed(100)
print("Getter Speed After Setter", my_car.get_speed())
print(my_car._Car__speed)  # Amma bu, tövsiyə edilmir! Çünki bu, enkapsulyasiyanı pozur və kodun etibarlılığını azaldır.

"""
"""
Getter və Setter
"""""""
class Car:
    def _set_color_(self, color):
        self.__color = color

    def get_color(self):
        return  self.__color
"""

"""
✅ public – Açıq (standart davranış)
İstənilən yerdən istifadə edilə bilər.
Həm sinifin içindən, həm xaricindən.
Python-da heç bir alt xətt (_) işarəsi yoxdursa, atribut/funksiya public sayılır.
"""

"""
⚠️ _protected – Qismən qapalı
Tək alt xəttlə (_attribute) qeyd olunur.
Bu atribut sinifin içindən və alt siniflərdən (inheritance) istifadə üçün nəzərdə tutulub.
Texniki olaraq tam qadağan etmir, sadəcə "daxili istifadə üçündür" mesajı verir.
"""

"""
⛔ __private – Tam gizli
İki alt xəttlə (__attribute) yazılır.
Bu atribut yalnız sinifin içindən istifadə oluna bilər.
Python atributun adını dəyişdirərək (name mangling) onu gizlədir: __speed → _Car__speed

➡️ Diqqət: Çöldən bu cür müraciət etmək mümkün deyil: car.__engine_status
Amma bu mümkündür (qəbul olunmur, amma mümkündür): car._Car__engine_status
"""