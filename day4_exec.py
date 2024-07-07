from flask import Flask, request

app = Flask(__name__)

def write_log():
    exec("print('started')")


@app.route('/')
def home():
    name = request.args.get("name")

    write_log.__code__ = write_log.__code__.replace(
        co_consts=(None, f"print('{name}')",)
    )

    write_log()

    return "good"
