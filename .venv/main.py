import requests
import sqlite4
from datetime import datetime
from flask import Flask
# Flask sql alchemy documentation: https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/#create-the-tables

app = Flask(__name__)
#different routes using the app.route decoration
@makebold
@app.route("/")
def hello_world():
    return"<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<strong>Bye!</strong>"

#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello there{name}, you are {number} years old!"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)