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


@app.route('/hbnb/<text>')
def hex(text):
    return 'C %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
