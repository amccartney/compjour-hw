# nope

import requests, bs4

url = 'http://publicpay.ca.gov/Reports/ReportBuilders/TopListNoSplit.aspx?FiscalYear=2010&TopType=1&ChartType=1&TopN=10&DataSet=1&PopCategory=0&EntityTypeIDs=4,1,2,3,5,6,9,8,7,10,11'

soup = bs4.BeautifulSoup(requests.get(url).text)

print(soup)