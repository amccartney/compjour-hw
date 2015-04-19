import requests
import json

data_url = "http://www.compjour.org/files/code/json-examples/maps.googleapis-geocode-mcclatchy.json"

obj = json.loads(requests.get(data_url).text)

results_obj = obj['results'][0]

print("A. " + results_obj['formatted_address'])
print("B. " + obj['status'])
print("C. " + results_obj['geometry']['location_type'])
print("D. " + str(results_obj['geometry']['location']['lat']))
print("E. " + str(results_obj['geometry']['viewport']['southwest']['lng']))
print("F. " + results_obj['address_components'][0]['long_name'] + ", " + results_obj['address_components'][1]['long_name'])