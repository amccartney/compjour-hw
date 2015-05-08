import json, requests, os
from operator import itemgetter

CA_FILE = 'data-hold/california.json'

rawdata = open(CA_FILE).read()
jobs = json.loads(rawdata)['jobs']

def cleanmoney(val):
    x = val.replace("$", "").replace(",", "")
    return float(x)

def cleansalarymax(job):
    return cleanmoney(job['SalaryMax'])

clean_jobs = []

for job in jobs:
    if cleanmoney(job['SalaryMax']) < 100000:
        salary_gap = cleanmoney(job['SalaryMax']) - cleanmoney(job['SalaryMin'])
        clean_jobs.append([job['JobTitle'], cleanmoney(job['SalaryMin']), cleansalarymax(job),salary_gap])

sorted_jobs = sorted(clean_jobs, key = itemgetter(2), reverse = True)
highest_diff = sorted_jobs[0]

print("%s,%d,%d" % (highest_diff[0], highest_diff[1], highest_diff[2]))