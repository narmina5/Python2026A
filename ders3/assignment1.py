"""
Aşağıdakı bütün string funksiyalarını ən az bir dəfə işlədin
"""

name = input("Adiniz? ")
#age = int(input("Yasiniz? "))
#person = {"ad": name, "yas": age}

#trans = name.maketrans("nm", "NM")

print(name.capitalize()) # ilk herfi boyuk herfe cevirir
print(name.casefold()) # setiri kicik herflere cevirir
print(name.center(35)) # setiri ortada yerlesdirir
print(name.count("o")) # mueyyen bir deyerin nece defe gorunduyunu qaytarir
print(name.encode()) # setirin kodlasdirilmis versiyasini qaytarir
print(name.endswith("n")) # setirin mueyyən bir deyerlə bitib-bitmediyini yoxlayir
print(name.expandtabs()) # setirin tab boslugunu teyin edir
print(name.find("min")) # mueyyen bir deyeri axtarir ve ilk tapilan movqeyi qaytarir
print(name.format("Hello")) # mueyyen edilmis deyerleri setirde formatlasdirir ({} lazimdir)
#print("Ad: {ad}, Yas: {yas}".format_map(person)) # mueyyen edilmis deyerleri setirde formatlasdirir
print(name.index("a")) # mueyyen bir deyeri axtarir ve ilk tapilan movqeyi qaytarir
print(name.isalnum()) # setirin butun simvollarinin herf ve ya reqem olub-olmadigini yoxlayir
print(name.isalpha()) # setirin butun simvollarinin yalniz herf olub-olmadigini yoxlayir
print(name.isascii()) # setirin butun simvollarinin ASCII simvollari olub-olmadigini yoxlayir
print(name.isdecimal()) # setirin butun simvollarinin onluq reqemler olub-olmadigini yoxlayir
print(name.isdigit()) # setirin butun simvollarinin reqem olub-olmadigini yoxlayir
print(name.isidentifier()) # setirin identifikator olub-olmadigini yoxlayir
print(name.islower()) # setirin butun herflerinin kicik olub-olmadigini yoxlayir
print(name.isnumeric()) # setirin butun simvollarinin reqem olub-olmadigini yoxlayir
print(name.isprintable()) # setirin butun simvollarinin cap edile biler olub-olmadigini yoxlayir
print(name.isspace()) # setirin butun simvollarinin bosluq olub-olmadigini yoxlayir
print(name.istitle()) # setirin basliq qaydalarina uygun olub-olmadigini yoxlayir
print(name.isupper()) # setirin butun herflerinin boyuk herf olub-olmadigini yoxlayir
print(name.join(["Mailova ", " telebedir"])) # tekrarlanan elementleri setire cevirir
print(name.ljust(3)) # setirin sola uygunlasdirilmis versiyasini qaytarir
print(name.lower()) # setiri kicik herflere cevirir
print(name.lstrip()) # sol terefden bosluqlari silir
#print(name.maketrans("nm", "NM")) # tercume cedveli qaytarir
print(name.partition("ar")) # setiri uc hisseye ayirib tuple seklinde qaytarir
print(name.replace("a", "e")) # mueyyen edilmis deyeri basqasi ile evez edir
print(name.rfind("n")) # mueyyen bir deyeri axtarir ve son tapilan movqeyi qaytarir
print(name.rindex("n")) # mueyyen bir deyeri axtarir ve son tapilan movqeyi qaytarir
print(name.rjust(10)) # setirin saga uygunlasdirilmis versiyasini qaytarir
print(name.rpartition("ar")) # setiri uc hisseye ayirib tuple seklinde qaytarir
print(name.rsplit("m")) # setiri verilmis separator uzre bolur ve siyahi qaytarir
print(name.rstrip()) # sag terefden bosluqlari silir
print(name.split("i")) # setiri verilmis separator uzre bolur ve siyahi qaytarir
print(name.splitlines()) # setiri setir qirilmalarina gore bolur ve siyahı qaytarir
print(name.startswith("m")) # setirin mueyyen bir deyer ile baslayib-baslamadigini yoxlayir
print(name.strip()) # setirdeki bosluqlari silir
print(name.swapcase()) # boyuk herfleri kicik, kicikleri ise boyuk edir
print(name.title()) # her sozun ilk herfini boyuk edir
#print(name.translate(trans)) # tercume edilmis setiri qaytarir
print(name.upper()) # setiri boyuk herflere cevirir
print(name.zfill(9)) # setiri baslangicda sifirlarla doldurur