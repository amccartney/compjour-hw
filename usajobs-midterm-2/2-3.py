import json
with open("data-hold/domestic-jobcount.json") as f:
    domestic_data = json.loads(f.read())
with open("data-hold/intl-jobcount.json") as f:
    intl_data = json.loads(f.read())

icount = sum([d[1] for d in intl_data])
print("There are %s international jobs." % icount)

dcount = sum([d[1] for d in domestic_data])  
print("There are %s domestic jobs." % dcount)  