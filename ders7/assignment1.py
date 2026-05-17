"""
FIBONACCI
Istifadəçidən 10 - 200 arasında bir tam ədəd alın və bu ədədə qədər olan fibonacci ədədlər ardıcıllığını çap edin. Ədəd doğru olmazsa, doğru olana qədər proqram ədədi istifadəçidən istəsin.
Bilgi: Fibonacci elə ədədlər ardıcıllığıdır ki, hər ədəd öncəki iki ədədin cəminə bərabərdir. Məsələn: 0,1,1,2,3,5,8,13,21,34...
"""

my_list = []
fib_1 = 0
fib_2 = 1

while True:
    eded = int((input("Eded daxil edin: ")))
    if eded not in range(10, 201):
        print("Yeniden cehd edin")
        continue
    else:
        break


while fib_1 < eded:
    my_list.append(fib_1)
    novbeti = fib_1 + fib_2
    fib_1= fib_2
    fib_2 = novbeti

print(my_list)
