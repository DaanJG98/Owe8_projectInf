from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage')

@app.route('/dbsearch')
def search():
    resultslist = list()
    return resultslist


@app.route('/result')
def results():
    return render_template('resultpage')
