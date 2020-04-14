from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/results')
def res():
    conn = sqlite3.connect('choc.sqlite')
    cur = conn.cursor()
    q = '''
        SELECT SpecificBeanBarName, Rating
        FROM Bars
        ORDER BY Rating DESC
        LIMIT 5
    '''
    cur.execute(q)

    bars = cur.fetchall()

    return render_template('choc.html', bars=bars)

@app.route('/hello', methods=['POST'])
def hello():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    print(firstname, lastname)
    return render_template('hello.html', firstname=firstname, lastname=lastname)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)