import bs4, requests

response = requests.get('http://www.data.gov/')

soup = bs4.BeautifulSoup(response.text)

link = soup.select("small a")[0]

print(link.text)