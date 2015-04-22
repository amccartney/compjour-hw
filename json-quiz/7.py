import requests
import json
import os

data_url = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
tempfilename = "/tmp/usgs.json"

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)
