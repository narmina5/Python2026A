"""
Qiymətlərin Kateqoriyalaşdırılması (hərf qiyməti)

İstifadəçidən imtahan balını daxil etməsini istəyin.
Qiymətləri kateqoriyalara ayırın:
90-100: “A”
80-89: “B”
70-79: “C”
60-69: “D”
0-59: “F”
"""

bal = int(input("Baliniz? "))
if 100 >= bal >= 90:
    print("A")
elif 89 >= bal >= 80:
    print("B")
elif 79 >= bal >= 70:
    print("C")
elif 69 >= bal >= 60:
    print("D")
elif 59 >= bal >= 0:
    print("F")



if 100 >= bal >= 90:
    print("A")
elif bal >= 80:
    print("B")
elif bal >= 70:
    print("C")
elif bal >= 60:
    print("D")
elif bal >= 0:
    print("F")
else:
    print("Daxil etdiyiniz bal yanlisdir")