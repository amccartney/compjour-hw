import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json"

obj = json.loads(requests.get(data_url).text)

print("A. " + obj['name'])
print("B. " + obj['taken_at'])
print("C. " + obj['meta']['name'])
print("D. " + obj['data'][0]['active_visitors'])
print("E.", ', '.join(obj.keys()))