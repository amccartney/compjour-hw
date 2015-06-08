import bs4, requests, csv

response = requests.get('https://inventory.data.gov/dataset/fe9eeb10-2e90-433e-a955-5c679f682502/resource/b626ef1f-9019-41c4-91aa-5ae3f7457328/download/federalexecagncyintntdomains03302015.csv').text
reader = csv.reader(response.splitlines())

line_count = 0
for row in reader:
    line_count += 1

print(line_count)