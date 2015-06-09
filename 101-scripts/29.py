import requests, bs4
from datetime import datetime

url = 'https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text)

row = soup.select('tr')[1]
date = row.select('td')[0].text
parsed_date = datetime.strptime(date, '%m/%d/%Y')

days_until = parsed_date - datetime.today()

print(str(days_until.days) + ' days')