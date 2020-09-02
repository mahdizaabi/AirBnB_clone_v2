#!/usr/bin/python3
"""
web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def view_states():
    """ display list states"""
    data = storage.all("State")
    return render_template("7-states_list.html", data=data)


@app.teardown_appcontext
def app_context():
    """teardown_appcontext"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
