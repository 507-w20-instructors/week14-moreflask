from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_results(sort_by, sort_order, source_region):
    conn = sqlite3.connect('choc.sqlite')
    cur = conn.cursor()
    
    if sort_by == 'rating':
        sort_column = 'Rating'
    else:
        sort_column = 'CocoaPercent'

    where_clause = ''
    if (source_region != 'All'):
        where_clause = f'WHERE Region = "{source_region}"'

    q = f'''
        SELECT SpecificBeanBarName, {sort_column}
        FROM Bars
        JOIN Countries
            ON BroadBeanOriginId=Countries.Id
        {where_clause}
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
    return render_template('index3.html')

@app.route('/results', methods=['POST'])
def bars():
    sort_by = request.form['sort']
    sort_order = request.form['dir']
    source_region = request.form['region']
    results = get_results(sort_by, sort_order, source_region)
    return render_template('results.html', 
        sort=sort_by, results=results,
        region=source_region)

if __name__ == '__main__':
    app.run(debug=True)