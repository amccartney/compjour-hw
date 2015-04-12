import csv
import os.path
DATA_DIR = 'data-hold'
csvname = os.path.join(DATA_DIR, 'sunlight_legislators.csv')

csvdata = csv.DictReader(open(csvname, encoding = 'utf-8'))

congressmembers = []

for row in csvdata:
	congressmembers.append(row) 

print ("There are {} Congressmembers listed".format(len(congressmembers)))

active_members = []
for m in congressmembers:
	if m['in_office'] == '1':
		active_members.append(m)

print ("There are {} active Congressmembers".format(len(active_members)))

#Active members in California

ca_active_members = []
for m in active_members:
	if m['state'] == 'CA':
		ca_active_members.append(m)

print ("There are {} active Congressmembers from CA".format(len(ca_active_members))	

#I'm getting a syntax error on the line below, but can't figure out why
ca_tweeters = []
for m in ca_active_members: 
	if m['twitter_id'] != '':
		ca_tweeters.append(m)

print ("There are {} active CA Congressmembers from CA on Twitter".format(len(ca_tweeters)))			