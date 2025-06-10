from flask import Flask, render_template
from flask import request
import random

app = Flask(__name__)

chapters = {
    1: "Tekst rozdziału 1.",
    2: "Tekst rozdziału 2.",
    3: "Tekst rozdziału 3.",
    4: "Tekst rozdziału 4.",
    5: "Tekst rozdziału 5.",
    6: "Tekst rozdziału 6.",
    7: "Tekst rozdziału 7.",
    8: "Tekst rozdziału 8.",
    9: "Tekst rozdziału 9.",
    10: "Tekst rozdziału 10.",
    11: "Tekst rozdziału 11.",
    12: "Tekst rozdziału 12."
}

names = {
    1: "Ness",
    2: "Devana",
    3: "Nina",
    4: "Ernest",
    5: "Rendy",
    6: "Michał",
}


@app.route('/')
def index():
    return render_template('index.html', title='Witaj w Flask!')


@app.route('/2')
def index2():
    random_number = random.randint(1, len(names))
    return render_template('index2.html', title=names[random_number])

@app.route('/tab')
def tablica_tadeusz():
    return render_template('index2.html', title='Witaj w Flask!')

@app.route('/chapter/<number>')
def chapter(number):
    #chapter_number = request.args.get('number', type=int)
    #chapter_text = chapters.get(chapter_number)
    return render_template('base.html', number=number)

@app.route('/greeting/<time_of_day>')
def greeting(time_of_day):
    return render_template('greeting.html', time_of_day=time_of_day)



if __name__ == '__main__':
    app.run(debug=True)