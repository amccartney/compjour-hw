import requests, json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

country_name = ['China','South Africa','Tajikistan']
total = 0

for country in country_name:
    atts = {"Country": country, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()
    total = total + int(data['TotalJobs'])
    print("%s has %s job listings." % (country, data['TotalJobs']))

print("Together, they have %s total job listings." % (total))    