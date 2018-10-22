from app.models.sales import Sales
from flask import Flask, jsonify, Response, request
from app.utilities import blueprint, admin_authorised, store_attendant_authorised, publisher_and_admin
from functools import wraps
import json

app = Flask(__name__)
sales_records = Sales()
all_sales = sales_records.get_all_sales()
@blueprint.route('/sales', methods=['GET'])
@admin_authorised
def get_sales():   
    return jsonify(sales_records.get_all_sales())

# GET a sale by its id
@blueprint.route('/sales/<int:sale_index>' , methods=['GET'])
@publisher_and_admin
def get_a_sale(sale_index):
    return jsonify(sales_records.get_single_sale (sale_index))

@blueprint.route('/sales/add', methods=['POST'])  
@store_attendant_authorised  
def add_sale():
    request_data = request.get_json()
    all_sales.append(request_data)
    response = Response(json.dumps(all_sales))
    return response