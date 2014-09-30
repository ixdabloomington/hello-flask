from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/hello/<name>")
def hello(name):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.debug = True
    app.run(host=os.environ['IP'],port=int(os.environ['PORT']))
