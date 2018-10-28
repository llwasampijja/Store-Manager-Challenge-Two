from flask import Blueprint, Response, request, session
from app.utilities import create_id
from app.models.store_attendant_model import StoreAttendant
import json
login_logout_bp = Blueprint("login_logout,", __name__)

store_attendants_obj = StoreAttendant()
all_store_attendants = store_attendants_obj.get_all_store_attendants()

@login_logout_bp.route("/", methods=["Get"])
def home():
    if "username" in session:
        return Response(json.dumps({"message": "Logged in"}), content_type="application/json", status=202)
    return Response(json.dumps({"message": "not logged in"}), content_type="application/json", status=202) 

@login_logout_bp.route("/auth/login", methods=["GET", "POST"])
def login_user():
    request_data = request.get_json()
    user_name = request_data.get("username")
    user_password = request_data.get("password")
    session[user_name] = True
    return home()

@login_logout_bp.route("/auth/signup", methods=["POST"])
def signup_user():
    request_data = request.get_json()
    user_id = create_id(all_store_attendants)
    request_data.update({"user_id": user_id})
    all_store_attendants.append(request_data)
    response = Response (json.dumps(all_store_attendants), content_type="application/json", status=201)
    return response

