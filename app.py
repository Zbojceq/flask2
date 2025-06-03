from flask import Flask
app = Flask(__name__)
    

@app.route('/')
def hello_world():
    return 'Hello, Ernest!'

from flask import Flask, render_template, request
@app.route('/about/<name>')
def hello(name):
    return render_template('about.html', name=name)


@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('result.html', name=name)
    return render_template('form.html')
    
@app.route('/hello/<name>')
def hello_name(name):
    return f'Witaj, {name}!'

@app.route('/<number>')
def number_check(number):
    if int(number) % 2 == 0:
        return f'Liczba podzielna przez 2'
    if int(number) % 3 == 0:
        return f'Liczba podzielna przez 3'
    if int(number) % 5 == 0:
        return f'Liczba podzielna przez 5'
    

import requests

@app.route('/api') 
def yesorno():
    response = requests.get('https://yesno.wtf/api') 
    data = response.json()
    fact = data['answer']
    return fact   
    

