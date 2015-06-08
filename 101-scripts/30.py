import bs4, requests

response = requests.get('http://www.dc.state.fl.us/oth/deathrow/execlist.html')
soup = bs4.BeautifulSoup(response.text)

print(len(soup.select('tr')))
