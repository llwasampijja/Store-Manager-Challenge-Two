"""
This module includes the routes for the endpoints relating to products
"""
from app.models.products import Products
from flask import request, Response, Blueprint
from app.utilities import admin_authorised
from app.validity_check import valid_product, product_not_in_db
from app.store_managerdb import DatabaseConnect
import json
import uuid

products_bp = Blueprint("products", __name__)
products_obj = Products()
products = products_obj.get_all_products()

database_connect_obj = DatabaseConnect()


@products_bp.route('/products', methods=['GET'])
def get_products():
    """This is the route for the endpoint for viewing all the products.
     It's accessible to both admin and the store attendants"""
    data_from_db = database_connect_obj.get_data_products()
    dict_product = {}
    list_products = []
    for product in data_from_db:
        dict_product = {
            "product_id": product[0],
            "product_name": product[1],
            "unit_price": product[2],
            "category": product[3],
            "stock_date": str(product[4]),
            "quantity": product[5],
            "acceptable_minimum": product[6]
        }
        list_products.append(dict_product)
    response = Response(json.dumps(list_products), content_type="application/json", status=200) 
    return response

# GET a product by its id
@products_bp.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    """
    This route is for the endpoint for getting a product by its id. It is also accessible to 
    both admin and the store attendants.
    """
    data_from_db = database_connect_obj.get_data_product_byid(product_id)
    dict_product = {
            "product_id": data_from_db[0],
            "product_name": data_from_db[1],
            "unit_price": data_from_db[2],
            "category": data_from_db[3],
            "stock_date": str(data_from_db[4]),
            "quantity": data_from_db[5],
            "acceptable_minimum": data_from_db[6]
        }
    response = Response(json.dumps(dict_product), content_type="application/json", status=200)
    return response


@products_bp.route('/products/add', methods=['POST'])
# @admin_authorised    
def add_product():
    """
    This route is for the endpoint for adding a product. It is only accessible to admins
    """
    # product_id = uuid.uuid1()
    request_data = request.get_json()
    product_name = request_data.get("product_name")
    unit_price = request_data.get("unit_price")
    minimum_quantity = request_data.get("minimum_quantity")
    stock_date = request_data.get("stock_date")
    quantity = request_data.get("quantity")
    category_name = request_data.get("category_name")

    # category_id = database_connect_obj.get_id_categories("food")

    database_connect_obj.insert_data_products(product_name, unit_price, minimum_quantity, \
    stock_date, quantity, category_name)


    # request_data.update({"product_id": product_id.int})
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

@products_bp.route("/products/update/<int:product_id>", methods=["PUT"])
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
        if product.get("product_id") == product_id:
            product.update(updated_product)

    response = Response(json.dumps(products), content_type="application/json", status=202)
    return response

@products_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    database_connect_obj.delete_data_product(product_id)
    for product in products:
        if product_id == product.get("product_id"):
            products.remove(product)
    response = Response(json.dumps(products), content_type="application/json", status=200)
    return response
            
