"""
The utilities.py module includes constants and methods 
which can be called from any moddule within this application
"""
from flask import Response
from functools import wraps
from app.store_managerdb import DatabaseConnect
import json
# from app.validity_check import check_item_in_list
from flask_jwt_extended import  JWTManager, verify_jwt_in_request, create_access_token, \
get_jwt_claims, get_jwt_identity
import hashlib

database_connect = DatabaseConnect()

def store_attendant_authorised(fn):
    """
    This decorator is for restricting content to only be availble to store attendants
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_identity = get_jwt_identity()
        if user_identity["role"]  != 'attendant':
            message = {"msg":"This feature is available to only the store attendants!"}
            response = Response(json.dumps(message), content_type="application/json", status=401)
            return response
        else:
            return fn(*args, **kwargs)
    return wrapper

def admin_and_attendant(fn):
    """
    This decorator is for restricting content to only be availble to store attendants
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_identity = get_jwt_identity()
        if user_identity["role"] == "admin" or user_identity["role"] == "attendant":
            return fn(*args, **kwargs)
        else:
            message = {"msg":"This feature is available to only the store attendants!"}
            response = Response(json.dumps(message), content_type="application/json", status=401)
            return response
    return wrapper

# def publisher_and_admin(fn):
#     """
#     This docorator is for granting access to content which is
#      only available to admins as well as the authors of the content.
#     """
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         user_identity = get_jwt_identity()
#         # if user_identity["role"] == "admin":
#         if config.author == True:
#             return fn(*args, **kwargs)
#         else:
#             message = {"msg":"This feature is available to only the admin and the individual who created it!"}
#             response = Response(json.dumps(message), content_type="application/json", status=403)
#             return response
#     return wrapper

def admin_authorised(fn):
    """
    This decorator is for restricting content to only be accessed by admins
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_identity = get_jwt_identity()
        if user_identity["role"] == 'admin':
            return fn(*args, **kwargs)
        else:
            message = {"msg":"This feature is available to only the Admins"}
            response = Response(json.dumps(message), content_type="application/json", status=401)
            return response
    return wrapper

def create_admin_user():
    user_name = "Edward Army"
    username = "edward"
    password = "myname"
    hashed_password = hashlib.sha224(b"{}").hexdigest().format(password)
    user_role = "admin"
    returned_user = list(database_connect.user_exist_not(username))

    if len(returned_user)==0:
        database_connect.insert_data_users(user_name, username, hashed_password, user_role)
    else:
        pass

def doesnt_exist():
    message = {"Message:": "Product or Category does not exist"}
    response = Response (json.dumps(message), content_type="application/json", status=201)
    return response
    
    