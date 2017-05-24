from flask import Flask, render_template, request
import cx_Oracle


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/dbsearch', methods=['POST', 'GET'])
def search():
    text = request.form["searchword"]
    db = cx_Oracle.connect('')
    return str(results(text))


def results(text):
    text = text + "abc"
    return text
    # return render_template('resultspage.html')


if __name__ == '__main__':
    app.run()