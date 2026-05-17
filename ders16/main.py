"""
class
"""

class Mashin:
    buraxilis_ili = 2000
    rengi = "sari"
    motor_hecmi = 2.5  # L
    hazirki_suret = 0

    def sureti_artir(self, ferq):
        self.hazirki_suret = self.hazirki_suret + ferq

    def sureti_azalt(self, ferq):
        self.hazirki_suret -= ferq


shahinin_mashini = Mashin()
nerminin_mashini = Mashin()
oguzun_mashini = Mashin()

shahinin_mashini.buraxilis_ili = 2020
shahinin_mashini.rengi = "qara"

print(shahinin_mashini.buraxilis_ili)
print(shahinin_mashini.rengi)
print(shahinin_mashini.hazirki_suret)

shahinin_mashini.sureti_artir(180)
shahinin_mashini.sureti_azalt(30)
shahinin_mashini.sureti_artir(5)
shahinin_mashini.sureti_azalt(40)

print(shahinin_mashini.hazirki_suret)
print(oguzun_mashini.hazirki_suret)


"""
snake_case - deyishkenler, funksiyalar, fayl_adlari (modullar)
kebap-case
camelCaseWord  
PascalCase / CapitalCamelCase - classlar
SCREAMING_CASE - sabitler
"""

"""
attributelar - deyishkenler
"""


"""
self
"""


"""
methodlar - funksiyalar
"""


"""
__init__ funksiyası
"""

class Car:
    def __init__(self, year, color, engine, curr_speed=0):
        self.year = year
        self.color = color
        self.engine = engine
        self.curr_speed = curr_speed

    def accelerate(self, diff):
        self.curr_speed = self.curr_speed + diff

    def decelerate(self, diff):
        self.curr_speed -= diff


class BankAccount:
    def __init__(self, hesab_no, username, password, balance):
        self.hesab_no = ""
        self.username = ""
        self.password = ""
        self.balance = 0

    def balansi_artir(self, amount):
        self.balance = self.balance + amount

if __name__ == "__main__":
    shahins_car = Car(2025, "black", 2.5)
    shahins_car.accelerate(50)
    print("-----")
    my_list = [1,2,3,4]