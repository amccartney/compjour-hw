### GETTING 503 ERROR ###

import requests, bs4

response = requests.get('https://www.boxer.senate.gov/about/committees.html')

soup = bs4.BeautifulSoup(response.text)

# print(soup.select('h3').text)

print(response)