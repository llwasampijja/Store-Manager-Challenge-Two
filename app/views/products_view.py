from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import blueprint
from functools import wraps


app = Flask(__name__)

user_role = "store_attendant"

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role == "store_attendant":
            return jsonify(msg='Admins only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


def top_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role == "store_attendant" or "admin":
            return jsonify(msg='Top Admin only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper
    
@blueprint.route('/products', methods=['GET'])
def get_products():   
    products_list = Products()
    return jsonify(products_list.get_all_products())


