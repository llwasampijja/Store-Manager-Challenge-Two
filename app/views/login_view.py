from flask import Blueprint, Response, request, session
# from app.utilities import create_id, is_json
# from app.models.store_attendant_model import StoreAttendant
from app.utilities import admin_authorised, admin_and_attendant
from app.store_managerdb import DatabaseConnect
from app.models.app_user import AppUser
from app.validity_check import invalid_user
import os
import json
import base64
import datetime
import hashlib


from flask_jwt_extended import (
    JWTManager, verify_jwt_in_request, create_access_token,
    get_jwt_claims, jwt_required
)

login_bp = Blueprint("login_logout,", __name__)

app_user_obj = AppUser()
# all_store_attendants = store_attendants_obj.get_all_store_attendants()
database_connect_obj = DatabaseConnect()


@login_bp.route("/", methods=["Get"])
# @admin_and_attendant
def home():
    if "username" in session:
        return Response(json.dumps({"message": "Logged in"}), content_type="application/json", status=202)
    return Response(json.dumps({"message": "not logged in"}), content_type="application/json", status=202) 

@login_bp.route("/auth/login", methods=["GET", "POST"])
def login_user():
    request_data = request.get_json()
    username = request_data.get("username")
    user_password = request_data.get("password")
    hashed_password = hashlib.sha224(b"{}").hexdigest().format(user_password)
    returned_user = database_connect_obj.verify_userlogin(username)
    print("returned user:", returned_user)


    if len(returned_user)==0:
        message = {"Message:": "User Not registered on the system"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response
    else:
        user_name = returned_user[1]
        user_role = returned_user[4]
        if username == returned_user[2] and hashed_password == returned_user[3]:
            print(returned_user[4])
            user_account_details = {"user_id": returned_user[0], "name": returned_user[1], "username": returned_user[2], "role": returned_user[4]}
            acess_token  = create_access_token(identity = user_account_details, \
            expires_delta=datetime.timedelta(days=30))
            response = Response(json.dumps({"acess_token": acess_token}), content_type="application/json",\
             status=202)
            message = {"Message:": "Login was successiful", "Access Token: ": acess_token, "Username:": username,\
            "Name ": user_name, "User Role": user_role,  "Password": hashed_password}
            response = Response (json.dumps(message), content_type="application/json", status=201)
            return response
        else:
            message = {"Message:": "Entered wrong password"}
            response = Response (json.dumps(message), content_type="application/json", status=401)
            return response

@login_bp.route("/auth/signup", methods=["POST"])
@admin_authorised
def signup_user():
    request_data = request.get_json()
    user_name = request_data.get("user_name")
    username = request_data.get("username")
    password = request_data.get("password")
    hashed_password = hashlib.sha224(b"{}").hexdigest().format(password)
    user_role = request_data.get("user_role")

    if invalid_user(request_data):
        message = {"Message:": "Invalid input details"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

    if not app_user_obj.check_empty_fields(user_name,  username, password, \
        user_role):
        message = {"Message": "No empty fields allowed"}
        return Response(json.dumps(message), content_type="application/json", status=406)

    if not app_user_obj.correct_data_type(user_name, username, password, user_role):
        message = {"Message": "No empty fields allowed"}
        return Response(json.dumps(message), content_type="application/json", status=406)

    returned_user = list(database_connect_obj.user_exist_not(username))
    if not app_user_obj.check_role(user_role):
        message = {"Message:": "Entered a non-existant role"}
        response = Response (json.dumps(message), content_type="application/json", status=404)
        return response

    if len(returned_user)==0:
        message = {"Message:": "User Successifully Added", "Username:": username,\
         "Name ": user_name, "User Role": user_role,  "Password": hashed_password}
        database_connect_obj.insert_data_users(user_name, username, hashed_password, user_role)
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response
    else:
        message = {"Message:": "The User Already Exists"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

