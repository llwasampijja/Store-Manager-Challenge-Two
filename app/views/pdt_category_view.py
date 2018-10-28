from flask import Response, request, Blueprint
import json
from app.models.pdt_category_model import PdtCategory
from app.utilities import create_id

pdt_category_bp = Blueprint("pdt_category", __name__)

pdt_category_obj= PdtCategory()
pdt_categories = pdt_category_obj.get_all_categories()

@pdt_category_bp.route("/categories", methods=["GET"])
def get_all_product_categories():
    response = Response(json.dumps(pdt_categories), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/<int:category_id>", methods=["GET"])
def get_category(category_id):
    response = Response(json.dumps(pdt_category_obj.get_category_by_id(category_id)), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/add", methods=["POST"])
def add_category():
    request_data = request.get_json()
    pdt_category_id = create_id(pdt_categories)
    request_data.update({"pdt_category_id":pdt_category_id})
    pdt_categories.append(request_data)
    response = Response(json.dumps(pdt_categories), content_type="application/json", status=200)
    return response