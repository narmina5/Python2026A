from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# URL: http://127.0.0.1:5000/
@app.route("/")
def home():
    return "Salam, Flask!"


@app.route("/users")
def haqqimizda():
    conn = sqlite3.connect('telebeler.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM telebeler')
    telebeler = cursor.fetchall()
    print(telebeler)
    conn.commit()
    conn.close()
    """
    my_team = [
        {"name": "Narmin", "role": "developer"},
        {"name": "Shahin", "role": "developer"},
        {"name": "Oguz", "role": "marketing-expert"},
        {"name": "Farid", "role": "ui/ux"},
        {"name": "Huseyn", "role": "excel"},
        {"name": "Zahid", "role": "developer"},
    ]"""

    return render_template("about.html", students=telebeler)

@app.route("/users/<int:user_id>")
def user_detail(user_id):
    conn = sqlite3.connect('telebeler.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM telebeler')
    telebeler = cursor.fetchall()  # [(1, "h"), 2]
    axtarilan_telebe = []
    for telebe in telebeler:
        if telebe[0] == user_id:
            axtarilan_telebe.append(telebe)

    conn.commit()
    conn.close()

    return render_template("about.html", students=axtarilan_telebe)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


"""
# URL parameter: /users/42
@app.route("/users/<int:user_id>")
def user_detail(user_id):
    return render_template("user.html", user_id=user_id)

# API endpoint
@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})"""