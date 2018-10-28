from flask import Blueprint, Response, request
from app.models.store_attendant_model import StoreAttendant
from app.utilities import create_id
import json

store_attendants_bp = Blueprint("storeattendants", __name__)

store_attendants_obj = StoreAttendant()
all_store_attendants = store_attendants_obj.get_all_store_attendants()

@store_attendants_bp.route('/storeattendants', methods=['GET'])
def get_store_attendants():
    response = Response(json.dumps(all_store_attendants), content_type="application/json", status=200)
    return response

@store_attendants_bp.route('/storeattendants/add', methods=['POST'])
def add_storeattendants():
    request_data = request.get_json()
    user_id = create_id(all_store_attendants)
    request_data.update({"user_id": user_id})
    all_store_attendants.append(request_data)
    response = Response (json.dumps(all_store_attendants), content_type="application/json", status=201)
    return response

@store_attendants_bp.route('/storeattendants/<int:user_id>', methods=['GET'])
def get_storeattendant(user_id):
    response = Response(json.dumps(store_attendants_obj.get_user_by_id(user_id)), content_type="application/json", status=200)
    return response

