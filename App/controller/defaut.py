from flask import render_template
from App import app
from App.model.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html")
