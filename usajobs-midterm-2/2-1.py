import requests, json

url = 'http://stash.compjour.org/data/usajobs/CountryCode.json'
BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

# os.makedirs("data-hold", exist_ok = True)
data = json.loads(requests.get(url).text)
country_codes = data['CountryCodes']
data_file = open('data-hold/intl-jobcount.json', 'w')

g = []

for c in country_codes:
    country = c['Value']
    if country != "United States":
        atts = {"Country": country, 'NumberOfJobs': 1}
        resp = requests.get(BASE_USAJOBS_URL, params = atts)
        jobs = resp.json()['TotalJobs']
        g.append([country, int(jobs)])

json.dump(g, data_file, indent = 2)
data_file.close()