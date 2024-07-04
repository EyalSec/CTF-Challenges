from flask import Flask, request

app = Flask(__name__)

@app.route('/file')
def home():
    file = request.args.get("file_name")

    try:
        file_content = open(file.replace("../", "")).read()
    except:
        return "error"

    return file_content

