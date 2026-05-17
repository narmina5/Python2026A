"""
Istifadəçidən 0 la 100 arasında tam ədəd daxil etməsini istəyin.

Alınan dəyərə qədər olan bütün 3-ə, 5-ə, 3-ə və 5-ə tam bölünən ədədləri ayrı ayrı göstərin. Yəni əvvəlcə
3ə bölünən, sonra 5ə, sonra hər ikisinə bölünən ədədlər.

Təqribi çıxış belə olmalıdır:
0-100 arasında:
    3-ə bölünən ədədlər: 3, 6, 9, 12 ...
    5-ə bölünən ədədlər: 5, 10, 15, 20, 25 ...
    3-ə və 5-ə bölünən ədədlər: 15, 30, 45 ...
"""
div3 = []
div5 = []
div3_5 = []

eded = int(input("0 ve 100 arasinda tam eded daxil edin: "))
if eded in range(1, 101):
    for n in range(1, eded):
        if n % 3 == 0:
            div3.append(n)
        if n % 5 == 0:
            div5.append(n)
        if n % 15 == 0:
            div3_5.append(n)
    print("3e bolunen ededler: ", div3)
    print("5e bolunen ededler: ", div5)
    print("her ikisine bolunen ededler: ", div3_5)
else:
    print("Duzgun eded daxil edin!")