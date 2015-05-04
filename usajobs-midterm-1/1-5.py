import requests, json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

state_names = ['California','Florida','New York','Maryland']
state_results = []

for state in state_names:
    atts = {"CountrySubdivision": state, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()['TotalJobs']
    state_results.append([state, int(data)])

print(state_results)