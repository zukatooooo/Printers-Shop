from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<profile_id>")
def homepage(profile_id):
    print("profile id", profile_id)
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def sing_up():
    return render_template("signup.html")

app.run(debug=True)