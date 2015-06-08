import requests

response = requests.get('http://api.wunderground.com/api/f73aadbe8067d45a/conditions/q/37738.1.99999.json')

data = response.json()

print(data['current_observation']['relative_humidity'])