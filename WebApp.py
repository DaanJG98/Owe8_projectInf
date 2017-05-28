from flask import Flask, render_template, request
import cx_Oracle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/dbsearch', methods=['POST', 'GET'])
def search():
    resultslist = list()
    text = request.form["searchword"]

    db = cx_Oracle.connect('owe7_pg2', 'blaat1234', 'cytosine.nl:1521/XE')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ORGANISME')
    result = cursor.fetchall()
    for regel in result:
        print(regel)

    demolijst = [('13-LOX', 'Bleken', '27403427', 'Gilissen D.', '2017', 'defense, herbivore, oxylipin', 'Kutkikker', 'AOM81152.1'),
                 ('15-LOX', 'Bleken', '27403427', 'Rademaker K.', '2015', 'defense, herbivore, oxylipin', 'Ander beest',
                  'AOM81152.1')]
    for row in demolijst:
        print(row[0])

    return render_template('resultspage.html', resultlist = demolijst)


def results(text):
    text = text + "abc"
    return text
    # return render_template('resultspage.html')


if __name__ == '__main__':
    app.run()