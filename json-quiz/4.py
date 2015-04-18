import requests
import json

xfile = requests.get('http://www.compjour.org/files/code/json-examples/spotify-related-to-beyonce.json')

txt = xfile.text

obj = json.loads(txt)

genre_list = obj['artists'][0]['genres']

print("A. " + str(len(obj['artists'])))
print("B. " + obj['artists'][4]['name'])
print("C. " + str(obj['artists'][11]['followers']['total']))
print("D. " + ', '.join(genre_list))
print("E. " + obj['artists'][19]['images'][0]['url'])