"""
İstifadəçidən:
adını, soyadını
yaşını
peşəsini
sevdiyi hobbini
boyunu
çəkisini
soruşun, sonra isə həm qısa bir tanıtım, həm də bədən indeksini verin.
"""

name = input("Your name:\n")
age = input("Your age:\n")
job = input("Your job:\n")
hobby = input("Your hobby:\n")
height= float(input("Your height (m):\n"))
weight = int(input("Your weight (kg):\n"))
bmi = weight / (height * height)

print("Salam", "sizin adiniz", name+"dir", "ve", age, "yasiniz var.", "Sizin peseniz", job+"dir", "ve en sevdiyiniz hobbi", hobby+"dir.", "\nBeden indeksiniz: ", bmi)
