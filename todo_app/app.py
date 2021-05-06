from todo_app.data import session_items
from flask import Flask
from flask import render_template
from flask import request
from requests import get

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)

bus_stops_endpoint = 'http://transportapi.com/v3/uk/places.json?lat=51.5539&lon=-0.1448&type=bus_stop&app_id=005504db&app_key=6e43d74df02d60551cfddbc4868f31c6'
live_stops_endpoint = 'http://transportapi.com/v3/uk/bus/stop/490008660N/live.json?app_id=005504db&app_key=6e43d74df02d60551cfddbc4868f31c6&group=route&nextbuses=yes'

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = get(url=live_stops_endpoint)
        live_stops = data.json()
        return render_template('index.html', live_stops=live_stops)


if __name__ == '__main__':
    app.run()
