from app.models.products import Products
from flask import Flask, jsonify, request
from app.utilities import blueprint
from functools import wraps

app = Flask(__name__)
products_obj = Products()

ACCESS = {
    'user': 0,
    'store_attendant': 1,
    'admin': 2
}

# Test case
user_role = ACCESS['admin']
author = True

def admin_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This featuer is only available to people with admin rights!'), 403
            
    return wrapper
    
@blueprint.route('/products', methods=['GET'])
def get_products():   
    return jsonify(products_obj.get_all_products())

# GET a product by its id
@blueprint.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    return jsonify(products_obj.get_product_by_id(product_id))


@blueprint.route('/products/add', methods=['POST'])
@admin_authorised    
def add_product():
    return jsonify(products_obj.admin_add_product())
