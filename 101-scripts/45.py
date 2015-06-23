import requests, bs4

response = requests.get('https://www.us-cert.gov/ncas/alerts')

soup = bs4.BeautifulSoup(response.text)

items = soup.select('span.document_id')

print len(items)
