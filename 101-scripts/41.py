import requests, bs4

url = 'http://clinicaltrials.gov/search?'
atts = {'term': 'alcohol', 'recr': 'Open'}

response = requests.get(url, params=atts)
soup = bs4.BeautifulSoup(response.text)

alcohol_studies = soup.select('div.results-summary')
results = alcohol_studies[0].text

print(results.split(' ')[0])