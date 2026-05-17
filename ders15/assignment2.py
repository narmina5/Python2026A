"""
π ədədini aşağıdakı sonsuz ifadə ilə təxmini hesablamaq mümkündür (formulun daha aydın versiyası əlavə olunmuş şəkildədir):
π ≈ 3 + 4 / (2 × 3 × 4) − 4 / (4 × 5 × 6) + 4 / (6 × 7 × 8) − 4 / (8 × 9 × 10) + 4 / (10 × 11 × 12) − … və bu şəkildə davam edir.

Bu tapşırıqda siz bir proqram yazmalısınız. Proqram:
π üçün 15 fərqli təxmini qiymət hesablamalıdır. Proqramı elə yazın ki, bu asanlıqla 30, 40 və s. edilə bilsin
1-ci təxmini qiymət  istifadə etməlidir. (3 + 4 / (2 x 3 x 4))
Hər növbəti təxmini qiymət  daxil edərək əvvəlkindən  nəticə verməlidir.
Yəni:
1-ci nəticə → 1 hədd
2-ci nəticə → 2 hədd
3-cü nəticə → 3 hədd
…
15-ci nəticə → 15 hədd
Beləcə, proqram artırılan hər həddlə π-yə (3.14159..) daha çox yaxınlaşan dəyərlər göstərməlidir.
Təxmini nəticə belə olmalıdır:

1-ci: 3.16666666
2-ci: 3.13333333
3-cü: 3.1452380
...
15-ci: 3.14159...
"""

def calc_pi(steps):
    pi = 3.0
    n = 2
    change_sign = 1
    for step in range(1, steps+1):
        expression = change_sign * (4.0 / (n * (n +1) * (n + 2)))
        pi += expression
        print(f'{step}: {pi:.5f}')
        n += 2
        change_sign *= -1 # bunu internetden komek aldim, sign-i "+" ve "-" arasinda deyismeye her zaman

if __name__ == '__main__':
    calc_pi(15)