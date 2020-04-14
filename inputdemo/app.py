from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # just the static HTML

@app.route('/handle_form', methods=['POST'])
def handle_the_form():
    return "form was processed"

if __name__ == "__main__":
    app.run(debug=True)

