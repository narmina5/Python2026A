"""
================================================================================
DƏRS 24: FLASK, JINJA2 VƏ API İSTƏKLƏRİ
================================================================================

- Flask: Python web framework
- Jinja2: Template engine (HTML şablonları)
- HTTP metodları: GET, POST, PUT, DELETE
- API development: RESTful API yaratmaq

Real-world nümunələr:
- Instagram, Netflix, Pinterest Flask istifadə edir
- Hər veb-sayt URL routing istifadə edir
- API-lər modern web development-in əsasını təşkil edir
"""

# ============================================================================
# 1. FLASK NƏDİR VƏ NİYƏ İSTİFADƏ EDİRİK?
# ============================================================================

"""
Flask - Python dilində yazılmış mikro web framework-dur.

Web Framework nədir?
- Web framework, veb-saytlar və web application-lar yaratmaq üçün hazır alətlər
  və strukturlar təmin edən kitabxanadır.
- Real-world nümunə: Ev tikmək üçün materiallar və alətlər lazımdır.
  Framework də eyni məntiqdir - hazır alətlər verir, biz yalnız istifadə edirik.

Niyə Flask?
1. Sadə və asan öyrənilir
2. Kiçik proyektlər üçün ideal
3. Çevik və genişləndirilə bilər
4. Böyük şirkətlər istifadə edir:
   - Instagram (Facebook-un bir hissəsi)
   - Netflix (bəzi xidmətlərində)
   - Pinterest
   - LinkedIn (bəzi komponentlərdə)

Flask nə edir?
- URL routing: hansı URL-ə nə cavab veriləcəyini təyin edir
- Request handling: istifadəçidən gələn məlumatları emal edir
- Response generation: istifadəçiyə cavab qaytarır
- Template rendering: HTML səhifələri yaradır
"""

# ============================================================================
# 2. QURAŞDIRMA VƏ İLK PROQRAM
# ============================================================================

"""
Quraşdırma:
Terminaldə yazın: pip install flask

Virtual Environment (Virtual Mühit) nədir?
- Hər proyekt üçün ayrı Python paketləri saxlayır
- Real-world nümunə: Hər evin öz qapısı və açarı var.
  Virtual environment də eynidir - hər proyektin öz paketləri var.

Virtual environment yaratmaq (məsləhətdir):
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate     # Windows
  pip install flask
"""

# Flask-i import edirik
from flask import Flask, render_template, request, jsonify, redirect, url_for

"""
Flask import edilən modullar:
- Flask: Əsas Flask sinifi
- render_template: HTML template-ləri render etmək üçün
- request: İstifadəçidən gələn məlumatları oxumaq üçün
- jsonify: JSON formatında cavab qaytarmaq üçün
- redirect: Başqa səhifəyə yönləndirmək üçün
- url_for: URL yaratmaq üçün
"""

# Flask app yaratmaq
app = Flask(__name__)

"""
app = Flask(__name__) - nədir?

1. Flask(__name__) - Flask sinifindən obyekt yaradır
2. __name__ - cari modulun adını verir (bu halda '__main__' və ya fayl adı)
3. app - Flask application obyektidir

Niyə __name__?
- Flask-ə hansı modulun əsas modul olduğunu bildirir
- Template və static faylları tapmaq üçün istifadə olunur
- Real-world nümunə: Evin ünvanı kimi - Flask bilir ki, fayllar harada yerləşir

app obyekti nə edir?
- Bütün route-ları (yolları) saxlayır
- Serveri idarə edir
- Request-ləri emal edir
"""

# ============================================================================
# 3. ROUTING (YÖNLƏNDİRMƏ) - ƏTRAFLI İZAHAT
# ============================================================================

"""
Route (Yol) nədir?
- URL ilə funksiya arasında əlaqə yaradır
- Real-world nümunə: 
  - instagram.com/john → John-un profil səhifəsi
  - instagram.com/explore → Kəşf səhifəsi
  - instagram.com/messages → Mesajlar səhifəsi
  Hər URL müəyyən bir səhifəni açır - bu route-dur!

@app.route('/') decorator nədir?
- Decorator - funksiyanı bəzəyən xüsusi sintaksisdir
- @app.route('/') - Flask-ə deyir: "/" URL-inə gələn request-i bu funksiyaya yönləndir
- Real-world nümunə: Qapı üzərindəki işarə - hansı otağa getmək lazım olduğunu göstərir
"""
'''google.com/'''


# Ana səhifə route-u
@app.route('/')
def ana_sehife():
    """
    Bu funksiya ana səhifəni göstərir.

    Real-world nümunə:
    - instagram.com → Ana səhifə (feed)
    - google.com → Axtarış səhifəsi
    - facebook.com → Login səhifəsi

    return - istifadəçiyə göndəriləcək cavabı qaytarır
    """
    a = 5 * 125
    return f"<h1>Ana Səhifə</h1><p>Xoş gəlmisiniz! Cavabiniz = {a}</p>"


"""
Yuxarıdakı kod nə edir?
1. @app.route('/') - "/" URL-inə gələn request-i tutur
2. def ana_sehife(): - Bu request-i emal edən funksiyadır
3. return - HTML string qaytarır (istifadəçiyə göndərilir)

Niyə string qaytarır?
- Flask, return edilən string-i HTTP response-a çevirir
- Browser bu string-i HTML kimi göstərir
"""
'''instagram.com/profile/'''


# URL parametrləri ilə route
@app.route('/user/<name>')
def user_profile(name):
    """
    URL parametrləri nədir?
    - URL-də dəyişən hissələr
    - Real-world nümunə:
      - instagram.com/john → name = "john"
      - instagram.com/mary → name = "mary"
      - youtube.com/watch?v=abc123 → v = "abc123"

    <name> - bu dəyişəndir, URL-dəki dəyər funksiyaya ötürülür
    """
    return f"<h1>{name}-in profili</h1><p>Xoş gəlmisiniz, {name.upper()}!</p>"


"""
Nümunə:
- /user/john → name = "john"
- /user/mary → name = "mary"
- /user/123 → name = "123"
"""

# ============================================================================
# 4. HTTP METODLARI - ƏTRAFLI İZAHAT
# ============================================================================

"""
HTTP metodları nədir?
- Browser və server arasında məlumat mübadiləsi üsulları
- Real-world nümunə: Poçt xidməti
  - GET: Məktub oxumaq (məlumat almaq)
  - POST: Yeni məktub göndərmək (yeni məlumat yaratmaq)
  - PUT: Məktubu yeniləmək (mövcud məlumatı dəyişdirmək)
  - DELETE: Məktubu silmək (məlumatı silmək)

GET metodu:
- Məlumat oxumaq üçün istifadə olunur
- Real-world nümunələr:
  - Səhifə açmaq (instagram.com)
  - Məhsul siyahısına baxmaq (amazon.com/products)
  - Profilə baxmaq (instagram.com/john)
- URL-də məlumat göndərilir: /search?q=python
- Təhlükəsizdir - məlumat dəyişdirmir
"""


@app.route('/products', methods=['GET'])
def get_products():
    """
    GET metodu - məhsulları gətirir

    Real-world nümunə:
    - amazon.com/products → bütün məhsulları göstərir
    - instagram.com/explore → postları göstərir
    """
    products = [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Telefon", "price": 500},
        {"id": 3, "name": "Tablet", "price": 300}
    ]
    return jsonify(products)  # JSON formatında qaytarır


"""
POST metodu:
- Yeni məlumat yaratmaq üçün istifadə olunur
- Real-world nümunələr:
  - Yeni istifadəçi qeydiyyatı (instagram.com/accounts/emailsignup)
  - Yeni post yazmaq (instagram.com/create)
  - Yeni məhsul əlavə etmək
- Məlumat request body-də göndərilir (görünmür URL-də)
- Təhlükəsiz deyil - məlumat dəyişdirir
"""


@app.route('/users', methods=['POST'])
def create_user():
    """
    POST metodu - yeni istifadəçi yaradır

    Real-world nümunə:
    - Instagram-da qeydiyyatdan keçmək
    - Facebook-da hesab yaratmaq
    - Amazon-da sifariş vermək
    """
    # request.form - form məlumatlarını oxuyur
    username = request.form.get('username')
    email = request.form.get('email')

    # Real-world: Bu məlumatlar verilənlər bazasına yazılır
    new_user = {
        "id": 1,  # Verilənlər bazası avtomatik ID verir
        "username": username,
        "email": email
    }

    return jsonify(new_user), 201  # 201 = Created status kodu


"""
PUT metodu:
- Mövcud məlumatı yeniləmək üçün istifadə olunur
- Real-world nümunələr:
  - Profil məlumatlarını dəyişdirmək (instagram.com/accounts/edit)
  - Məhsul məlumatlarını yeniləmək
  - Postu redaktə etmək
- Bütün məlumatı göndərmək lazımdır
"""


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    PUT metodu - istifadəçi məlumatını yeniləyir

    Real-world nümunə:
    - Instagram-da profil şəklini dəyişdirmək
    - Facebook-da bio-nu yeniləmək
    - LinkedIn-də iş təcrübəsini əlavə etmək
    """
    # request.json - JSON məlumatlarını oxuyur
    data = request.json
    username = data.get('username')
    email = data.get('email')

    # Real-world: Verilənlər bazasında yenilənir
    updated_user = {
        "id": user_id,
        "username": username,
        "email": email
    }

    return jsonify(updated_user)


"""
DELETE metodu:
- Məlumatı silmək üçün istifadə olunur
- Real-world nümunələr:
  - Postu silmək (instagram.com/p/abc123/delete)
  - Hesabı silmək (instagram.com/accounts/remove)
  - Məhsulu silmək
- Diqqətli istifadə edilməlidir!
"""


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    DELETE metodu - istifadəçini silir

    Real-world nümunə:
    - Instagram-da hesabı silmək
    - Facebook-da postu silmək
    - Amazon-da sifarişi ləğv etmək
    """
    # Real-world: Verilənlər bazasından silinir
    return jsonify({"message": f"İstifadəçi {user_id} silindi"}), 200


# ============================================================================
# 5. REQUEST VƏ RESPONSE - ƏTRAFLI İZAHAT
# ============================================================================

"""
Request (İstək) nədir?
- İstifadəçidən serverə gələn məlumat
- Real-world nümunə: Restoranda sifariş vermək
  - Siz: "Bir pizza istəyirəm" (request)
  - Garson: "Hansı pizza?" (sual)
  - Siz: "Margarita" (request məlumatı)

Request obyekti nə ehtiva edir?
- request.method: Hansı HTTP metodu (GET, POST, PUT, DELETE)
- request.form: Form məlumatları (POST request-dən)
- request.args: URL parametrləri (GET request-dən, ?q=python kimi)
- request.json: JSON məlumatları
- request.headers: HTTP başlıqları
"""


@app.route('/search', methods=['GET'])
def search():
    """
    request.args nədir?
    - URL-dəki query parametrləri
    - Real-world nümunə:
      - google.com/search?q=python → request.args.get('q') = "python"
      - youtube.com/watch?v=abc123 → request.args.get('v') = "abc123"
      - instagram.com/explore?tag=python → request.args.get('tag') = "python"
    """
    # URL: /search?q=python&category=tech
    query = request.args.get('q', '')  # 'q' parametrini al, yoxdursa '' qaytar
    category = request.args.get('category', 'all')

    # Real-world: Verilənlər bazasında axtarış edilir
    results = f"Axtarış: {query}, Kateqoriya: {category}"
    return jsonify({"results": results})


@app.route('/login', methods=['POST'])
def login():
    """
    request.form nədir?
    - HTML form-dan gələn məlumatlar
    - Real-world nümunə:
      - Instagram login səhifəsi: username və password
      - Qeydiyyat formu: ad, email, şifrə
      - Əlaqə formu: ad, email, mesaj
    """
    # Form məlumatlarını oxuyur
    username = request.form.get('username')
    password = request.form.get('password')

    # Real-world: Verilənlər bazasında yoxlanılır
    if username == "admin" and password == "12345":
        return jsonify({"message": "Giriş uğurlu!"}), 200
    else:
        return jsonify({"message": "Yanlış məlumat!"}), 401


@app.route('/api/data', methods=['POST'])
def receive_json():
    """
    request.json nədir?
    - JSON formatında gələn məlumatlar
    - Real-world nümunə:
      - Mobile app-dən məlumat göndərmək
      - JavaScript-dən AJAX request
      - API-lər arasında məlumat mübadiləsi
    """
    # JSON məlumatlarını oxuyur
    data = request.json
    name = data.get('name')
    age = data.get('age')

    # Real-world: Məlumatlar emal olunur
    return jsonify({"received": {"name": name, "age": age}})


"""
Response (Cavab) nədir?
- Serverdən istifadəçiyə göndərilən məlumat
- Real-world nümunə: Restoranda sifariş
  - Siz: "Bir pizza istəyirəm" (request)
  - Garson: "Pizza gətirilir" (response)

Response növləri:
1. String: Sadə HTML və ya mətn
2. JSON: API-lər üçün
3. Template: Jinja2 ilə render edilmiş HTML
4. Redirect: Başqa səhifəyə yönləndirmə
"""

# ============================================================================
# 6. JINJA2 TEMPLATES - ƏTRAFLI İZAHAT
# ============================================================================

"""
Template (Şablon) nədir?
- Dinamik HTML səhifələri yaratmaq üçün şablon
- Real-world nümunələr:
  - Email şablonları: Hər email eyni dizayn, fərqli məlumat
  - CV şablonları: Eyni format, fərqli məlumat
  - Instagram post siyahısı: Hər post eyni dizayn, fərqli məzmun

Niyə template istifadə edirik?
- HTML kodunu təkrarlamırıq
- Məlumatı dinamik şəkildə göstəririk
- Kod daha təmiz və idarə oluna bilir olur

Jinja2 nədir?
- Python-un template engine-i
- Flask ilə inteqrasiya olunub
- HTML-də Python kodu yazmağa imkan verir
"""


@app.route('/home')
def home():
    """
    render_template() nədir?
    - Template faylını render edir (HTML-ə çevirir)
    - templates/ qovluğunda fayl axtarır
    - Dəyişkənləri template-ə ötürür

    Real-world nümunə:
    - Instagram feed: Hər post eyni dizayn, fərqli məlumat
    - Facebook timeline: Hər post eyni struktur, fərqli məzmun
    """
    # Template-ə ötürüləcək məlumatlar
    user_name = "Farid"
    posts = [
        {"title": "Python öyrənirəm", "likes": 10},
        {"title": "Flask proyekti", "likes": 25},
        {"title": "API yaradıram", "likes": 15}
    ]

    # Template render edilir
    # templates/home.html faylı axtarılır
    return render_template('index.html',
                           name=user_name,
                           posts=posts)


"""
Jinja2 sintaksisi:

1. {{ variable }} - Dəyişkən göstərmək
   Nümunə: <h1>{{ name }}</h1> → <h1>Farid</h1>

2. {% if condition %} ... {% endif %} - Şərt
   Nümunə:
   {% if user_logged_in %}
       <p>Xoş gəlmisiniz!</p>
   {% else %}
       <p>Giriş edin</p>
   {% endif %}

3. {% for item in items %} ... {% endfor %} - Döngü
   Nümunə:
   {% for post in posts %}
       <div>{{ post.title }}</div>
   {% endfor %}

4. {% extends 'base.html' %} - Template mirası
   - Base template-dən miras alır
   - Real-world: Hər səhifədə eyni header və footer

5. {% block content %} ... {% endblock %} - Bloklar
   - Base template-də boş bloklar
   - Child template-də doldurulur
"""


@app.route('/profile/<username>')
def profile(username):
    """
    Template ilə dinamik səhifə

    Real-world nümunə:
    - instagram.com/john → John-un profili
    - instagram.com/mary → Mary-nin profili
    - Eyni dizayn, fərqli məlumat
    """
    # Real-world: Verilənlər bazasından məlumat gətirilir
    user_info = {
        "username": username,
        "full_name": f"{username} Həsənov",
        "bio": "Python developer",
        "followers": 150,
        "following": 200,
        "posts": [
            {"id": 1, "image": "photo1.jpg", "likes": 50},
            {"id": 2, "image": "photo2.jpg", "likes": 30},
        ]
    }

    return render_template('profile.html', user=user_info)


# ============================================================================
# 7. API ENDPOINTS - ƏTRAFLI İZAHAT
# ============================================================================

"""
API (Application Programming Interface) nədir?
- Proqramlar arasında məlumat mübadiləsi üçün interfeys
- Real-world nümunələr:
  - WhatsApp API: Mesaj göndərmək
  - Instagram API: Post yükləmək
  - Facebook API: Məlumat paylaşmaq
  - Weather API: Hava proqnozu almaq

RESTful API nədir?
- REST (Representational State Transfer) prinsiplərinə əsaslanan API
- Standart HTTP metodları istifadə edir (GET, POST, PUT, DELETE)
- JSON formatında məlumat mübadiləsi

JSON nədir?
- JavaScript Object Notation
- Məlumat mübadiləsi formatı
- Real-world: Hər API JSON istifadə edir
"""

# Sadə API: Task Management
# Real-world nümunə: Todo app API

tasks = [
    {"id": 1, "title": "Python öyrənmək", "completed": False},
    {"id": 2, "title": "Flask proyekti", "completed": True},
]


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    GET /api/tasks - Bütün task-ları gətirir

    Real-world nümunə:
    - instagram.com/api/posts → bütün postları gətirir
    - facebook.com/api/users → bütün istifadəçiləri gətirir
    """
    return jsonify(tasks)


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """
    POST /api/tasks - Yeni task yaradır

    Real-world nümunə:
    - Instagram-da yeni post yaratmaq
    - Facebook-da yeni status yazmaq
    """
    data = request.json
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get('title'),
        "completed": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201  # 201 = Created


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    PUT /api/tasks/<id> - Task-u yeniləyir

    Real-world nümunə:
    - Instagram-da postu redaktə etmək
    - Facebook-da statusu dəyişdirmək
    """
    data = request.json
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = data.get('title', task['title'])
            task['completed'] = data.get('completed', task['completed'])
            return jsonify(task)
    return jsonify({"error": "Task tapılmadı"}), 404


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    DELETE /api/tasks/<id> - Task-u silir

    Real-world nümunə:
    - Instagram-da postu silmək
    - Facebook-da statusu silmək
    """
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task silindi"}), 200


"""
jsonify() nədir?
- Python dict/list-i JSON formatına çevirir
- HTTP response kimi qaytarır
- Content-Type: application/json təyin edir

Status kodları:
- 200: OK (uğurlu)
- 201: Created (yaradıldı)
- 404: Not Found (tapılmadı)
- 401: Unauthorized (icazə yoxdur)
- 500: Server Error (server xətası)
"""

# ============================================================================
# 8. SERVERİ İŞƏ SALMAQ
# ============================================================================

"""
if __name__ == "__main__": nədir?
- Fayl birbaşa işə salındıqda (python main.py) bu kod işləyir
- Import edildikdə işləmir
- Real-world nümunə: Evin əsas qapısı - yalnız birbaşa gəldikdə açılır

app.run() parametrləri:
- debug=True: Xəta olduqda ətraflı məlumat göstərir (development üçün)
- host='0.0.0.0': Bütün network interfeyslərindən gələn request-ləri qəbul edir
- port=5000: Server hansı portda işləyəcək (default: 5000)
"""

if __name__ == "__main__":
    """
    Serveri işə salır

    Terminalda görəcəksiniz:
    * Running on http://127.0.0.1:5000
    * Debug mode: on

    Browser-də açın: http://localhost:5000
    """
    app.run(debug=True, host='0.0.0.0', port=5000)

"""
Serveri dayandırmaq:
- Terminalda Ctrl+C basın

Real-world nümunə:
- Development: debug=True (xəta məlumatları görünür)
- Production: debug=False (təhlükəsizlik üçün)
"""

"""
================================================================================
XÜLASƏ
================================================================================

Bu dərsdə öyrəndiklərimiz:

1. Flask - Web framework, veb-saytlar yaratmaq üçün
2. Routing - URL-ləri funksiyalarla əlaqələndirmək
3. HTTP metodları - GET (oxumaq), POST (yaratmaq), PUT (yeniləmək), DELETE (silmək)
4. Request handling - İstifadəçidən məlumat almaq
5. Response handling - İstifadəçiyə cavab göndərmək
6. Jinja2 - Template engine, dinamik HTML səhifələri
7. API development - RESTful API yaratmaq
8. JSON - Məlumat mübadiləsi formatı

Real-world tətbiqlər:
- Instagram, Netflix, Pinterest Flask istifadə edir
- Hər veb-sayt routing istifadə edir
- API-lər modern web development-in əsasını təşkil edir
- Template-lər hər veb-saytda istifadə olunur

Növbəti addımlar:
- Workshop-da real proyekt yaradacağıqsınız
- CampusLink proyekti bu konseptləri praktikada görəcəksiniz
"""
