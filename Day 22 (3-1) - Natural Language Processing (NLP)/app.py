from flask import Flask, render_template, request, redirect
from model import Model

app =  Flask(__name__)
model = Model()


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/autocomplete", methods=["GET", "POST"])
def autocomplete():
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        phrase = request.form.get("phrase")
        results = model.autocomplete(phrase, 10)
        return render_template("autocomplete.html", results=results)
