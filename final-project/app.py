import json
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
    if agency in agencies:
        agencies[agency] += 1
    else:
        agencies[agency] = 1    

# print(agencies)

# CONTRACTS BY RECIPIENT CITY
recipient_city = {}
for h in hp_data:
    city_state = str(h['RecipientCity'] + "," + h['RecipientState'])
    if city_state in recipient_city:
        recipient_city[city_state] += 1
    else:
        recipient_city[city_state] = 1    

# print(recipient_city)

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
products_code = {}
for h in hp_data:
    code = h['ProductorServiceCode']
    contract_amount = float(h['DollarsObligated'])
    if code in products_code:
        products_code[code] += contract_amount
    else:
        products_code[code] = contract_amount

# print(products_code)



@app.route("/")    
def index():
    template = 'index.html'
    object_list = hp_data
    return render_template(template, object_list=object_list)


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
