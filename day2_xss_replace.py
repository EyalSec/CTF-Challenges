from flask import Flask, request

app = Flask(__name__)

@app.route('/home')
def home():
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    if not first_name or not last_name:
        return "need first_name and last_name"

    if "<" in first_name or ">" in first_name or '"' in first_name \
        or "<" in last_name or ">" in last_name or '"' in last_name:
        return "bad request"

    return f"""hello 
    <script>
        var first_name = \"{first_name}\"; var last_name = \"{last_name}\";
        alert(\"hello \" + first_name + \" \" + last_name);
    </script>"""


