from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movies = []
    return render_template("index.html")

@app.route('/homepage')
def homepage():
    movies = []
    return render_template("homepage.html", movies=movies)