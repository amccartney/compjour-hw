import requests, bs4

url = 'http://www.supremecourt.gov/opinions/slipopinion/14'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text)

names_dict = {'K': 'Anthony Kennedy', 'EK': 'Elena Kagan', 'SS': 'Sonia Sotomayor', 'G': 'Ruth Bader Ginsberg', 'PC': 'Per Curiam', 'AS': 'Antonin Scalia', 'T': 'Clarence Thomas', 'A': 'Samuel Alito', 'R': 'John Roberts', 'B': 'Stephen Breyer', 'D': 'Decree'}

initials = soup.select('tr td')
initials = initials[6]


if initials.text in names_dict:
    print(names_dict[initials.text])