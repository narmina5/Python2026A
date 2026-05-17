"""
İstifadəçidən bir tam ədəd (n) alın və 1-dən n-ə qədər bütün sadə ədədləri tapıb çap edin.
Qeyd: n 0-la 100 arasında olmalıdır (əks halda 1-100 arasında olana qədər istifadəçidən yenidən al). Sadə ədəd yalnız 1-ə və özünə bölünən ədəddir.

Məs.:
Zəhmət olmasa, bir ədəd daxil edin: 20
20-ə qədər olan sadə ədədlər: 2, 3, 5, 7, 11, 13, 17, 19
"""

my_list = []
while True:
    eded = int(input("Zehmet olmasa bir eded daxil edin: "))
    if eded not in range (0, 101):
        print("Duzgun eded daxil edin")
    else:
        break

for n in range(2, eded):
    count = 0
    for j in range(2, n):
        if n % j == 0:
            count += 1
    if count == 0:
        my_list.append(n)
print(my_list)