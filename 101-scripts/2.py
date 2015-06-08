import bs4, requests

response = requests.get('http://catalog.data.gov/dataset?q=&sort=metadata_created+desc&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435605%2C-59.0625%2C61.77312286453148')

soup = bs4.BeautifulSoup(response.text)

link = soup.select("h3.dataset-heading a")[0]

print(link.text)