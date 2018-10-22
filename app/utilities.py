from flask import Blueprint, jsonify
from functools import wraps

blueprint = Blueprint('api', __name__)
endpoints_list = """
<h2>Store Manager Challenge Two</h2>
              <a href='/api/v1/products'>Admin Add Product</a></li>
"""

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
        if user_role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This featuer is only available to people with admin rights!'), 403
            
    return wrapper