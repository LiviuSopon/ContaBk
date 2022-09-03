from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Working!"


@app.route("/add")
def add_contact():
    return "TO DO"


@app.route("/edit")
def edit_contact():
    return "TO DO"


@app.route("/delete")
def delete_contact():
    return "TO DO"
