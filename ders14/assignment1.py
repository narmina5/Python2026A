"""
Tam ədəd n, əgər onun bütün tam bölənlərinin (təbii ki özü xaric) cəmi n-ə bərabərdirsə, mükəmməl ədəd adlanır.

Məsələn, 28 mükəmməl ədəddir, çünki onun tam bölənləri 1, 2, 4, 7 və 14-dür və bu ədədlərin cəmi belədir:
1+2+4+7+14=28.

Müsbət bir tam ədədin mükəmməl olub-olmadığını təyin edən bir funksiya yazın (Bu hissenin flowchart və ya pseuodokodunu yazsanız onu da əlavə edin).
Funksiya bir parametr qəbul edəcək. Əgər bu parametr mükəmməl ədəd olarsa, funksiya True qaytaracaq, əks halda False qaytaracaq.

Bundan əlavə, main funksiyası yazın ki, yaratdığınız funksiyadan istifadə edərək 1-dən 10,000-ə qədər olan bütün mükəmməl ədədləri müəyyən etsin və
ekrana çap etsin.
"""

def mukemmel_eded(n):
    bolenler_list = []
    for bolenler in range(1, n):
        if n % bolenler == 0:
            bolenler_list.append(bolenler)
    if sum(bolenler_list) == n:
        return True
    return False

print(mukemmel_eded(28))


if __name__=='__main__':
    mukemmel_ededler = []
    for eded in range(1, 10001):
        if mukemmel_eded(eded) == True:
            mukemmel_ededler.append(eded)

print(f'1den 10000e qeder olan mukemmel ededler: {mukemmel_ededler}')

