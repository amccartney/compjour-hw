import requests, json, os, time

data_url = 'http://www.compjour.org/files/code/json-examples/earthquake.usgs-significant_month.json'
data = json.loads(requests.get(data_url).text)

quakes = data['features']

# Answer A
print("A. " + data['metadata']['title'])

# Answer B
print("B. " + str(len(data['features'])))

# Answer C
magnitudes = 0
for d in quakes:
	if d['properties']['mag'] > magnitudes:
		magnitudes = d['properties']['mag']

print("C. " + str(magnitudes))	


# Answer D
tsunamis = 0
for d in quakes:
	if d['properties']['tsunami'] == 1:
		tsunamis += 1

print("D. " + str(tsunamis))		


# Answer E
from operator import itemgetter

some_list = []
for d in quakes:
	some_list.append(d['properties'])

t = sorted(some_list, key = itemgetter('mag'), reverse = False)
s = t[0]

print("E. " + s['title'])


# Answer F
x = sorted(some_list, key = itemgetter('felt'), reverse = True)
y = x[0]

print("F. " + y['title'])


# Answer G
qsecs = [d['properties']['time'] / 1000 for d in quakes]
tsec = qsecs[0]
timeobj = time.gmtime(tsec)
print("G. " + time.strftime('%Y-%m-%d %H:%M', timeobj))


# Answer H
sqsec = sorted(qsecs)
tqsec = sqsec[0]
timeobj2 = time.gmtime(tqsec)
print("H. " + time.strftime('%A, %B %d', timeobj2))


# Answer I
weekdays = ['Wednesday', 'Thursday', 'Friday', 'Monday', 'Tuesday']
weekday_quakes = 0
for d in quakes:
	t = time.gmtime(d['properties']['time'] / 1000)
	if any(time.strftime('%A', t) in w for w in weekdays):
		weekday_quakes += 1

print("I. " + str(weekday_quakes))		


# Answer J
five_to_nine_quakes = 0
for d in quakes:
	t = time.gmtime(d['properties']['time'] / 1000)
	if int(time.strftime('%H', t)) >= 5 and int(time.strftime('%H', t)) < 9:
		five_to_nine_quakes += 1

print("J. " + str(five_to_nine_quakes))		


# Answer K
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a))
	r = 6371
	return c * r

def distance_from_stanford(quake):
	stanford_lng = -122.166
	stanford_lat = 37.424
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, stanford_lng, stanford_lat)

q = max(quakes, key = distance_from_stanford)
print("K. " + q['properties']['title'])	


# Answer L
def distance_from_paris(quake):
	paris_lng = 2.351
	paris_lat = 48.857
	coords = quake['geometry']['coordinates']
	lng = coords[0]
	lat = coords[1]
	return haversine(lng, lat, paris_lng, paris_lat)

r = max(quakes, key = distance_from_paris)

print("L. " + r['properties']['title'])	


# Answer M
basemap_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=1&size=500x400'
markers_str = 'markers=color:orange'
for d in quakes:
	coords = d['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	markers_str += s

print("M. " + basemap_url + '&' + markers_str)	


# Answer N
markers_red = 'markers=color:red'
markers_orange = 'markers=color:orange'
for d in quakes:
	coords = d['geometry']['coordinates']
	lng = str(coords[0])
	lat = str(coords[1])
	s = '%7C' + lat + ',' + lng
	if int(d['properties']['mag']) >= 6.0:
		markers_red += s
	else:
		markers_orange += s	

print("N. " + basemap_url + '&' + markers_red + '&' + markers_orange)	