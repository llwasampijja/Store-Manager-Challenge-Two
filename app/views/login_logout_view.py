from flask import Blueprint, Response, request, session
from app.utilities import create_id
from app.models.store_attendant_model import StoreAttendant
from app.utilities import admin_authorised
from app.store_managerdb import DatabaseConnect
import os
import json
import base64
import datetime


from flask_jwt_extended import (
    JWTManager, verify_jwt_in_request, create_access_token,
    get_jwt_claims, jwt_required
)

login_logout_bp = Blueprint("login_logout,", __name__)

store_attendants_obj = StoreAttendant()
all_store_attendants = store_attendants_obj.get_all_store_attendants()
database_connect_obj = DatabaseConnect()


@login_logout_bp.route("/", methods=["Get"])
def home():
    if "username" in session:
        return Response(json.dumps({"message": "Logged in"}), content_type="application/json", status=202)
    return Response(json.dumps({"message": "not logged in"}), content_type="application/json", status=202) 

@login_logout_bp.route("/auth/login", methods=["GET", "POST"])
def login_user():
    request_data = request.get_json()
    username = request_data.get("username")
    user_password = request_data.get("password")
    returned_user = database_connect_obj.verify_userlogin(username)
    if len(returned_user)==0:
        message = {"Message:": "User Not registered on the system"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response
    else:
        if username == returned_user[2] and user_password == returned_user[3]:
            print(returned_user[4])
            acess_token  = create_access_token(identity = returned_user[4], expires_delta=datetime.timedelta(days=30))
            response = Response(json.dumps({"acess_token": acess_token}), content_type="application/json", status=202)
            message = {"Message:": "Login was successiful", "Access Token: ": acess_token}
            response = Response (json.dumps(message), content_type="application/json", status=201)
            return response
        else:
            message = {"Message:": "Entered wrong password"}
            response = Response (json.dumps(message), content_type="application/json", status=401)
            return response

@login_logout_bp.route("/auth/signup", methods=["POST"])
@admin_authorised
def signup_user():
    request_data = request.get_json()
    user_name = request_data.get("user_name")
    username = request_data.get("username")
    password = request_data.get("password")
    user_role = request_data.get("user_role")
    returned_user = list(database_connect_obj.user_exist_not(username))

    if len(returned_user)==0:
        message = {"Message:": "User Successifully Added"}
        database_connect_obj.insert_data_users(user_name, username, password, user_role)
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response
    else:
        message = {"Message:": "User User Already Exists"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

