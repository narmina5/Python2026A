"""
----------------------------------------ALQORİTM----------------------------------------

- Məsələnin addım-addım həlli
- Müəyyən başlanğıc və son
- Yekun nəticə verməlidir
"""

# 5000-den 10000-e qeder butun 17ye ve 3e qaliqsiz bolunen ededleri tapin

# 0. Bir bosh siyahi yarat hansi ki icherisinde bu ededleri (3ve 17ye bolunen) saxlayaq - my_list +
# 1. 5000-den 10000-e qeder ededleri teyin et / tap +
# 2. bu araliqdan her bir ededi sech (ona eded de) +
# 3. eded 3 ve 17 ye qaliqsiz bolunurmu? +
# 4. eger bolunurse bir siyahiya (my_list e) elave et +
# 5. bu ededleri istifadeciye goster

my_list = []  # icherisinde 3 ve 17ye bolunen ededlerin tutacam
for eded in range(5000, 10001):
    if eded % 17 == 0 and eded % 3 == 0:
        my_list.append(eded)
print(my_list)

"""
----------------------------------------PSEUDOCODE----------------------------------------

- Alqoritmin yazılı təsviri
- Dilə bağlı deyil
- Koddan əvvəl düşünmək üçündür
"""

# 5000-den 10000-e qeder butun 17ye ve 3e qaliqsiz bolunen ededleri tapin
"""
BASHLA
my_list = []
FOR 5000 ve 10000 arasinda her bir EDED uchun
    IF EDED 3 ve 17ye bolunurmu?
        my_liste EDEDi elave et (my_list.append(EDED)
    ENDIF
ENDFOR
my_listi goster
SON
"""

"""
OGUZDAN TAM EDED (10-200) ISTE
EGER EDED 10-200 DEYILSE DOGRU OLANA QEDER YENIDEN ISTE
EGER EDED DOGRU DAXIL EDILDISE OPERATIONA BASHLA
ILK NOVBEDE HANSI EDEDLERIN 2 YE BOLUNDUYUNU TAP 10-200 ARASINDA
    10-200 ARASINDA BUTUN EDEDLERI TUT
    BU ARALIQDA HER BIR EDEDIN 2 YE BOLUNDUYUNE BAX
    BOLUNENLERI TEZE VEREQE YAZ


OGUZDAN TAM EDED (10-200) ISTE
EGER EDED 10-200 DEYILSE DOGRU OLANA QEDER YENIDEN ISTE
         - OPT - VERILEN DEYER EDEDDIMI?
CUT REQEMLER: 0,2,4,6,8
OGUZUN REQEMININ AXRINCI REQEMINI AL
BU AXRINCI REQEM CUT REQEMLERIN ICHINDEDIRSE CUTDUR
DEYILSE TEKDIR 


OGUZDAN TAM EDED (10-200) ISTE
EGER EDED 10-200 DEYILSE DOGRU OLANA QEDER YENIDEN ISTE
DEYERI 0 OLAN YENI EDED GOTUR
TEZE SEHIFE
NE QEDER KI YENI EDED OGUZUN EDEDINDEN KICHIKDIR
    EGER YENI EDED IKIYE BOLUNURSE VEREQE YENI EDEDI YAZ
    YENI EDEDI BIR ARTIR


OGUZDAN TAM EDED (10-200) ISTE
EGER EDED 10-200 DEYILSE DOGRU OLANA QEDER YENIDEN ISTE
OGUZUN EDEDI DOGRUDURSA
DAXIL EDILEN EDEDE QEDER EDEDLERIN HER BIRININ 2 YE BOLUNUB BOLUNMEDIYINI YOXLUYURUQ
0-dan OGUZUN EDEDE QEDER HER BIR EDEDI TEK TEK GOTUR
HER BIR EDED 2 YE BOLUNURMU?
BOLUNURSE VEREQE YAZ



START

EDED = ISTIFADECIDEN EDED AL
WHILE EDED 10-200 ARASINDA DEYILSE:
    EDED = ISTIFACEDEN EDED AL

CUTLER = YENI LIST
DONGU 0 dan EDED-e QEDER HER BIR YENI_EDED:
    EGER YENI EDED 2 Ye BOLUNURSE:
        CUTLER LISTINE ELAVE ET

END


START

EDED = INPUT()
WHILE EDED NOT IN 10-200:
    EDED = INPUT()

CUTLER = []
FOR YENI_EDED IN (0,EDED):
    IF YENI EDED 2 Ye BOLUNURSE:
        CUTLER LISTINE ELAVE ET

END



"""



"""
START

max_eded input()

DONGU
    eded in range 1,max_eded
    QALIQ = eded % 2
    EGER QALIQ == 0
        Print Eded
    EGER END
DONGU END

END
"""


"""
----------------------------------------FLOWCHART----------------------------------------

Dairə       - start, end
Romb        - şərt
Kvadrat     - proses
Oxlar       - axın yönü
"""

"""
----------------------------------------ŞƏRT STRUKTURU----------------------------------------

- if / else məntiqi şərt
- Şərt doğru → bir istiqamət
- Yanlış → digər istiqamət
"""

"""
----------------------------------------DÖNGÜ STRUKTURU----------------------------------------

- for / while istifadə olunur
- Eyni əməliyyatı təkrar icra etmək
- Əsasən siyahılar üzərində
"""

"""
----------------------------------------GİRİŞ / ÇIXIŞ (INPUT / OUTPUT)----------------------------------------

- input() → istifadəçidən dəyər almaq
- print() → ekrana nəticə çıxarmaq
"""

