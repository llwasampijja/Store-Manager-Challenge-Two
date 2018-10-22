from app.models.products import Products
from flask import Flask, jsonify, request, Response
from app.utilities import blueprint, admin_authorised
import json

products_obj = Products()
products = products_obj.get_all_products()
    
@blueprint.route('/products', methods=['GET'])
def get_products():   
    return jsonify(products)

# GET a product by its id
@blueprint.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    return jsonify(products_obj.get_product_by_id(product_id))


@blueprint.route('/products/add', methods=['POST'])
@admin_authorised    
def add_product():
    request_data = request.get_json()

    product_id = request_data["product_id"]
    product_name = request_data["product_name"]
    unit_price = request_data["unit_price"]
    category = request_data["category"]
    stock_date = request_data["stock_date"]
    quantity = request_data["stock_date"]
    acceptable_minimum = request_data["acceptable_minimum"]

    # if(isinstance(product_id, int))
    # products.append(request_data)
    response = Response(json.dumps(products))
    return response
