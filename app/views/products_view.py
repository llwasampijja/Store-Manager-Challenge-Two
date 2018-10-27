"""
This module includes the routes for the endpoints relating to products
"""
from app.models.products import Products
from flask import request, Response, Blueprint
from app.utilities import admin_authorised
from app.validity_check import valid_product, product_not_in_db
import json
import uuid

products_bp = Blueprint("products", __name__)
products_obj = Products()
products = products_obj.get_all_products()
    
@products_bp.route('/products', methods=['GET'])
def get_products():
    """This is the route for the endpoint for viewing all the products.
     It's accessible to both admin and the store attendants"""
    response = Response(json.dumps(products), content_type="application/json", status=200) 
    return response

# GET a product by its id
@products_bp.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    """
    This route is for the endpoint for getting a product by its id. It is also accessible to 
    both admin and the store attendants.
    """
    response = Response(json.dumps(products_obj.get_product_by_id(product_id)), content_type="application/json", status=200)
    return response


@products_bp.route('/products/add', methods=['POST'])
# @admin_authorised    
def add_product():
    """
    This route is for the endpoint for adding a product. It is only accessible to admins
    """
    product_id = uuid.uuid1()
    request_data = request.get_json()
    request_data.update({"product_id": product_id.int})
    if valid_product (request_data):
        if product_not_in_db(request_data, products):
            products.append(request_data)
            response = Response(json.dumps(products), content_type="application/json", status=202)
            return response
        else:
            message = {"Status": "The product is already in the database"}
            response = Response(json.dumps(message), content_type="application/json", status=202)
            return response
    else:
        message = {"Error": "The product is not valid  or already in the database"}
        response = Response(json.dumps(message), content_type="application/json", status=202)
        return response