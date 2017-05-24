from flask import Flask, render_template, request
import cx_Oracle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/dbsearch', methods=['POST', 'GET'])
def search():
    text = request.form["searchword"]

    db = cx_Oracle.connect('owe7_pg2', 'blaat1234', 'cytosine.nl:1521/XE')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ORGANISME')
    result = cursor.fetchall()
    for regel in result:
        print(regel)
    print(db.version)

    return str(results(text))


def results(text):
    text = text + "abc"
    return text
    # return render_template('resultspage.html')


if __name__ == '__main__':
    app.run()