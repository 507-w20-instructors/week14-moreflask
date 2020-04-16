from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
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

if __name__ == '__main__':
    app.run(debug=True)