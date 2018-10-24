from app.models.products import Products
from flask import jsonify, request, Response, Blueprint
from app.utilities import admin_authorised
import json

products_bp = Blueprint("products", __name__)

products_obj = Products()
products = products_obj.get_all_products()
    
@products_bp.route('/products', methods=['GET'])
def get_products():   
    return jsonify(products)

# GET a product by its id
@products_bp.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    return jsonify(products_obj.get_product_by_id(product_id))


@products_bp.route('/products/add', methods=['POST'])
@admin_authorised    
def add_product():
    request_data = request.get_json()
    products.append(request_data)
    response = Response(json.dumps(products))
    return response

# PATCH /products/product_id
@products_bp.route('/products/<int:product_id>', methods=['PATCH'])
@admin_authorised    
def update_product(product_id):
    request_data = request.get_json()
    updated_product = {}

    if ("product_name" in request_data):
        updated_product["product_name"] = request_data["product_name"]

    if ("unit_price" in request_data):
        updated_product["unit_price"] = request_data["unit_price"]

    if ("category" in request_data):
        updated_product["category"] = request_data["category"]

    if ("stock_date" in request_data):
        updated_product["stock_date"] = request_data["stock_date"]

    if ("quantity" in request_data):
        updated_product["quantity"] = request_data["quantity"]

    if ("acceptable_minimum" in request_data):
        updated_product["acceptable_minimum"] = request_data["acceptable_minimum"]

    for product in products:
        if product["product_id"] == product_id:
            product.update(updated_product)

    response = Response(json.dumps(products))
    return response