from flask import Blueprint
from functools import wraps


blueprint = Blueprint('api', __name__)
endpoints_list = """
<h2>Store Manager Challenge Two</h2>
              List of End Points <br>
              <ul>
              <li><a href='/api/v1/products'>View all Products</a></li>
              </ul>
"""

# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         role = user_role
#         if role == "store_attendant":
#             return jsonify(msg='Admins only!'), 403
#         else:
#             return fn(*args, **kwargs)
#     return wrapper