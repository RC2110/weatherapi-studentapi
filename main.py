from flask import Flask, render_template

app = Flask("first_one")

@app.route("/")
def home():
    return render_template("tutorial.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/store/")
def store():
    return render_template("store.html")

app.run(debug=True)

