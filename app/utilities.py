from flask import Blueprint, jsonify
from functools import wraps

blueprint = Blueprint('api', __name__)
endpoints_list = """
<h2>Store Manager Challenge Two</h2>
              <li><a href='/api/v1/sales/4'>Get A single Sale Record of Id 4</a></li>
"""

ACCESS = {
    'user': 0,
    'store_attendant': 1,
    'admin': 2
}

# Test case
user_role = ACCESS['store_attendant']
author = True

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
        role = user_role
        if role == 2:
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='This featuer is only available to people with admin rights!'), 403
            
    return wrapper