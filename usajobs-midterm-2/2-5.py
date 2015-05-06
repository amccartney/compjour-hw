import json
from operator import itemgetter

with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

country_list = []    

for i in intl_data:
    if i[1] > 10:
        country_list.append([i[0], i[1]])


sorted_list = sorted(country_list, key=itemgetter(1))      

for s in sorted_list:
    print(s[0] + ',' + str(s[1]))