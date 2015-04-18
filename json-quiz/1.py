import requests
import json

xfile = requests.get("http://www.compjour.org/files/code/json-examples/analyticsgov-realtime.json")

txt = xfile.text

obj = json.loads(txt)

print("A. " + obj['name'])
print("B. " + obj['taken_at'])
print("C. " + obj['meta']['name'])
print("D. " + obj['data'][0]['active_visitors'])
print("E.", ', '.join(obj.keys()))