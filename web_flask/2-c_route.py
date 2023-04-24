#!/usr/bin/python3
''' Python script that a Flask web application
    ------------------------------------------
    The application listens on 0.0.0.0 port 5000
    Routes
    ------
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by value of <text>
'''
from flask import Flask


app = Flask(__name__) 


@app.route('/', strict_slashes=False)
def hello():
    ''' Displays "Hello HBNB!" '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbhb():
    ''' Displays 'HBNB'''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    ''' displays C followed by the value of <text> '''
    text = tex.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)