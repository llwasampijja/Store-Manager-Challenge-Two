from flask import jsonify
from functools import wraps

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