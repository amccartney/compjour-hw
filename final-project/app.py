from flask import Flask
from flask import abort
from flask import render_template
from helpers import hp_data


app = Flask(__name__)

###################################################

@app.route("/")
def index():
    template = 'index.html'
    object_list = hp_data.load_data()
    products_list = hp_data.dollars_by_product_service_code(object_list)
    recipient_city_list = hp_data.contracts_by_city(object_list)
    return render_template(template, object_list=object_list, products_list=products_list, recipient_city_list=recipient_city_list)


@app.route('/<product_id>/')
def contract_list(product_id):
    template = 'list.html'
    object_list = hp_data.load_data()
    products_list = hp_data.dollars_by_product_service_code(object_list)
    for p in products_list:
        if p[4] == product_id:
            object_list = [o for o in object_list if p[0] == o["ProductorServiceCode"]]
            return render_template(template, object_list=object_list)
    abort(404)


# This doesn't work yet
@app.route('/<product_id>/<contract_id>/')
def contract(product_id, contract_id):
    template = 'contract.html'
    object_list = hp_data.load_data()
    record = [o for o in object_list if o['record_count'] == contract_id]
    # x, y = geocode(str(record[0]['RecipientAddressLine123'], record[0]['RecipientCity'], record[0]['RecipientState']))
    return render_template(template, object=record)

"""
@app.route('/<city_id>/')
def list(city_id):
    template = 'geo-list.html'
    cities_list = recipient_city
    object_list = hp_data
    for c in cities:
        if c[5] == city:
            object_list = [o for o in object_list if c[0] == o["RecipientCity"]]
            return render_template(template, object_list=object_list)
    abort(404)
"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
