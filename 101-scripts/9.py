import bs4
import requests
import  xml.etree.ElementTree as ET


xml = requests.get('http://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_114_1.xml').text

root = ET.fromstring(xml)

votes = 0
for vote in root[3]:
    if vote[4].text == 'Rejected':
        diff = int(vote[5][0].text) - int(vote[5][1].text)
        if diff > -5 and diff < 5:
            votes += 1

print(votes)
