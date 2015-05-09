import requests, json

url = 'https://projects.propublica.org/nonprofits/api/v1/search.json'
atts = {'order': 'revenue', 'sort_order': 'desc'}

resp = requests.get(url, params = atts)
data = resp.json()

print(data['filings'][0]['organization']['name'])