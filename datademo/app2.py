from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_results(sort_by, sort_order):
    conn = sqlite3.connect('choc.sqlite')
    cur = conn.cursor()
    
    if sort_by == 'rating':
        sort_column = 'Rating'
    else:
        sort_column = 'CocoaPercent'

    q = f'''
        SELECT SpecificBeanBarName, {sort_column}
        FROM Bars
        ORDER BY {sort_column} {sort_order}
        LIMIT 10
    '''
    print(q)
    results = cur.execute(q).fetchall()
    conn.close()
    print(results)
    return results

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/results', methods=['POST'])
def bars():
    sort_by = request.form['sort']
    sort_order = request.form['dir']
    print('getting results for', sort_by, sort_order)
    results = get_results(sort_by, sort_order)
    return render_template('results.html', 
        sort=sort_by, results=results)

if __name__ == '__main__':
    app.run(debug=True)