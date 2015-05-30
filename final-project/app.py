import json, operator, requests
from flask import Flask 
from flask import abort
from flask import render_template

app = Flask(__name__)

with open('static/hp-data-2015.json') as f:
    data = json.loads(f.read())

hp_data = data['usaspendingSearchResults']['result']['doc']


# SUMMARIES

# CONTRACTS BY AGENCY
agencies = {}
for h in hp_data:
    agency = h['AgencyID']
    contract_amount = float(h['DollarsObligated'])
    if agency in agencies:
        agencies[agency] += contract_amount
    else:
        agencies[agency] = contract_amount   

# print(agencies)

# CONTRACTS BY RECIPIENT CITY
recipient_city = []
cities = []
for h in hp_data:
    city_state = str(h['RecipientCity'] + ", " + h['RecipientState'])
    contract_amount = int(float(h['DollarsObligated']))
    if city_state not in cities:
        recipient_city.append([city_state, contract_amount, 1, 'x', 'y'])
        cities.append(city_state)   
    else: 
        for r in recipient_city:
            if r[0] == city_state:
                r[1] += contract_amount
                r[2] += 1 

recipient_city = sorted(recipient_city, key=operator.itemgetter(1), reverse=True)

# GEOCODING
maps_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
for r in recipient_city:
    atts = {'address': r[0], 'key': 'AIzaSyDdBsQKgsXLrHAil_feh5RK_g5lyxbRmAU'}
    resp = requests.get(maps_url, params = atts)
    data = resp.json()
    r[3] = data['results'][0]['geometry']['location']['lat']
    r[4] = data['results'][0]['geometry']['location']['lng']

print(recipient_city)

# CONTRACTS BY PERFORMANCE CITY
'''
performance_city = {}
for h in hp_data:
    if h['PlaceofPerformanceState']: # not every contract line has a 'PlaceofPerformanceState' key?
        state = h['PlaceofPerformanceState'].split(':')
        state = state[0]
        print(state)
        city = h['PrincipalPlaceCountyOrCity']
        city_state = str(city + ',' + state)
        if city_state in performance_city:
            performance_city[city_state] += 1
        else:
            performance_city[city_state] = 1

print(performance_city)            
'''

# DOLLARS OBLIGATED BY FISCAL YEAR
fiscal_year = {}
for h in hp_data:
    year = h['FiscalYear']
    contract_amount = float(h['DollarsObligated'])
    if year in fiscal_year:
        fiscal_year[year] += contract_amount
    else:
        fiscal_year[year] = contract_amount

# print(fiscal_year)

# DOLLARS OBLIGATED BY PRODUCTS OR SERVICE CODE
products_code = []
codes = []
for h in hp_data:
    code = h['ProductorServiceCode']
    contract_amount = int(float(h['DollarsObligated'])) 
    if code not in codes:
        products_code.append([code, contract_amount, 1])
        codes.append(code)   
    else: 
        for p in products_code:
            if p[0] == code:
                p[1] += contract_amount
                p[2] += 1 
        
products_code = sorted(products_code, key=operator.itemgetter(1), reverse=True)




@app.route("/")    
def index():
    template = 'index.html'
    object_list = hp_data
    products_list = products_code
    recipient_city_list = recipient_city
    return render_template(template, object_list=object_list, products_list=products_list, recipient_city_list=recipient_city_list)

'''
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_json()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row) 
    abort(404)           
'''
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
