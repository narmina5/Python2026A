"""
İki fərqli sözdə, eyni hərflər fərqli sırada dayanırsa, bu sözlər anaqram hesab olunur.
Məsələn, "evil" və "live" anaqramdır, çünki hər ikisində bir e, bir i, bir l və bir v var.


Bir proqram yazın ki, istifadəçidən iki string alsın,
onların anaqram olub-olmadığını təyin etsin və nəticəni göstərsin.
Əvvəlcə flowchart qurun.

"""

"""

START

my_str1 = Istifadeciden string al
my str2 = Istifadeciden string al

IF DONGU
if uzunluqlar !=
    Ola bilmez
elif uzunluqlar ==        
    Anaqramdir
else
    Anaqram deyil

END

"""

my_str1 = input("Istifadeciden string al: \n")
my_str2 = input("Istifadeciden string al: \n")

if len(my_str1) != len(my_str2):
    print("Anaqram ola bilmez")
elif sorted(my_str1) == sorted(my_str2):
    print(f'{my_str1} ve {my_str2} anaqramdir')
else:
    print("Anaqram deyil")
