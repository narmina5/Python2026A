"""
================================================================================
DƏRS 28 – CURSOR AI
================================================================================

Cursor – kod yazmağı sürətləndirən süni intellekt dəstəkli IDE-dir (mühit).
Brauzerdə ChatGPT istifadə etdikdə kontekst (layihə faylları, terminal, diff)
adətən əl ilə köçürülməlidir. Cursor isə açıq layihəni, seçilmiş faylları
və terminalı bir yerdə görür; Chat, Agent (Composer) və Plan rejimləri ilə
kod üzərində birbaşa işləyir.

Bu faylda ev tapşırığı və quiz var. Cavab açarı və ya nümunə həllər bu faylda
yoxdur.

Əvvəlcədən hazırlıq:
  - Cursor quraşdırılmış olmalıdır (https://cursor.com)
  - Bu repozitoriya (Python2026A) Cursor-da açılmış olmalıdır
  - Dərs 27 materialları ilə tanışlıq faydalıdır (JSON, requests və s.)

--------------------------------------------------------------------------------
HİSSƏ A – PRATİKİ EV TAPŞIRIQLARI
--------------------------------------------------------------------------------

Tapşırıqları Cursor-da yerinə yetirin. Nəticəni öz qeyd dəftərinizdə və ya
müəllimin göstərdiyi kanalda (sinif, e-poçt, LMS) təqdim edin. Bu fayla cavab
yazmaq və ya git-ə commit etmək məcburi deyil (müəllim xüsusi istəməyincə).

1) Workspace və @ konteksti
   - Python2026A layihəsini Cursor-da açın.
   - ders27/ qovluğunu tapın və içindəki əsas faylları (məsələn main.py,
     assignment.py, student.json) siyahıya alın.
   - Chat panelində @ istifadə edərək layihə və ya qovluq konteksti verin
     (məsələn @folder ders27) və AI-dan qovluq strukturunun qısa təsvirini
     istəyin.
   - Qeydinizə: hansı @ növünü istifadə etdiyinizi və AI cavabının 2–3 cümlə
     xülasəsini yazın.

Cavab:
---
Fayl	                   Məqsəd
main.py                    Əsas dərs materialı: JSON (dump/load/dumps/loads), random və secrets, requests ilə API çağırışları (şərhlərdə GET/POST/PUT/DELETE nümunələri).
assignment.py              Ev tapşırığı: student dict yaradıb JSON fayla yazmaq/oxumaq, dumps/loads, yaş çıxarmaq, bonus get().
calisma_1_2_3.py           3 praktik məşq: zar atma, təsadüfi tələbə seçimi, 1–10 təxmin oyunu — JSON string + random birləşdirilmiş variantlar.
student.json               Tapşırıqdan yaranan nümunə data: Elvin adlı tələbənin məlumatları (yaş, qiymətlər və s.).
Qısa struktur:

ders27/
├── main.py           → dərs nümunələri (JSON, random, requests)
├── assignment.py     → ev tapşırığı + həll
├── calisma_1_2_3.py  → 3 kiçik oyun/məşq
└── student.json      → JSON data faylı
Dərsin əsas axını: Python dict ↔ JSON, təsadüfi ədədlər/tokenlər, sonra xarici API-dən JSON cavab almaq. main.py-də "title": "CursorAI" JSON nümunəsi də var — Dərs 28 ilə əlaqəlidir.


2) @file və @folder
   - @file ilə ders27/main.py haqqında sual verin (məsələn: faylda hansı
     mövzular işlənir?).
   - @folder ilə ders26/templates qovluğu haqqında sual verin (məsələn: hansı
     HTML şablonları var?).
   - Qeydinizə: hər iki sualın mətnini və fərqi (fayl vs qovluq) qısa izah edin.

Cavab:
---
1. JSON (sətir 1–50)
JSON ↔ Python uyğunluğu (object→dict, array→list, null→None və s.)
json modulu:
json.dump() — dict → fayl
json.dumps() — dict → string
json.load() — fayl → dict
json.loads() — string → dict
Nümunə dict və CursorAI ilə bağlı JSON obyekti ("title": "CursorAI")
2. RANDOM və SECRETS (sətir 53–120)
random modulu (aktiv kod):

random.random(), random.randint(), random.uniform()
Şərhlərdə (əlavə nümunələr):

random.randrange()
random.choice(), random.sample(), random.choices(), random.shuffle()
secrets modulu (təhlükəsiz təsadüfilik / tokenlər):

secrets.token_hex(), secrets.token_urlsafe()
Şərhlərdə: token_bytes, secrets.choice
3. REQUESTS — HTTP API (sətir 122–172)
Aktiv kod:

requests.get() — jsonplaceholder.typicode.com/posts ünvanına GET sorğusu
response.text, response.status_code
Şərhlərdə (əlavə HTTP metodları):

POST — məlumat göndərmək (json=data)
GET — params ilə filtr
Headers — Authorization nümunəsi
PUT — yeniləmə
DELETE — silmə
response.json() — cavabı JSON kimi parse etmək
Qısa xülasə: Fayl JSON serializasiyası, təsadüfi ədədlər/tokenlər və xarici API ilə işləməyi (requests) bir dərsdə birləşdirir. Aktiv işləyən hissələr JSON, random, secrets və sadə GET sorğusudur; qalan HTTP metodları şərh bloklarında izah üçündür.
3) Chat rejimi vs Agent rejimi
   - Kiçik bir istək seçin: məsələn, öz seçdiyiniz bir ders*/ faylına 1–2 cümləlik
     izahedici şərh (comment) əlavə etmək və ya mövcud funksiyanın nə etdiyini
     soruşmaq.
   - Eyni istəyi əvvəl Chat rejimində verin (yalnız izah / məsləhət).
   - Sonra Agent rejimində verin (dəyişiklik tətbiq etməyi xahiş edin).
   - Qeydinizə: Chat və Agent nəticələrini müqayisə edin (nə dəyişdi, diff
     gördünüzmü, faylı saxladınızmı?).

Cavab:
---

4) Prompt keyfiyyəti
   Aşağıdakı ZƏİF promptu oxuyun:
     "kodu düzəlt"

   Bu promptu AYDIN prompta çevirin (fayl adı, gözlənilən nəticə, məhdudiyyət).
   Yaxşılaşdırılmış promptu öz ders* kodunuzda real kiçik problemə (səhv mesaj,
     adlandırma, sadə refactor) tətbiq edin.
   - Qeydinizə: zəif prompt, yaxşılaşdırılmış prompt və nə baş verdiyini yazın.

5) Layihə qaydaları (Rules)
   - Layihədə .cursor/rules/ (və ya Cursor layihə qaydaları) yaradın.
   - Özünüz yazdığınız BİR qayda əlavə edin (məsələn: Azərbaycan dilində şərh,
     assignment fayllarında həll yazılmır, PEP 8 və s.).
   - Qeydinizə: qaydanın mətnini və Agent/Chat-də bu qaydanın təsir etdiyini
     düşündüyünüz bir nümunəni qeyd edin.

6) .cursorignore
   - Layihədə .cursorignore faylı varmı yoxlayın; yoxdursa yaradın və ya
     mövcud olanı oxuyun.
   - İndekslənməməli olan ən azı 3 element seçin (məsələn __pycache__,
     *.db, .env) və niyə indexlənməməli olduğunu qısa izah edin.
   - Qeydinizə: .cursorignore-da yazdığınız (və ya planlaşdırdığınız) sətirləri
     və izahı yazın.

7) Plan rejimi
   - Plan rejimində kiçik bir dəyişiklik üçün plan istəyin (məsələn: "ders27
     JSON ev tapşırığına yaş üçün sadə yoxlama əlavə et").
   - Planın YALNIZ başlığını və ilk 3 addımını qeyd dəftərinizə köçürün.
   - Tam yaradılmış kodu təqdim etməyin; plan rejiminin məqsədini 1–2 cümlə ilə
     izah edin.

8) Etik və iş axını
   - Agent təklif etdiyi dəyişiklikləri qəbul etməzdən əvvəl diff-i necə
     yoxladığınızı təsvir edin.
   - AI dəyişikliyini RƏDD etdiyiniz və ya QƏBUL etdiyiniz bir halı qeyd edin
     (səbəb: səhv fayl, lazımsız kod, təhlükəsizlik və s.).
   - Qısa cümlə: Python öyrənmək üçün AI-dan nə vaxt istifadə etmək, nə vaxt
     özünüz yazmaq daha yaxşıdır?

Əlaqə (Dərs 27):
  ders27/main.py faylında JSON nümunəsində "title": "CursorAI" keçir.
  Bu tapşırıqda həmin layihə fayllarından kontekst kimi istifadə edin.

--------------------------------------------------------------------------------
HİSSƏ B – QUIZ (12 SUAL)
--------------------------------------------------------------------------------

Cavabları müəllimin göstərdiyi üsulla təqdim edin. Bu faylda cavab açarı yoxdur.

--- Çoxseçimli suallar ---

Sual 1. Cursor əsasən nədir?
   a) Yalnız söhbət botu olan veb səhifə
   b) Kod redaktoru + layihə konteksti ilə AI inteqrasiyası olan IDE
   c) Yalnız Python interpretatoru
   d) Yalnız verilənlər bazası idarəetmə aləti

Sual 2. Brauzerdə ChatGPT ilə kod yazarkən Cursor-un əsas üstünlüyü hansıdır?
   a) İnternet olmadan işləyir
   b) Açıq layihə faylları, terminal və diff bir mühitdə AI ilə birləşir
   c) Yalnız şəkil yaradır
   d) Git commit avtomatik silir

Sual 3. Chat rejimində tipik olaraq nə gözlənilir?
   a) Fayllar avtomatik silinir
   b) Əsasən izah, məsləhət və kod nümunəsi (dəyişiklik tətbiqi məhdud ola bilər)
   c) Yalnız terminal əmrləri icra olunur
   d) Yalnız HTML render olunur

Sual 4. Agent (Composer) rejiminin əsas funksiyası nədir?
   a) Yalnız musiqi oxutmaq
   b) Layihədə faylları oxumaq, dəyişmək və tapşırıqları addım-addım yerinə yetirmək
   c) Yalnız e-poçt göndərmək
   d) Python versiyasını dəyişmək

Sual 5. @file konteksti nə üçün istifadə olunur?
   a) Müəyyən bir faylın məzmununu AI-a kontekst kimi vermək
   b) Kompüteri söndürmək
   c) Yalnız şəkil yükləmək
   d) Git branch yaratmaq

Sual 6. @folder ilə @file arasındakı fərq ən düzgün hansıdır?
   a) @folder bütün interneti indeksləyir
   b) @file bir faylı, @folder isə qovluqdakı faylları kontekstə əlavə edir
   c) Fərq yoxdur
   d) @file yalnız .exe faylları üçündür

Sual 7. .cursor/rules/ (layihə qaydaları) əsasən nə üçündür?
   a) API açarlarını saxlamaq
   b) AI-a layihə üzrə davranış və kod standartlarını öncədən bildirmək
   c) Python paketlərini silmək
   d) Yalnız fon rəngini dəyişmək

Sual 8. .cursorignore faylının məqsədi nədir?
   a) Bütün faylları məcburi indeksləmək
   b) Müəyyən fayl/qovluqları AI indeksindən və kontekstdən kənarda saxlamaq
   c) Yalnız şəbəkə sürətini artırmaq
   d) Git history-ni sıfırlamaq

--- Doğru / Yanlış ---

Sual 9. "Cursor istifadə etdikdə Python öyrənməyə ehtiyac qalmır" – ifadəsi
         həmişə doğrudur.
   (Doğru / Yanlış – cavabınızı qeyd edin)

Sual 10. Agent rejimi həmişə heç bir xəbərdarlıq olmadan bütün terminal
          əmrlərini avtomatik icra edir.
   (Doğru / Yanlış – cavabınızı qeyd edin)

--- Qısa cavablı suallar ---

Sual 11. json.dumps() ilə kodu özünüz yazmaq arasında AI-dan istifadə etmək
          zamanı hansı fərqlər var? (1–3 cümlə)

Sual 12. @code və @file nə vaxt seçilməlidir? Hər biri üçün bir nümunə
          ssenari yazın. (1–3 cümlə)

--------------------------------------------------------------------------------
TƏQDİM VƏ TƏHLÜKƏSİZLİK
--------------------------------------------------------------------------------

  - Ev tapşırığı qeydləri və quiz cavablarını müəllimin göstərdiyi kanalla
    göndərin; repozitoriyaya commit etmək yalnız müəllim istəsə.
  - API açarları, parollar və .env fayllarını heç vaxt git-ə əlavə etməyin.
  - AI təklif etdiyi kodu qəbul etməzdən əvvəl diff-i yoxlayın.

================================================================================
"""
