from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import blueprint, admin_authorised

app = Flask(__name__)
    
@blueprint.route('/sales', methods=['GET'])
@admin_authorised   
def get_sales():   
    sales_records = Sales()
    return jsonify(sales_records.get_all_sales())
