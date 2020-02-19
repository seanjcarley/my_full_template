import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # aka "view"
def index():
    # return "<h1>Hello,</h1><h2>world!</h2>"
    return render_template("index.html")


@app.route("/about")  # aka "view"
def about():
    return render_template("about.html")


@app.route("/contact")  # aka "view"
def contact():
    return render_template("contact.html")


@app.route("/careers")  # aka "view"
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)