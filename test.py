from flask import Flask, render_template, request
import db   # keep this

app = Flask(__name__)

@app.route("/home")
def home():
    return "www.google.com"

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    city = request.form["city"]

    conn = db.get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name, age, gender, city) VALUES (%s, %s, %s, %s)",
        (name, age, gender, city)
    )

    conn.commit()
    cur.close()
    conn.close()

    return render_template("result.html", name=name, age=age, gender=gender, city=city)

if __name__ == "__main__":
    app.run(debug=True)




import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="StudentDB",
        user="postgres",
        password="Kabir12345"
    )
    return conn