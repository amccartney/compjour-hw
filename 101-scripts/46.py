import requests
import bs4

response = requests.get('http://www.state.gov/r/pa/ode/socialmedia/#pinterest')

soup = bs4.BeautifulSoup(response.text)

links = soup.findAll('a')

pinterest_links = 0
for l in links:
    if l.has_attr('href') and 'pinterest.com' in l['href']:
        pinterest_links += 1

print pinterest_links
