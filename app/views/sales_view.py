from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import bp

app = Flask(__name__)
    
@bp.route('/sales', methods=['GET'])    
def get_sales():   
    sales_records = Sales()
    return jsonify(sales_records.get_all_sales())
