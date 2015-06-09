import requests, json

url = 'https://analytics.usa.gov/data/live/realtime.json'

data = json.loads(requests.get(url).text)

print(data['data'][0]['active_visitors'])