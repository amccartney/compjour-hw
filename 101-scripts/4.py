import requests, json

url = 'https://data.usajobs.gov/api/jobs?'
atts = {'Title': 'Librarian'}

resp = requests.get(url, params = atts)
data = resp.json()

print(len(data['JobData']))