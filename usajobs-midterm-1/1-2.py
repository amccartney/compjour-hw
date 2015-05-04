import requests, json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

state_name = ['Alaska','Hawaii']
total = 0

for state in state_name:
    atts = {"CountrySubdivision": state, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    total = total + int(data['TotalJobs'])
    print("%s has %s job listings." % (state, data['TotalJobs']))

print("Together, they have %s total job listings." % (total))    