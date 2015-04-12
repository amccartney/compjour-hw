import requests
from urllib.parse import urljoin
import bs4

home_url = "http://news.stanford.edu/news/"
home_page = requests.get(home_url).text
home_soup = bs4.BeautifulSoup(home_page)

topic_links = home_soup.select('.topiclist li a')
print ("There are {} topic links total".format(len(topic_links))) 

for link in topic_links:
	if link['href'].find('/tags') > -1:
		print("Tagged topic:", link.text, "at URL:", link['href'])
		
		tag_url = urljoin(home_url, link['href'])
		tpage = requests.get(tag_url).text
		tsoup = bs4.BeautifulSoup(tpage)

		heds = tsoup.select("#main-content .postcard-text")

		h = heds[0]
		hed = h.find('h3').text

		print ("	Latest headline: {}".format(hed))
		print ("")