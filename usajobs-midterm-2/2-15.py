import json, os, requests
from operator import itemgetter

with open("california-geochart.html") as f:
    htmlstr = f.read()

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

def get_ca_cities(job):
    ca_locs = []
    locations = job['Locations'].split(';')
    for n in locations:
        if "California" in n:
            ca_locs.append(n)

    for c in ca_locs:
        c_split = c.split(",")
        return(c_split[0])        

# creates a dictionary counting the number of jobs per city
jobs_per_city = {}

for job in jobs:
    city = get_ca_cities(job)
    if city in jobs_per_city:
        jobs_per_city[city] += 1
    else:
        jobs_per_city[city] = 1

# makes two lists from the dictionary to be used in the chart -- one for the table and one for the chart
table_list = []
jobs_list = [['City', 'Number of Jobs']]

for key, value in jobs_per_city.items():
    if key is not None:
        jlist = [key,value]
        table_list.append(jlist)
        jobs_list.append(jlist)

# sort cities in descending order by number of jobs they have
sorteddata = sorted(table_list, key = itemgetter(1), reverse = True)

tablerows = []
for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))    

tablerows = "\n".join(tablerows)    

with open("2-15.html", "w") as f:
    htmlstr = htmlstr.replace("#CHART_DATA#", str(jobs_list)) 
    htmlstr = htmlstr.replace("#TABLE_ROWS#", tablerows)
    f.write(htmlstr)