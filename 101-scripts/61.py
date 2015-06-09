import requests, bs4

url = 'http://www.state.gov/secretary/travel/index.htm'

soup = bs4.BeautifulSoup(requests.get(url).text)

print(soup)