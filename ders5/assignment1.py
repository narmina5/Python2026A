"""
Aşağıda bir online mağazanın sifariş məbləğləri verilmişdir:
orders = [120, 45, 78, 200, 15, 90, 300]

Sizdən tələb olunur:
1. Əgər list boş deyilsə, ilk sifariş məbləğini çap edin.

2. Əgər son sifariş məbləği 50-dən kiçikdirsə, onu listdən silin.

3. Əgər listdə 200 varsa, ekrana "Big order exists" yazdırın.

4. Əgər listdəki sifarişlərin sayı 5-dən çoxdursa, ekrana "Many orders" yazdırın.

5. Əgər ən böyük sifariş 250-dən böyükdürsə, listin sonuna 500 əlavə edin.

6. Listi artan sırada düzün (sort edin).

7. Sonda alınan listi çap edin.

Qaydalar:
- Yalnız list və if istifadə edin
- for və while istifadə etmək olmaz
"""

orders = [120, 45, 78, 200, 15, 90, 300]

if len(orders) > 0:
    print("First order amount: ", orders[0])

if orders[-1] < 50:
    print(orders.pop(), "is removed from the list")

if 200 in orders:
    print("Big order exists")

if len(orders) > 5:
    print("Many orders")

if max(orders) > 250:
    orders.append(500)
    print(orders)

orders.sort()
print(orders)