"""
Abstrakt Hesablama Sistemi

Bu tapşırıqda məqsədiniz abstrakt siniflərdən istifadə edərək müxtəlif hesablama əməliyyatlarını modelləşdirməkdir.

1. Abstrakt Sinif Yaradın:
   - "Operation" adlı abstrakt sinif yaradın.
   - Bu sinifdə aşağıdakı abstrakt metodlar olsun:
        - execute(numbers: list) -> float: Verilmiş ədədlər siyahısı üzərində əməliyyatı icra edir.
        - description() -> str: Əməliyyat haqqında qısa məlumat verir.

2. Aşağıdakı alt sinifləri yaradın və hər birində abstrakt metodları implement edin:

   a) SumOperation:
       - execute(): numbers siyahısındakı bütün ədədləri toplayıb nəticəni qaytarsın.
       - description(): "Toplama əməliyyatı" qaytarsın.

   b) MaxOperation:
       - execute(): siyahıdakı ən böyük ədədi qaytarsın. Əgər siyahı boşdursa, None qaytarsın.
       - description(): "Ən böyük ədədin tapılması" qaytarsın.

   c) EvenAverageOperation:
       - execute(): yalnız cüt ədədlərin orta qiymətini hesablayıb qaytarsın.
                     Əgər siyahıda cüt ədəd yoxdursa, None qaytarsın.
       - description(): "Cüt ədədlərin orta qiymətinin hesablanması" qaytarsın.

3. Əlavə olaraq aşağıdakı funksiyanı yazın:

   run_operations(operations: list, numbers: list):
       - Hər bir əməliyyat obyektini operations siyahısından götürüb:
           - onun adını description() ilə çap etsin
           - və numbers siyahısı üzərində execute() metodunu çağıraraq nəticəni çap etsin

4. Test üçün aşağıdakı kodu istifadə edin:
   numbers = [4, 7, 2, 9, 6, 1, 8]
   operations = [SumOperation(), MaxOperation(), EvenAverageOperation()]
   run_operations(operations, numbers)

Gözlənilən Nəticə (təxmini):
Toplama əməliyyatı: 37
Ən böyük ədədin tapılması: 9
Cüt ədədlərin orta qiymətinin hesablanması: 5.0
"""
from abc import ABC, abstractmethod

class Opeartion(ABC):
    @abstractmethod
    def execute(self, numbers: list) -> float:
        pass
    @abstractmethod
    def description(self) -> str:
        pass


class SumOperation(Opeartion):
    def execute(self, numbers):
        return sum(numbers)

    def description(self):
        return "Toplama əməliyyatı:"


class MaxOperation(Opeartion):
    def execute(self, numbers):
        if len(numbers) < 1:
            return None
        else:
            return max(numbers)

    def description(self):
        return "Ən böyük ədədin tapılması:"


class EvenAverageOperation(Opeartion):
    def execute(self, numbers):
        even_numbers = [num for num in numbers if num % 2 == 0]
        if not even_numbers:
            return None
        return sum(even_numbers) / len(even_numbers)

    def description(self):
        return "Cüt ədədlərin orta qiymətinin hesablanması:"


def run_operations(operations: list, numbers: list):
    for operation in operations:
        print(operation.description())
        print(operation.execute(numbers))

if __name__ == "__main__":
    numbers = [4, 7, 2, 9, 6, 1, 8]
    operations = [SumOperation(), MaxOperation(), EvenAverageOperation()]
    run_operations(operations, numbers)