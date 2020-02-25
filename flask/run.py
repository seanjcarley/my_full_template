import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # aka "view"
def index():
    # return "<h1>Hello,</h1><h2>world!</h2>"
    return render_template("index.html")


@app.route("/about")  # aka "view"
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")  # aka "view"
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")  # aka "view"
def careers():
    return render_template("careers.html", page_title="Careers")


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
