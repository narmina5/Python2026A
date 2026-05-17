"""
İstifadəçidən bir tam ədəd (n) alın. n! (n faktoriyal) hesablayın.Bu faktoriyalın bütün rəqəmlərinin cəmini tapın.

Məs. n = 6
6! = 720
Rəqəmlərin cəmi: 9

Qeyd: ədədin faktorialı 1 dən ədədə qədər olan ədədlərin hasilinə (vurulmasına) bərabərdir (məs. 5! = 5*4*3*2*1 = 120)
"""

tam_eded = int(input("n! hesabla: "))

if tam_eded < 0:
    print("Neqativ eded olmaz")
else:
    factorial = 1
    for n in range(1, tam_eded + 1):
        factorial = factorial * n


    cem = 0
    for i in str(factorial):
        cem = cem + int(i)
print(f"{n}! = {factorial}"f"\nReqemlerin cemi: {cem}")
