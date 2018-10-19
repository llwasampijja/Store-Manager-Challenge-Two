from flask import Blueprint, jsonify
from functools import wraps

blueprint = Blueprint('api', __name__)
endpoints_list = """
<h2>Store Manager Challenge Two</h2>
              <li><a href='/api/v1/products'>View All Products</a></li>
              <li><a href='/api/v1/products/4'>Get a Product by id, i.e 4</a></li>
              <li><a href='/api/v1/products/add'>Add a Product</a></li>
              <li><a href='/api/v1/sales/add'>Create A Sale Order</a></li>
              <li><a href='/api/v1/sales/2'>Get a Sale Order by id, say 2</a></li>
              <li><a href='/api/v1/sales'>View All Sale Order</a></li>
"""

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

def publisher_and_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if author or user_role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This feature is available to only the admin and the individual who created it!'), 403
    return wrapper

def admin_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if user_role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This featuer is only available to people with admin rights!'), 403
            
    return wrapper