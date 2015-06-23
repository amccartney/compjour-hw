import bs4
import requests

response = requests.get('http://www.fda.gov/MedicalDevices/Safety/ucm384618.htm')

soup = bs4.BeautifulSoup(response.text)

devices = soup.select("tr")

print(len(devices))
