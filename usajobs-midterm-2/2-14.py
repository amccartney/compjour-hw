import json, requests, os
from datetime import datetime

CA_FILE = 'data-hold/california.json'
if not os.path.exists(CA_FILE):
    print("Can't find" + CA_FILE + "so fetching remote copy")
    resp = requests.get("http://stash.compjour.org/data/usajobs/california-all.json")
    f = open(CA_FILE, 'w')
    f.write(resp.text)
    f.close()

rawdata = open(CA_FILE).read()
jdata = json.loads(rawdata)
jobs = jdata['jobs']


collection_date = datetime.strptime(jdata['date_collected'], '%Y-%m-%dT%H:%M:%S')

def daystillexpire(job):
    enddate = datetime.strptime(job['EndDate'], '%m/%d/%Y')
    return(enddate - collection_date).days 

def cleanmoney(val):
    x = val.replace("$", "").replace(",", "")
    return float(x)

for job in jobs:
    if cleanmoney(job['SalaryMin']) > 90000:
        if daystillexpire(job) < 5 and daystillexpire(job) >= 0:
            print('%s,%s,%s' % (job['JobTitle'], daystillexpire(job), job['ApplyOnlineURL']))