from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import blueprint

app = Flask(__name__)
sales_records = Sales()
    
@blueprint.route('/sales', methods=['GET'])    
def get_sales():   
    return jsonify(sales_records.get_all_sales())

# GET a sale by its id
@blueprint.route('/sales/<int:sale_index>' , methods=['GET'])
def get_a_sale(sale_index):
    return jsonify(sales_records.get_single_sale (sale_index))

@blueprint.route('/sales/add', methods=['POST'])    
def add_sale():   
    return jsonify(sales_records.make_sale_order())