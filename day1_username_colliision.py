import sqlite3
from flask import Flask, request

app = Flask(__name__)
con = sqlite3.connect("sqlite.db", check_same_thread=False)

def add_user(_user: str, _password: str) -> None:
    cur = con.cursor()
    cur.execute("insert into users(user, password) values(?, ?)", [_user, _password])
    con.commit()
def check_if_user_exists(_user: str) -> list:
    cur = con.cursor()
    cur.execute("select user from users where user = ?", [_user])
    con.commit()
    return cur.fetchall()

def check_password(_user: str, _password: str) -> bool:
    cur = con.cursor()
    cur.execute("select user from users where user = ? and password = ?", [_user, _password])
    con.commit()
    return bool(cur.fetchall())

@app.route('/register', methods=['POST'])
def register():
    username, password = request.form["user"], request.form["pass"]
    if not check_if_user_exists(username):
        add_user(username.strip(), _password=password)
        return "user added"
    return "user exists"

@app.route('/login', methods=['POST'])
def login():
    username, password = request.form["user"], request.form["pass"]
    if check_password(username, password):
        return "nice :)"
    else:
        return "booooo, try again"
