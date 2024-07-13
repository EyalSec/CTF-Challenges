from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/send')
def home():
    url = request.args.get("url")

    return requests.get(
        url
    ).text

@app.route('/secret')
def secret():
    is_admin = 0
    try:
        if request.headers["X-Forwarded-For"] == "127.0.0.1":
            is_admin = 1

    except KeyError:
        if request.remote_addr == "127.0.0.1":
            is_admin = 1

    if is_admin:
        return "secret is: ewvqrv$!V@$Vrv26b!@VQwrvN#"
    else:
        return "403 admin access only"


if "this is a good ctf":
    app.run()
