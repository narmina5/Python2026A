"""
---------------------------------KOMMENTLƏR------------------------------------------
təksətirli və çoxsətirli
"""

# Burada biz iki print funksiyasi yazdiq
# Bura komment deyil

"""
Bura da kommentdir
bura da 
bura da
bura da
"""

'''
Bura da kommentdir
Bu bizim ikinci dersimizdir
Burada biz kommentlerle tanish olacagiq
'''

print("Salam")
print("Necesen?")


"""
----------------------------------DƏYİŞKƏNLƏR----------------------------------------

Dəyişkən adları qayda:
    - Hərf və ya alt xətt ilə başlamalıdır.
    - Hərflər, rəqəmlər və alt xəttlərdən ibarət ola bilər (xüsusi simvol və ya boşluq yoxdur).
    - Böyük hərfə həssasdır (myVar və myvar fərqlidir).

Dəyişkənlərin təyini
    - Dəyişkənlər "=" operatorundan istifadə etməklə təyin edilir.
    - Daha sonra dəyişənin dəyərini dəyişə bilərsiniz.
    - Python eyni anda çoxlu təyinata imkan verir:

Dəyişkən adları
    - Dəyişkəndə saxlanan dəyəri əks etdirən mənalı adlar seçin.
    - Dəyişən adları üçün snake_case istifadə edin (məsələn, first_name, total_price).
    - if, else, while, for kimi açar sözlərdən istifadə etməyin.
"""
a = 5
b = 7
a7 = 8
print("a7", a7)
A7 = 9
a7 = 10

feridin_yashi = 27
narminin_yashi = 21
shahinin_yashi = 36
oguzun_yashi = 26

print("a7", a7)
print("A7", A7)



"""
Dəyişkən dəyərini yazdırmaq: print()
"""

print(shahinin_yashi)
print(narminin_yashi)


"""
-----------------------------------SABİTLƏR-----------------------------------------
"""
PI = 3.141529
BIR_GUNDE_SAAT_SAYI = 24
print(BIR_GUNDE_SAAT_SAYI)

BIR_GUNDE_SAAT_SAYI = 25
print(BIR_GUNDE_SAAT_SAYI)


"""
----------------------------------DATA TİPLƏRİ--------------------------------------
Ümumi data tipləri: 
    - int (tam sayı)  -- integer
    - float (onluq sayı)
    - str (sətir)
    - bool (boolean: doğru və yanlış) - True, False

    - list, tuple, dict, set (bunlar haqqında daha sonrakı dərslərdə)
"""
# int
a = 7
b = 8
c = 9

# float
d = 0.5
e = 0.0
f = -3.7545876487536

# str
g = "salam"
r = 'necesen yaxshisan?---?? ---'

# bool
oguz_telebedir = False



a1 = 9.98
ab = 0.0






"""
----------------------------------Riyazi operatorlar----------------------------------
    - Toplama:      +   2 + 3   (=5)      
    - Çıxma:        -   5 - 3   (=2)
    - Vurma:        *   2 * 3   (=6)
    - Bölmə:        /   7 / 2   (=3.5)
    - Qalıq:        %   11 % 4  (=3)   
    - Üst:          **  2 ** 3  (=8)
    - Tam qismət:   //  14 // 3 (=4)
"""
print("================")
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a % b)
print(a ** b)
print(a // b)


"""
type() funksiyası

int()
float()
str()
bool()

round()
"""

print(type(a))
print(a1)
print(int(a1))

# a1 = int(a1)
# print(type(a1))

# my_list = [5, 6, 7]
# print(int(my_list))

a2 = 3.19
print(round(a2, 1))

print(bool(""))

