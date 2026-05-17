"""
Müxtəlif şəhərlərin koordinatlarını (enlik, uzunluq) saxlayan tuple-lardan ibarət bir siyahı yaradin.

Elə kod yazın ki:

    - Bütün şəhərlərin orta enliyini hesablasın.
    - Siyahı boş olarsa, "Siyahi boshdur" print elesin.

Təlimatlar:

    - Koordinatlarla bir tuple siyahısı təyin edin.
        Mes. koordinatlar = [(12.3435, -40.3453), (35,5754, -34.5773) ...]

    - Orta enliyi hesablayib yazdirin.
    - Maksimum uzunluga malik koordinati (!) yazdirin.

"""
enler = []
uzunluqlar = []
koordinatlar = [(12.3435, -40.3453), (35.5754, -34.5773), (15.5754, -62.5773), (5.5754, -2.5773)]
if not koordinatlar:
    print("Siyahi bosdur")
else:
    for element in koordinatlar:
        enler.append(element[0])
        uzunluqlar.append(element[1])

print(max(uzunluqlar))
print(sum(enler)/len(enler))
