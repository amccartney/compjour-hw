import json
from operator import itemgetter

with open("data-hold/domestic-jobcount.json") as f:
    us_jobs = json.loads(f.read())

state_list = []

for u in us_jobs:
    if u[1] < 100:
        state_list.append([u[0], u[1]])

sorted_list = sorted(state_list, key=itemgetter(0))

for s in sorted_list:
    print(s[0] + "," + str(s[1]))