from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_bars_by_rating():
    conn = sqlite3.connect('choc.sqlite')
    cur = conn.cursor()
    q = '''
        SELECT SpecificBeanBarName, Rating
        FROM Bars
        ORDER BY Rating DESC
        LIMIT 10
    '''
    results = cur.execute(q).fetchall()
    conn.close()
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bars/<sort>')
def bars(sort):
    results = get_bars_by_rating()
    return render_template('results.html', 
        sort=sort, results=results)

if __name__ == '__main__':
    app.run(debug=True)