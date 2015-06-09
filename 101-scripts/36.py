import requests
from datetime import datetime
import json

url = 'https://open.whitehouse.gov/resource/p86s-ychb.json'

data = json.loads(requests.get(url).text)

visitors_in_2012 = 0
for d in data:
    split_date = d['appt_start_date'].split(' ')
    split_date = split_date[0]
    parsed_date = datetime.strptime(split_date, "%m/%d/%y").year
    if parsed_date == 2012:
        visitors_in_2012 += 1

print(visitors_in_2012)