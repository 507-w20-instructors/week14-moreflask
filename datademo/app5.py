from flask import Flask, render_template, request
import sqlite3
import plotly.graph_objects as go

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
    return render_template('index4.html')

@app.route('/results', methods=['POST'])
def bars():
    sort_by = request.form['sort']
    sort_order = request.form['dir']
    source_region = request.form['region']
    results = get_results(sort_by, sort_order, source_region)
    
    plot_results = request.form.get('plot', False)
    if (plot_results):
        x_vals = [r[0] for r in results]
        y_vals = [r[1] for r in results]
        bars_data = go.Bar(
            x=x_vals,
            y=y_vals
        )
        fig = go.Figure(data=bars_data)
        div = fig.to_html(full_html=False)
        return render_template("plot.html", plot_div=div)
    else:
        return render_template('results.html', 
            sort=sort_by, results=results,
            region=source_region)

@app.route('/plot')
def plot():
    x_vals = ['lions', 'tigers', 'bears']
    y_vals = [6, 11, 3]

    bars_data = go.Bar(
        x=x_vals,
        y=y_vals
    )
    fig = go.Figure(data=bars_data)
    div = fig.to_html(full_html=False)
    return render_template("plot.html", plot_div=div)

if __name__ == '__main__':
    app.run(debug=True)