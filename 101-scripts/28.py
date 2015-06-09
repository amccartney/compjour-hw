import requests, bs4

url = 'https://clinicaltrials.gov/'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text)

trial_count = soup.select('div#trial-count span')

print(trial_count[0].text)