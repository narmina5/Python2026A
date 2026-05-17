"""
BankAccount adlı sinif yaradın və aşağıdakı atributları və metodları daxil edin:
owner (string), balance (float)
deposit(amount) – Müəyyən edilmiş məbləği balansın üzərinə əlavə edir.
withdraw(amount) – Müəyyən edilmiş məbləği balansdan çıxarır (balansın kifayət etməsini yoxlayın).
get_balance() – Cari balansı qaytarır.
BankAccount sinifindən irsiyyət alaraq SavingsAccount adlı sinif yaradın və əlavə edin:
interest_rate (float, məsələn, 0.05, yəni 5% faiz)
apply_interest() – Balans üzərinə faizi tətbiq edir (faiz, balansın interest_rate ilə vurulmasıyla hesablanır).

Kiçik bir proqram yazın ki:
Bir BankAccount instansı və bir SavingsAccount instansı yaratsın.
Hər iki hesaba məbləğ depozit və çıxarış etsin.
Yığım hesabına faiz tətbiq etsin və yenilənmiş balansı göstərin.
Məs.:Bank hesabının balansı: 500
Yığım hesabının faizə qədər balansı: 1000
Yığım hesabının faizdən sonra balansı: 1050
"""

class BankAccount:
    def __init__(self, owner = '', balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} AZN balansa yatirildi")
        else:
            print("Yatirilan mebleg sifirdan boyuk olmalidir")

    def withdraw(self, amount):
        if amount <= 0:
            print("Yatirilan mebleg sifirdan boyuk olmalidir")
        elif self.balance < amount:
            print("Bu emeliyyati yerine yetirmek ucun balansinizda kifayet qeder vesait yoxdur")
        else:
            self.balance -= amount
            print(f"{amount} AZN balansdan cixarildi")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = 0.05

    def apply_interest(self, interest_rate):
        evvelki_balance = self.balance
        self.balance += self.balance * interest_rate
        print(f"Yigim hesabinin faize qeder balansi: {evvelki_balance} AZN\nYigim hesabinin faizden sonra balansi: {self.balance} AZN")


if __name__ == "__main__":
    my_bank_account = BankAccount('Narmin Mailova', 10000)
    my_savings_account = SavingsAccount('Narmin Mailova', 200, 0.05)
    my_bank_account.deposit(500)
    my_savings_account.deposit(1000)
    my_bank_account.withdraw(10000)
    my_savings_account.withdraw(200)
    print(my_bank_account.get_balance(),"AZN")
    my_savings_account.apply_interest(0.05)
    print(my_savings_account.get_balance(),"AZN")