import requests, json, os

url = 'http://stash.compjour.org/data/usajobs/us-statecodes.json'
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

# os.makedirs("data-hold", exist_ok = True)
data_file = open('data-hold/domestic-jobcount.json', 'w')

states = json.loads(requests.get(url).text)

g = []

for s in states:
    atts = {"CountrySubdivision": s, "NumberOfJobs": 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobs = resp.json()['TotalJobs']
    g.append([s, int(jobs)])

json.dump(g, data_file, indent = 2)
data_file.close()