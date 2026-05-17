"""
Söz Təkrarlanma Sayğacı (Word Frequency Analyzer) mətndəki sözlərin neçə dəfə təkrarlanmasını tapmaq üçün istifadə olunur.
Bu, mətn analizi və məlumat emalı sahəsində çox vacib bir anlayışdır.
Proqram daxil edilən cümlədə hər bir sözün neçə dəfə təkrarlanmasını hesablayacaq və nəticələri ekranda göstərəcək.

---

Tapşırıq:
1. İstifadəçidən bir mətn daxil etməsini istəyin.
   (Məsələn: "Data is the new oil and data drives the world")
2. Data və data sözlərini eyni söz kimi qəbul et (hərf böyük/kiçik fərqi yoxdur)
3. Hər bir sözün təkrarlanma sayını ekranda çap edin.

---

Əlavə olaraq:
- Ən çox təkrarlanan sözü tapın və ekranda göstərin.
- Mətndəki unikal (sadəcə 1 dəfə yazılan) sözlərin sayını hesablayın.
- Nəticələri azalan ardıcıllıqla sıralayıb çap edin.

---

Nümunə çıxış:
Enter text: Data is the new oil and data drives the world
data → 2
is → 1
the → 2
new → 1
oil → 1
and → 1
drives → 1
world → 1

Ən çox təkrarlanan söz: data (2 dəfə)
Unikal sözlərin sayı: 8
"""


my_metn = input("Istifadeciden metn al: \n")
words = my_metn.split()
words = [word.casefold() for word in words]
unikal_words = []
max_word = ""
max_count = 0

for word in words:
    if word not in unikal_words:
        unikal_words.append(word)

for word in unikal_words:
    count = words.count(word)
    print(f'{word} -> {count}')

    if count > max_count:
        max_word = word
        max_count = count

print(f'En cox tekrarlanan soz: {max_word} ({max_count} defe)')
print(f'Unikal sozlerin sayi: {len(unikal_words)}')
