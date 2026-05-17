"""
İki fərqli kursun tələbə siyahısı verilib.
Sənin məqsədin `set` əməliyyatlarından istifadə edərək qruplar arasındakı əlaqələri analiz etməkdir.

Verilənlər:
python_qrupu = ["Aysel", "Murad", "Rashid", "Nihad", "Ayan", "Murad"]
excel_qrupu  = ["Ayan", "Lale", "Fidan", "Murad", "Aysel"]

Tapşırıqlar:

1️⃣ Hər iki siyahını `set`-ə çevir və təkrarlanan adları aradan qaldır.
   print(python_set)
   print(excel_set)

2️⃣ Ortaq tələbələri tap (`intersection`) və çap et:
   print("Hər iki qrupa yazılanlar:", ...)

3️⃣ Yalnız Python qrupunda olan tələbələri tap (`difference`).

4️⃣ Yalnız birində olan tələbələri tap (`symmetric_difference`).

5️⃣ Python qrupuna yeni tələbə “Elvin” əlavə et (`add`),
   Excel qrupundan “Lale” tələbəsini sil (`discard`).

6️⃣ Nəticədə hər iki qrupu yenidən çap et və neçə tələbə qaldığını göstər.

💡 Sonda ise:
Bütün tələbələrin adlarını birləşdirib (`union`) sayını çap et.
"""
python_qrupu = ["Aysel", "Murad", "Rashid", "Nihad", "Ayan", "Murad"]
excel_qrupu  = ["Ayan", "Lale", "Fidan", "Murad", "Aysel"]
python_set = set(python_qrupu)
excel_set = set(excel_qrupu)
print(python_set)
print(excel_set)
print(f'Her iki qrupa yazilanlar: {python_set.intersection(excel_set)}')
print(f'Yalniz Python qrupunda olan telebeler: {python_set.difference(excel_set)}')
print(f'Yalniz birinde olan telebeler: {python_set.symmetric_difference(excel_set)}')
python_set.add("Elvin")
excel_set.discard("Lale")
print(f'Python qrupunda {len(python_set)}, Excel qrupunda {len(excel_set)} telebe qaldi.')
print(f'Butun telebeler: {python_set.union(excel_set)}')

