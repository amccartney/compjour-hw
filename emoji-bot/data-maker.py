import requests, json, bs4, re
from links import urls

tmp = open('tmp-3.txt', 'w')

for url in urls:
    response = requests.get(url).text
    soup = bs4.BeautifulSoup(response)
    emoji_desc = soup.select('.entry-content ul')[0].select('li')
    emoji = soup.find('title')
    tmp.write(emoji.text + '\n')
    for e in emoji_desc:
        if e:
            tmp.write(e.text + '\n')

#    tmp.write(str(response))
