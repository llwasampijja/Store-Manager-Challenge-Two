from flask import Blueprint, Response, request, session
import json
login_logout_bp = Blueprint("login_logout,", __name__)

@login_logout_bp.route("/", methods=["Get"])
def home():
    if "username" in session:
        return Response(json.dumps({"message": "Logged in"}), content_type="application/json", status=202)
    return Response(json.dumps({"message": "not logged in"}), content_type="application/json", status=202) 

@login_logout_bp.route("/login", methods=["GET", "POST"])
def login_user():
    request_data = request.get_json()
    user_name = request_data.get("username")
    user_password = request_data.get("password")
    session[user_name] = True
    return home()