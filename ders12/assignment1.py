"""
Scrabble™ oyununda hər bir hərfin ona aid olan xalları var. Bir sözün ümumi xalı,onun tərkibindəki hərflərin xallarının cəmi ilə hesablanır.
Daha çox istifadə olunan hərflər daha az xal dəyərinə malikdir, daha az istifadə olunan hərflər isə daha çox xal dəyərinə malikdir.

Hərflərə aid olan xallar aşağıda göstərilmişdir:

Bir xal: A, E, I, L, N, O, R, S, T və U
İki xal: D və G
Üç xal: B, C, M və P
Dörd xal: F, H, V, W və Y
Beş xal: K
Səkkiz xal: J və X
On xal: Q və Z

Elə proqram yazın ki, verilmiş söz üçün (istifadəçidən input) Scrabble™ xalını hesablayıb ekranda göstərsin.
Bunun üçün hərfləri xal dəyərləri ilə uyğunlaşdıran bir lüğət (dict) yaradın və sonra bu lüğətdən istifadə edərək sözün ümumi xalını tapın.
"""

my_dict = {
        "A": 1,
        "E": 1,
        "I": 1,
        "L": 1,
        "N": 1,
        "O": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
}

while True:
    word = input("Soz nedir? ")
    total = 0
    valid = True

    for letter in word:
        letter = letter.upper()
        if letter not in my_dict:
            print("Uygunsuz karakter, yeniden cehd edin!")
            valid = False
            break
        else:
            total += my_dict[letter]

    if valid == True:
        print(total)
        break


"""
1. Luget yarat
2. Dogru oldugu muddetce (while loop), istifadeciden soz al
3. Initialize et total = 0
4. True ya beraber deyer initialize et (valid = True)
5. Sozun herflerini iterasiya edib tap, boyuk herfe cevir
6. Eger herf lugetde yoxdursa: uygun mesaji ver ve valid = False et, varsa: total deyere, herfe uygun value nu (my_dict[letter]) elave ve beraber et
7. valid = True olan teqdirde total deyeri cap et 
"""
