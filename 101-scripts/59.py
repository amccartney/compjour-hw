import requests, bs4

url = 'http://catalog.data.gov/dataset?q=university'
soup = bs4.BeautifulSoup(requests.get(url).text)

datasets = soup.select('div.new-results')

print(datasets[0].text)