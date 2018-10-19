from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import blueprint, ACCESS, publisher_and_admin, admin_authorised
from functools import wraps

app = Flask(__name__)
sales_records = Sales()

# user page restrications are located in utilities.py
    
@blueprint.route('/sales', methods=['GET'])    
@admin_authorised
def get_sales():
    return jsonify(sales_records.get_all_sales())

# GET a sale by its id
@blueprint.route('/sales/<int:sale_index>' , methods=['GET'])
@publisher_and_admin
def get_a_product(sale_index):
    return jsonify(sales_records.get_single_sale (sale_index))