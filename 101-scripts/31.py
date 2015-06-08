import bs4
import requests
response = requests.get('http://www.regulations.gov/#!searchResults;rpp=25;po=0;cs=3;dct=N%252BFR%252BPR')
soup = bs4.BeautifulSoup(response.text)
#link = soup.select("div h1")[0]
print(response.text)