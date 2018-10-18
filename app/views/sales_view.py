from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import bp

app = Flask(__name__)
sales_records = Sales()
    
@bp.route('/sales', methods=['GET'])    
def get_sales():   
    return jsonify(sales_records.get_all_sales())

# GET a sale by its id
@bp.route('/sales/<int:sale_index>' , methods=['GET'])
def get_a_product(sale_index):
    return jsonify(sales_records.get_single_sale (sale_index))