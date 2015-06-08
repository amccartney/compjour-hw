
import requests, json

url = 'https://analytics.usa.gov/data/live/browsers.json'

resp = requests.get(url)
data = resp.json()

print(data['totals']['browser']['Internet Explorer'])