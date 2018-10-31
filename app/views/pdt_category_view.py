from flask import Response, request, Blueprint
import json
from app.models.pdt_category_model import PdtCategory
from app.utilities import create_id
from app.store_managerdb import DatabaseConnect

pdt_category_bp = Blueprint("pdt_category", __name__)

pdt_category_obj= PdtCategory()
pdt_categories = pdt_category_obj.get_all_categories()
database_connect_obj = DatabaseConnect()

@pdt_category_bp.route("/categories", methods=["GET"])
def get_all_product_categories():
    list_categories = get_db_categories()
    response = Response(json.dumps(list_categories), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/<int:category_id>", methods=["GET"])
def get_category(category_id):
    data_from_db = database_connect_obj.get_data_category_byid(category_id)
    dict_category = {"product_id": data_from_db[0], "category_name": data_from_db[1]}
    response = Response(json.dumps(dict_category), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/add", methods=["POST"])
def add_category():
    request_data = request.get_json()

    category_name = request_data.get("category_name")
    database_connect_obj.insert_data_categories(category_name)
    pdt_categories.append(request_data)
    list_categories = get_db_categories()
    response = Response(json.dumps(list_categories), content_type="application/json", status=200)
    return response

def get_db_categories():
    data_from_db = database_connect_obj.get_data_categories()
    dict_category = {}
    list_categories = []
    for x in data_from_db:
        dict_category = {"product_id": x[0], "category_name": x[1]}
        list_categories.append(dict_category)

    return list_categories