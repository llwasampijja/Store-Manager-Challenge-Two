"""
The utilities.py module includes constants and methods 
which can be called from any moddule within this application
"""
from flask import Response
from functools import wraps
import json
from app.validity_check import check_item_in_list
import random

"""
This includes the different types of accounts for this application. 
The "user" account is assumeed to have 0 rights. That is he/she is not logged in.
At this instance, for testing purposes, it is assumed that the user of the application 
is either a store_attendant or admin
The "store_attendant" and "admin" accounts have rights to this application.

"""
ACCESS = {
    'user': 0,
    'store_attendant': 1,
    'admin': 2
}

"""
This is the test case for securing urls to different users. 
The "author" is to determine if the current user (store_attendant) is the author of a given sales record.
"""
user_role = ACCESS.get('admin')
author = True

def store_attendant_authorised(fn):
    """
    This decorator is for restricting content to only be availble to store attendants
    """
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
    """
    This docorator is for granting access to content which is
     only available to admins as well as the authors of the content.
    """
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
    """
    This decorator is for restricting content to only be accessed by admins
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if user_role == 2:
            return fn(*args, **kwargs)
        else:
            message = {"msg":"This featuer is only available to people with admin rights!"}
            response = Response(json.dumps(message), status=403)
            return response
            
    return wrapper

# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         claims = get_jwt_claims()
#         if claims['roles'] != 'admin':
#             return jsonify(msg='Admins only!'), 403
#         else:
#             return fn(*args, **kwargs)
#     return wrapper

def get_all_items(items):
    """
    method for returning items in any list. i.e, list of sales, list of products, etc.
     The purpose of this method is to refactor code and prevent similar code accross the modules.
     When calling this method, it takes a list as an argument
    """
    if len(items) == 0:
        message = {"message": "List is Empty"}
        return message
    else:
        return items


def get_chosen_item (index_label, item_index, items):
    """
     method to return the value of a dictionary item of 
     a given key value from the list of dictionaries.
     When calling this method, it takes three arguments, 
     that is: index label (key of the item that is being searched for, that is, sale_index, product_id, etc), 
     item_index (the actual value corresponding to the index_label),
      items ( a list of dictionaries from which a given item is wanted)
    """

    for item in items:   
        if item.get("{0}".format(index_label)) == item_index:
            return item

def create_id(items):
    user_id = random.randint(1, 1000)
    if check_item_in_list("user_id", user_id, items):
        create_id (items)
    else:
        return user_id
    
    