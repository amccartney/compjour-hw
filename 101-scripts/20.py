import requests, bs4

url = 'https://www.osha.gov/pls/imis/establishment.search?'
atts = {'p_logger': '1', 'establishment': 'Wal-Mart', 'State': 'CA', 'startmonth': '01', 'startyear': '2014', 'endmonth': '06', 'endyear': '2015'}

response = requests.get(url, params=atts)

soup = bs4.BeautifulSoup(response.text)

table = soup.findAll("td", {"class": "blueTen"})

print(int(len(table) / 6))