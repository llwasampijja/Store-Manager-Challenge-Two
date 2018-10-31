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

    # user_identity = json.dumps({"username": username, "role": "attendant"})
    acess_token  = create_access_token(identity = "admin", expires_delta=datetime.timedelta(days=1))
    response = Response(json.dumps({"acess_token": acess_token}), content_type="application/json", status=202)
    return response

@login_logout_bp.route("/auth/signup", methods=["POST"])
@admin_authorised
def signup_user():
    request_data = request.get_json()
    user_id = create_id(all_store_attendants)
    request_data.update({"user_id": user_id})
    all_store_attendants.append(request_data)
    response = Response (json.dumps(all_store_attendants), content_type="application/json", status=201)
    return response

