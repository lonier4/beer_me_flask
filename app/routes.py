from flask.templating import render_template
from flask import url_for
from app import app

@app.route('/')
def home():
    beer = "Beer Taste Test"
    return render_template("index.html", beer=beer)
