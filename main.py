import requests
from datetime import datetime
from flask import Flask
from random import randint
# Flask sql alchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/#create-the-tables

app = Flask(__name__)
#different routes using the app.route decoration
the_number = randint(1, 9)

def text_color(function):
<<<<<<< HEAD
    def wrapper_function(*args):
=======
    def wrapper_function(*args, **kwargs):
>>>>>>> c77aab2 (syntax fixes)
        color = randint(0,5)
        hex = ["#FFBF00", "#FF7F50", "#DE3163", "#40E0D0", "#6495ED", "#CCCCFF"]
        color_picker = hex[color]
<<<<<<< HEAD
        return f"<h1 style='color:FF7F50;'>{function(*args)}</h1>"
    return wrapper_function


=======
        text = function(*args, **kwargs)
        return f"<h1 style='{color_picker}'>{text}</h1>"
    return wrapper_function

>>>>>>> c77aab2 (syntax fixes)
@app.route("/")
def guess_a_number():
    return "Guess a number" + str(the_number) + \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<name>")
def green(name):
    return f"Hello {name + str(12)}"

@app.route("/<int:num>")
@text_color
def number(num):
    if num < 0 or num > 10:
        return "That is not a number between 0 and 9"
    if num == the_number:
<<<<<<< HEAD
        return "<h1>You found it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if num > the_number:
        return "<h1>That number is too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if num < the_number:
        return "<h1>That number is too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    return
=======
        return "You found it!" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if num > the_number:
        return "That number is too high" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if num < the_number:
        return "That number is too low" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

>>>>>>> c77aab2 (syntax fixes)
'''@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there{name}, you are {number} years old!"'''

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
