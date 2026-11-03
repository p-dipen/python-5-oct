from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1 style="color: #2E86C1; font-family: Arial;">Hello Dipen</h1>'