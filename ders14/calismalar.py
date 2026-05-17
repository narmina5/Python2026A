"""
Tapşırıq 1: Funksiya və Parametrlər
Bir funksiya yazın salamla(ad), hansı ki, istifadəçidən adını parametr kimi qəbul edir və onu salamlayır (heç nə qaytarmır - return).
"""
def salamla(ad):
    print(f'Salam, {ad}!')
"""
Tapşırıq 2: İki Ədədin Cəmi
İki ədədi qəbul edib onların cəmini qaytaran bir funksiya yaradın.
"""
def cem(a, b):
    return a + b
"""
Tapşırıq 3: Faktoriyal Hesablama
Bir funksiya yazın faktoriyal(n), hansı ki, verilmiş n ədədinin faktoriyalını hesablayır və qaytarır.
"""
def factorial(n):
    netice = 1
    for i in range(1, n+1):
        netice = netice * i
    return netice
"""
Tapşırıq 4: main() funksiyası yazım, hansı ki 3 parameter: ad və 2 integer ədəd alıb, istifadəçini salamlayıb, ədədləri
toplayıb faktorialını print edir. Yuxarıda yazdığınız funksiyaların hamısını istifadə edin
"""
def main(ad, a, b):
    salamla(ad)
    toplama = cem(a, b)
    print(toplama)
    print(factorial(toplama))



if __name__ == "__main__":
    main("herkes", 5, 1)