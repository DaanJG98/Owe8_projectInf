from flask import Flask, render_template
import cx_Oracle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage')

@app.route('/dbsearch')
def search():
    resultslist = list()
    db = cx_Oracle.connect('owe7_pg2', 'blaat1234', '')
    return resultslist


@app.route('/result')
def results():
    return render_template('resultpage')
