

from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


# DB Connection Function
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="StudentDB",
        user="postgres",
        password="Kabir12345"   # change this
    )
    return conn