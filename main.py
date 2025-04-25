import requests
from datetime import datetime
from flask import Flask
from random import randint
# Flask sql alchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/#create-the-tables

app = Flask(__name__)
#different routes using the app.route decoration
the_number = randint(0, 9)

def text_color(function):
    def wrapper_function(*args):
        color = randint(0,5)
        hex = ["FFBF00", "FF7F50", "DE3163", "40E0D0", "6495ED", "CCCCFF"]
        color_picker = hex[color]
        return f"<h1 style='color:FF7F50;'>{function(*args)}</h1>"
    return wrapper_function


@app.route("/")
def guess_a_number():
    return"<h1 style='color:FFBF00'>Guess a number</h1>" + str(the_number)


@app.route("/<name>")
def green(name):
    return f"Hello {name + str(12)}"

@text_color
@app.route("/<int:num>")
def number(num):
    if num < 0 or num > 10:
        return "<h1>That is not a number between 0 and 9</h1>"
    if num == the_number:
        return "<h1>You found it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if num > the_number:
        return "<h1>That number is too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if num < the_number:
        return "<h1>That number is too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    return
'''@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there{name}, you are {number} years old!"'''

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
