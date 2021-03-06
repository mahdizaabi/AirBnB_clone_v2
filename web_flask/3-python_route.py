#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """return hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hellox():
    """return html content"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hex(text):
    """return html content"""
    return 'C %s' % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<text>')
def python(text):
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
