from flask import Response
from functools import wraps
import json

ACCESS = {
    'user': 0,
    'store_attendant': 1,
    'admin': 2
}

# Test case
user_role = ACCESS.get('admin')
author = True

def store_attendant_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        role = user_role
        if role != 1:
            message = {"msg":"This feature is available to only the store attendants!"}
            response = Response(json.dumps(message), status=403)
            return response
        else:
            return fn(*args, **kwargs)
    return wrapper

def publisher_and_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if author or user_role == 2:
            return fn(*args, **kwargs)
        else:
            message = {"msg":"This feature is available to only the admin and the individual who created it!"}
            response = Response(json.dumps(message), status=403)
            return response
    return wrapper

def admin_authorised(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if user_role == 2:
            return fn(*args, **kwargs)
        else:
            message = {"msg":"This featuer is only available to people with admin rights!"}
            response = Response(json.dumps(message), status=403)
            return response
            
    return wrapper

#method for returning items in any list. i.e, list of sales, list of products, etc.
def get_all_items(items):
        if len(items) == 0:
            message = {"message": "List is Empty"}
            return message
        else:
            return items

# method to return the value of item at given index ina list
def get_chosen_item (index_label, item_index, items):
        for item in items:
            if item.get("{0}".format(index_label)) == item_index:
                return item