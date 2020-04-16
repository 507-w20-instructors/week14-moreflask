from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # just the static HTML

@app.route('/handle_form', methods=['POST'])
def handle_the_form():
    user_name = request.form["name"]
    fave_color = request.form["colors"]
    # return f"Hello {user_name}! I hear you like {fave_color}."

    return render_template('response.html', name=user_name, color=fave_color)

if __name__ == "__main__":
    app.run(debug=True)

