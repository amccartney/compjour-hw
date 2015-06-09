import requests, json

url = 'https://data.cityofchicago.org/resource/n379-5uzu.json'

data = json.loads(requests.get(url).text)

print(len(data))