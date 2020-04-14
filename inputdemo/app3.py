from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # just the static HTML

@app.route('/handle_form', methods=['POST'])
def handle_the_form():

    name = request.form["name"]
    secret = request.form["secret"]
    color = request.form["colors"]
    feeling = request.form["feeling"]

    like_pizza = "like_pizza" in request.form.keys()
    like_sushi = "like_sushi" in request.form.keys()
    like_massaman = "like_massaman" in request.form.keys()

    return render_template('response2.html', 
        name=name, 
        secret=secret,
        color=color, 
        feeling=feeling, 
        like_pizza=like_pizza,
        like_sushi=like_sushi,
        like_massaman=like_massaman)

if __name__ == "__main__":
    app.run(debug=True)

