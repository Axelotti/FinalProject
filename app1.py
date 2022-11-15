from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route("/")
def homePage():
    name = 'Axel Cortes'
    details = readDetails('static/details.txt')
    return render_template('base.html', name = name, aboutMe = details)

@app.route("/user/<name>")
def greet(name):
    return f'<p>Hello, {name}!</p>'

def hello_world2():
    return render_template('base.css')

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)
