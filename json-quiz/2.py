import requests
import json

xfile = requests.get("http://www.compjour.org/files/code/json-examples/graph.facebook-whitehouse.json")

txt = xfile.text

obj = json.loads(txt)

print("A. " + str(obj['checkins']))
print("B. " + str(obj['likes']))
print("C. " + str(obj['location']['longitude']))
print("D. " + obj['category_list'][1]['name'])