import requests, json

url = 'https://analytics.usa.gov/data/live/top-pages-realtime.json'

obj = json.loads(requests.get(url).text)

print(obj['data'][0]['page'])