from app.models.sales import Sales
from flask import Flask, jsonify
from app.utilities import blueprint
from functools import wraps

app = Flask(__name__)
sales_records = Sales()

ACCESS = {
    'user': 0,
    'store_attendant': 1,
    'admin': 2
}

# Test case
user_role = ACCESS['store_attendant']
author = True

def store_attendant_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role != 1:
            return jsonify(msg='This feature is available to only the store attendants!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

def admin_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This featuer is only available to people with admin rights!'), 403
            
    return wrapper

def publisher_and_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if author or user_role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This feature is available to only the admin and the individual who created it!'), 403
    return wrapper
    
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
    return jsonify(sales_records.make_sale_order())