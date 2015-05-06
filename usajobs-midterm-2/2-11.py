import json, requests, os

CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find" + CA_FILE + "so fetching remote copy...")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()

rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
    x = val.replace("$", "").replace(",", "")
    return float(x)

def cleansalarymax(job):
    return cleanmoney(job['SalaryMax'])

sortedjobs = sorted(jobs, key = cleansalarymax, reverse = True)

for job in sortedjobs[0:5]:
    print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])))