"""
Pig Latin, İngilis sözlərinin çevrilməsi ilə yaradılan bir dildir. Dilin mənşəyi məlum olmasa da, XIX əsrdən ən azı iki sənəddə qeyd edilib,
bu da onun 100 ildən çox müddətdir mövcud olduğunu göstərir. İngilis dilindən Pig Latin dilinə tərcümə etmək üçün aşağıdakı qaydalar istifadə olunur:

• Əgər söz bir samitlə başlayırsa, sözün əvvəlindəki bütün hərflər, ilk sait hərfə qədər çıxarılır və sonra sözün sonuna əlavə edilir, ardından "ay" əlavə olunur.
Məsələn, "physics" sözünü "icsphysay"  və "live" sözünü "ivelay" olaraq çevirmək olar.
• Əgər söz bir saitlə  başlayırsa, sözün sonuna "way" əlavə olunur. Məsələn, "oak" sözü "oakway" və "eight" sözü "eightway" olaraq çevrilir.

Bir proqram (main funksiyada) yazın ki, istifadəçidən bir mətn sətiri oxusun. Sonra proqram bu mətn sətirini Pig Latin dilinə çevirsin (ayrıca convert_to_pig_latin() funksiyası yaradın
və istifadəçi verdiyi sözü bu funksiyaya ötürün) və nəticəni ekrana çap etsin.

İstifadəçinin daxil etdiyi sətirin yalnız kiçik hərflər və boşluqlardan ibarər olduğu qəbul edilir.
"""

def convert_to_pig_latin(soz:str):
    if not soz:
        return "Bos metn daxil edilib"

    samitler = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    saitler = ["a", "e", "i", "o", "u"]

    soz = soz.lower()
    sozler = soz.split()
    pig_latin_sozler = []

    for soz in sozler:
        if soz[0] in samitler:
            index = 0
            while index < len(soz) and soz[index] in samitler:
                index += 1
            pig_latin_soz = soz[index:] + soz[:index] + "ay"
            pig_latin_sozler.append(pig_latin_soz)

        elif soz[0] in saitler:
            pig_latin_sozler.append(soz + "way")

    return " ".join(pig_latin_sozler)

if __name__=='__main__':
    metn = str(input("Setir daxil et: "))
    print(convert_to_pig_latin(metn))