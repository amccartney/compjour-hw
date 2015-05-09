import requests, bs4

response = requests.get('https://www.osha.gov/dep/fatcat/dep_fatcat.html')

soup = bs4.BeautifulSoup(response.text)

print(soup.select('h5')[1].text)