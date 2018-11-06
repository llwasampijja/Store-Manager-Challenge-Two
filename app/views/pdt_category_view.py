from flask import Response, request, Blueprint
import json
from app.models.pdt_category_model import PdtCategory
from app.store_managerdb import DatabaseConnect
from app.utilities import admin_authorised
from app.validity_check import empty_category, wrong_type_category

pdt_category_bp = Blueprint("pdt_category", __name__)

pdt_category_obj= PdtCategory()
# pdt_categories = pdt_category_obj.get_all_categories()
database_connect_obj = DatabaseConnect()

@pdt_category_bp.route("/categories", methods=["GET"])
def get_all_product_categories():
    list_categories = get_db_categories()
    print("Thop aru thu catugiroup:", list_categories)
    response = Response(json.dumps(list_categories), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/<int:category_id>", methods=["GET"])
def get_category(category_id):
    data_from_db = database_connect_obj.get_data_category_byid(category_id)
    dict_category = {"product_id": data_from_db[0], "category_name": data_from_db[1]}
    response = Response(json.dumps(dict_category), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories", methods=["POST"])
@admin_authorised
def add_category():
    request_data = request.get_json()
    category_name = request_data.get("category_name")
    returned_category= list(database_connect_obj.category_exist_not(category_name))

    if empty_category(category_name) or wrong_type_category(category_name):
        message = {"Message:": "Data type entered not allowed"}
        database_connect_obj.insert_data_categories(category_name)
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

    if len(returned_category)==0:
        message = {"Message:": "Category Successifully Added"}
        database_connect_obj.insert_data_categories(category_name)
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response
    else:
        message = {"Message:": "Category Already Exists"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

def get_db_categories():
    data_from_db = database_connect_obj.get_data_categories()
    dict_category = {}
    list_categories = []
    for x in data_from_db:
        dict_category = {"product_id": x[0], "category_name": x[1]}
        list_categories.append(dict_category)

    return list_categories