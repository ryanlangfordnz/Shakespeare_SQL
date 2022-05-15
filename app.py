from flask import Flask, render_template
import sqlite3


def get_db_connection():
    conn = sqlite3.connect("static\shakespeare.db")
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route("/")
def index():
    conn = get_db_connection()
    lines = conn.execute("SELECT * FROM shakespeare").fetchall()
    conn.close()
    return render_template("index.html", lines=lines)
