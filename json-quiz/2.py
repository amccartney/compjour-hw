import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/graph.facebook-whitehouse.json"

obj = json.loads(requests.get(data_url).text)

print("A. " + str(obj['checkins']))
print("B. " + str(obj['likes']))
print("C. " + str(obj['location']['longitude']))
print("D. " + obj['category_list'][1]['name'])