import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json"

obj = json.loads(requests.get(data_url).text)

genre_list = obj['artists'][0]['genres']

print("A. " + str(len(obj['artists'])))
print("B. " + obj['artists'][4]['name'])
print("C. " + str(obj['artists'][11]['followers']['total']))
print("D. " + ', '.join(genre_list))
print("E. " + obj['artists'][19]['images'][0]['url'])