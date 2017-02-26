import googlemaps
from decouple import config
from datetime import datetime

GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY')
ORIGIN = config('ORIGIN')
DESTINATION = config('DESTINATION')
TRANSIT_MODE = config('TRANSIT_MODE')


gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
now = datetime.now()
result = (gmaps.distance_matrix(ORIGIN, DESTINATION, TRANSIT_MODE, departure_time=now,traffic_model='best_guess'))
duration = result['rows'][0]['elements'][0]['duration_in_traffic']['text']
print (duration)
