from flask import Flask
from flask_ask import Ask, statement
import googlemaps
from decouple import config
from datetime import datetime

GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY')
ORIGIN = config('ORIGIN')
DESTINATION = config('DESTINATION')
TRANSIT_MODE = config('TRANSIT_MODE')

app = Flask(__name__)
ask = Ask(app, "/")


def get_duration():
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    now = datetime.now()
    result = (gmaps.distance_matrix(ORIGIN, DESTINATION, TRANSIT_MODE, departure_time=now))
    duration = result['rows'][0]['elements'][0]['duration']['text']
    return duration


@app.route('/')
def homepage():
    return "Hi there, how ya doin?"


@ask.launch
def start_skill():
    duration = get_duration()
    duration_msag = 'You will be at work in {}'.format(duration)
    return statement(duration_msag)


@ask.intent("YesIntent")
def duration_to_work():
    duration = get_duration()
    duration_msag = 'Your distance to work is {}'.format(duration)
    return statement(duration_msag)


if __name__ == '__main__':
    app.run(debug=True)
