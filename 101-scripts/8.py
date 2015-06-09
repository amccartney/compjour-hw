import requests

url = 'https://health.data.ny.gov/resource/dk4z-k3xb.json'
atts = {'comparison_results': 'Rate significantly higher than Statewide Rate'}

response = requests.get(url, params=atts)
data = response.json()

print(len(data))