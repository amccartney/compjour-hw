import requests
import json
import os

data_url = 'http://www.compjour.org/files/code/json-examples/nyt-books-bestsellers-hardcover-fiction.json'
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

print(accounts['status'])

scrib_books = 0

for a in accounts:
	if accounts['books']['publisher'] == "Scribner":
		scrib_books += 1

print("A. " + str(scrib_books))

