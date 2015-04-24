import requests
import json
import os


data_url = 'http://www.compjour.org/files/code/json-examples/twitter-cspan-congress-list.json'
tempfilename = "/tmp/congresslist.json"

if os.path.exists(tempfilename):
    tfile = open(tempfilename, "r")
    j = tfile.read()
else:    
    j = requests.get(data_url).text
    tfile = open(tempfilename, "w")
    tfile.write(j)

tfile.close()
accounts = json.loads(j)


# Answer A
print("A. " + str(len(accounts)))


# Answer B
x = 0
for a in accounts:
	if a['followers_count'] > 10000:
		x += 1

print("B. " + str(x))	


# Answer C
y = 0
for a in accounts:
	if a['verified'] == True:
		y += 1

print("C. " + str(y))		


# Answer D
counts = []
for a in accounts:
	counts.append(a['followers_count'])
maxval = sorted(counts, reverse = True)[0]

print("D. " + str(maxval))


# Answer E
count_statuses = []
for a in accounts:
	count_statuses.append(a['statuses_count'])
maxval_statuses = sorted(count_statuses, reverse = True)[0]

print("E. " + str(maxval_statuses))	


# Answer F
from operator import itemgetter

q = sorted(accounts, key = itemgetter('followers_count'), reverse = True)
w = q[0]

print("F. @" + w['screen_name'] + ' has ' + str(w['followers_count']) + ' followers')


# Answer G
some_list = []
for a in accounts:
	if a['verified'] != True:
		some_list.append(a)


t = sorted(some_list, key = itemgetter('statuses_count'), reverse = True)
s = t[0]

print("G. @" + s['screen_name'] + ' has ' + str(s['statuses_count']) + ' tweets')


# Answer H
totes = 0
for a in accounts:
	totes += a['followers_count']

print("H. " + str(round(totes / len(accounts))))	


