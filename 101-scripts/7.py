import requests, json

# url = 'https://api.fda.gov/drug/enforcement.json'
# atts = {'api_key': 'HvobCMlNGQDLfIJf2je1qPIou8fv69wTuP7hFr0e', 'search':'report_date:[20120101+TO+20151231]', 'count': 'classification'}
# resp = requests.get(url, params = atts)

url = 'https://api.fda.gov/drug/enforcement.json?search=report_date:[20120101+TO+20151231]&count=classification'

resp = requests.get(url)

data = resp.json()

print(data['results'][3]['count'])