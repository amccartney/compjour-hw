import bs4
import requests

response = requests.get('https://data.ny.gov/browse')

soup = bs4.BeautifulSoup(response.text)

link = soup.select("div.titleLine span")[0]

print(link.text)