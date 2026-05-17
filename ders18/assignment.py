"""
1. İlk olaraq, "Employee" adlı bir əsas sinif yaradın. Bu sinifdə aşağıdakı atributlar və metodlar olmalıdır:
   - `name` (str): İşçinin adı.
   - `salary` (float): İşçinin maaşı.
   - `department` (str): İşçinin işlədiyi departament.
   - `__bonus` (private): İşçinin bonusu, başlanğıcda 0 olaraq təyin olunsun.

   Bu sinifdə aşağıdakı metodlar olmalıdır:
   - `__init__(self, name, salary, department)`: İşçinin adını, maaşını və departamentini təyin edən konstruktor.
   - `get_bonus(self)`: Bonus dəyərini qaytaran metod.
   - `set_bonus(self, amount)`: Bonus dəyərini təyin edən metod.
   - `work(self)`: İşi yerinə yetirən metod (sadəcə çap etsin: "I am working").

2. "Manager" adlı bir alt sinif yaradın ki, bu sinif `Employee` sinifindən irsiyyət alacaq. Bu sinifdə əlavə olaraq:
   - `team_size` (int): İdarə etdiyi komandanın ölçüsü.
   - `work(self)` metodunu dəyişdirərək, manager olduğuna uyğun olaraq "Managing the team" mesajını çap etsin.

3. "Developer" adlı başqa bir alt sinif yaradın ki, bu sinif də `Employee` sinifindən irsiyyət alacaq. Bu sinifdə əlavə olaraq:
   - `programming_language` (str): İstifadə etdiyi proqramlaşdırma dili.
   - `work(self)` metodunu dəyişdirərək, "Coding in Python" mesajını çap etsin.

4. Siniflərdəki metodları test etmək üçün aşağıdakı obyektləri yaradın:
   - Bir `Manager` obyekti: Adı "John", maaşı 5000, departamenti "IT", komanda ölçüsü 10.
   - Bir `Developer` obyekti: Adı "Alice", maaşı 4000, departamenti "IT", proqramlaşdırma dili "Python".
   - Bir `Employee` obyekti: Adı "Eve", maaşı 3500, departamenti "HR".

5. Hər bir obyekt üçün `work()` metodunu çağırın.
6. Bonus dəyərini dəyişdirin (məsələn, `Manager` üçün 1000, `Developer` üçün 500), sonra `get_bonus()` metodunu çağıraraq bonusu əldə edin.
"""

class Employee:
    def __init__(self, name="", salary=0.00, department=""):
        self.name = name
        self.salary = salary
        self.department = department
        self.__bonus = 0

    def get_bonus(self):
        return f"{self.__bonus} $"

    def set_bonus(self, amount):
        self.__bonus = amount

    def work(self):
        print("I'm working")


class Manager(Employee):
    def __init__(self, name, salary, department, team_size=0):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def work(self):
        print("Managing the team")

class Developer(Employee):
    def __init__(self, name, salary, department, programming_language="Python"):
        super().__init__(name, salary, department)
        self.programming_language = programming_language

    def work(self):
        print("Coding in Python")


manager = Manager("John", 5000, "IT", 10)
developer = Developer("Alice", 4000, "IT", "Python")
employee = Employee("Eve", 3500, "HR")
manager.work()
developer.work()
employee.work()
manager.set_bonus(1000)
developer.set_bonus(500)
print(manager.get_bonus())
print(developer.get_bonus())
