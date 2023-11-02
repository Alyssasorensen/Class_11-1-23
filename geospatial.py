import requests
import urllib
import json

api_key = 'AIzaSyBqpXVgyXNwPZZx71Gzgtpg_tf3GFWcoMQ'

search = 'https://maps.googleleapis.com/maps/api/geocode/json?address='

location_raw = 'New York City'
location_clean = urllib.parse.quote(location_raw)

url_request_part1 = search + location_clean

response = requests.get(url_requests_part1)
response.text