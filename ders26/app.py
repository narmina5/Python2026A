"""================================================================================MƏŞQ 1: FLASK VƏ JINJA2 PRAKTİKASI================================================================================
Tapşırıq: Kiçik şirkət veb-saytı yaradın
Tələblər:
1. Flask app yaradın
2. Aşağıdakı route-ları yaradın: - / (ana səhifə) - /about (haqqımızda) - /contact (əlaqə) - /services (xidmətlər)
3. Hər route üçün Jinja2 template istifadə edin
4. Template-də dəyişkənlər, şərtlər, döngülər istifadə edin
5. Base template yaradın (header və footer üçün)Real-world nümunə: Hər şirkətin veb-saytı var - bu da belə bir saytdır.""" #from flask import Flask, render_template

# TODO: Flask app yaradın# app = Flask(__name__)

# TODO: Ana səhifə route-u yaradın# Şirkət haqqında qısa məlumat gösterin
# Template: index.html

# TODO: Haqqımızda səhifəsi route-u yaradın# Şirkətin tarixçəsi, missiyası və komandası haqqında məlumat
# Template: about.html
# Template-də komanda üzvləri list-də göstərin (for döngüsü)

# TODO: Xidmətlər səhifəsi route-u yaradın# Şirkətin təklif etdiyi xidmətləri göstərin
# Template: services.html
# Xidmətləri list-də göstərin (for döngüsü)

# TODO: Əlaqə səhifəsi route-u yaradın# Əlaqə məlumatları (email, telefon, ünvan)
# Template: contact.html

# TODO: Serveri işə salın# if __name__ == "__main__":
# app.run(debug=True, host='0.0.0.0', port=5000)

"""
İpucu:
1. templates/ qovluğu yaradın
2. base.html - base template (header və footer)
3. index.html, about.html, services.html, contact.html - child template-lər
4. {% extends 'base.html' %} istifadə edin
5. {% block content %} ... {% endblock %} istifadə edin

Dərs materiallarından html faylları əldə edə bilərsiniz.
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():

    company_name = "FutureTech"

    return render_template(
        "index.html",
        company = company_name
    )

@app.route('/about')
def about():

    team_members = [
        "Narmin",
        "Shahin",
        "Farid",
        "Oghuz"
    ]

    return render_template(
        "about.html",
        team = team_members
    )

@app.route('/services')
def services():

    services_list = [
        "Mobile App Development",
        "Web Development",
        "UI/UX Design",
        "Web Design",
        "Cloud Services"
    ]

    return render_template(
        "services.html",
        services = services_list
    )

@app.route('/contact')
def contact():

    contact_info = {
        "email": "info@futuretech.com",
        "phone": "+994 50 123 45 67",
        "address": "Baku, Azerbaijan"
    }

    return render_template(
        "contact.html",
        contact = contact_info
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)