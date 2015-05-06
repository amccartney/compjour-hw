import requests
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
resp = requests.get(BASE_USAJOBS_URL, params = {"CountrySubdivision": "California", "NumberOfJobs": 250})
data = resp.json()

mydict = {}
for job in data['JobData']:
    org_name = job['OrganizationName']
    if org_name in mydict:
        mydict[org_name] += 1
    else:
        mydict[org_name] = 1

print(mydict)            