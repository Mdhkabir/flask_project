

from flask import Flask,render_template, request
import db 
import psycopg2     # this is a jdbc connection

app = Flask(__name__)

@app.route("/students")
def show_students():
    conn = db.get_db_connection()
    cur = conn.cursor()
    cur.execute("select id, name, gender, city, phone from student")
    students = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("students.html", students = students)

@app.route("/home")
def home():
    return "www.google.com"


@app.route("/UserName")
def user():
    return "Used your User Name here!"

@app.route("/password")
def pwd():
    return "Type your password here!"

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]   # FIXED
    city = request.form["city"]
    phone = request.form["phone"]

    # Connect to DB
    conn = db.get_db_connection()
    cur = conn.cursor()
    

    # Insert query
    cur.execute(
        "INSERT INTO student (name, age, gender, city, phone) VALUES (%s, %s, %s, %s, %s)",
        (name, age, gender, city, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    return render_template("result.html", name=name, age=age, gender=gender, city=city, phone=phone)
    
 
if __name__ == "__main__":
    app.run(debug=True)
 