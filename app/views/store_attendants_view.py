from flask import Blueprint, Response, request
from app.models.store_attendant_model import StoreAttendant
from app.utilities import create_id
from app.store_managerdb import DatabaseConnect
import json
import uuid

store_attendants_bp = Blueprint("storeattendants", __name__)

store_attendants_obj = StoreAttendant()
all_store_attendants = store_attendants_obj.get_all_store_attendants()
database_connect_obj = DatabaseConnect()

@store_attendants_bp.route('/storeattendants', methods=['GET'])
def get_store_attendants():
    response = Response(json.dumps(all_store_attendants), content_type="application/json", status=200)
    return response

@store_attendants_bp.route('/storeattendants', methods=['POST'])
def add_storeattendants():
    
    request_data = request.get_json()
    # user_id = str(uuid.uuid1())
    name_store_attendant = request_data.get("user_name")
    username_store_attendant = request_data.get("username")
    password_store_attendant = request_data.get("password")
    user_role_store_attendant = request_data.get("user_role")
    # request_data.update({"user_id": user_id})
    all_store_attendants.append(request_data)
    database_connect_obj.insert_data_users(name_store_attendant,\
    username_store_attendant, password_store_attendant, user_role_store_attendant)
    response = Response (json.dumps(all_store_attendants), content_type="application/json", status=201)
    return response

@store_attendants_bp.route('/storeattendants/<int:user_id>', methods=['GET'])
def get_storeattendant(user_id):
    response = Response(json.dumps(store_attendants_obj.get_user_by_id(user_id)),\
     content_type="application/json", status=200)
    return response

