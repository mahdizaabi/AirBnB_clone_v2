#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)

if models.storage_t != "db":
    @app.route('/cities_by_states', strict_slashes=False)
    def display_not_db():
        """desplay_citites_with_getter"""
        listx = []
        data = storage.all(State)
        for state in data.values():
            for city in state.cities:
                listx.append(city)
        return render_template('8-cities_by_states.html', listx=listx)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_states():
    """ desplay the citites coresponding to the states"""
    data = storage.all('State').values()
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def teardown_db(fake):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
