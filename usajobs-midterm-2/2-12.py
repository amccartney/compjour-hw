import json, requests, os

CA_FILE = 'data-hold/california.json'

rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
    x = val.replace("$", "").replace(",", "")
    return float(x)

def cleansalarymax(job):
    return cleanmoney(job['SalaryMax'])

sortedjobs = sorted(jobs, key = cleansalarymax, reverse = True)

for job in jobs:
    if cleansalarymax < 100000:
        
    print('%s,%d,%d' % (job['JobTitle'], cleanmoney(job['SalaryMin']), cleanmoney(job['SalaryMax'])))