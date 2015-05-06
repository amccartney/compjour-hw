import json
from operator import itemgetter

with open("sample-geochart-2.html") as f:
    htmlstr = f.read()

with open("data-hold/intl-jobcount.json") as f:
    data = json.loads(f.read())

sorteddata = sorted(data, key = itemgetter(1), reverse = True)

chartdata = [['Country', 'Jobs']]
chartdata.extend(sorteddata[0:10])

tablerows = []
for d in sorteddata:
    tablerows.append("<tr><td>%s</td><td>%s</td></tr>" % (d[0], d[1]))

tablerows = "\n".join(tablerows)

with open("2-8.html", "w") as f:
    htmlstr = htmlstr.replace("#CHART_DATA#", str(chartdata)) 
    htmlstr = htmlstr.replace("#TABLE_ROWS#", tablerows)
    f.write(htmlstr)   