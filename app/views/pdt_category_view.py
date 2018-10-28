from flask import Response, request, Blueprint
import json
from app.models.pdt_category_model import PdtCategory

pdt_category_bp = Blueprint("pdt_category", __name__)

pdt_category_obj= PdtCategory()
pdt_categories = pdt_category_obj.get_all_categories()

@pdt_category_bp.route("/categories", methods=["GET"])
def get_all_product_categories():
    response = Response(json.dumps(pdt_categories), content_type="application/json", status=200)
    return response

@pdt_category_bp.route("/categories/<int:category_id>", methods=["GET"])
def get_category(category_id):
    pass