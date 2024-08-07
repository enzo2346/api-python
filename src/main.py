from flask import Flask, render_template
from src.conf import HOST, PORT
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/home")
def home():
    return render_template("index.html", title="Home")

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)