from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/birthday')
def birthday():
    return 'November 7 1998'


@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    total = a + b
    totalAsString = str(total)
    return totalAsString


@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    total = a - b
    totalAsString = str(total)
    return totalAsString


@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    total = a * b
    totalAsString = str(total)
    return totalAsString


@app.route('/favoritefoods')
def favoritefoods():
    favfoods = ['football', 'basketball', 'rugby']
    return jsonify(favfoods)
