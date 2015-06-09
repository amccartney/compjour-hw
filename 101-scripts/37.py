import requests, bs4

url = 'https://www.cia.gov/about-cia/leadership'
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text)

updated = soup.select('div#content div.documentByLine div')[2]

print(updated.text)