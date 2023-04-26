#!/usr/bin/python3
''' Python script that starts a Flash web app. '''

from flask import abort
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' Displays Hello HBNB! '''
    return 'HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Displays HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Displays 'C' followed by <text> """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text):
    ''' Displays 'Python' followed by the value of <text>'''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('number/<int:n>', strict_slashes=False)
def num(n):
    ''' Displays number if and only if n is an integer. '''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
