from flask import Flask, render_template, request, flash, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Thisissocool_dude"

@app.route("/")
def home():
    flash("What's your name?")
    return render_template("home.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hello " + str(request.form['name_input']) + ", pleasure to meet you! ")
    request.form['name_input']
    return render_template("home.html")

@app.route("/number")
def number():
    session["number"] = random.randrange(0,30)
    print(session["number"])
    return render_template("number.html")

@app.route("/guess", methods=['POST'])
def result():
    if int(request.form['guess']) == session['number']:
        answer = "Correct"
        return render_template("number.html", answer=answer)
    elif int(request.form['guess']) < session['number']:
        answer = "It's too Low"
        return render_template("number.html", answer=answer)
    else:
        answer = "It's too High"
        return render_template("number.html", answer=answer)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/techsiulutions")
def techsiulutions():
    return render_template("index.html")

@app.route("/photos")
def photos():
    return render_template("photos.html")


if __name__ == '__main__':
    app.run()
