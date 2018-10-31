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
import datetime

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
    list_products = get_all_items()
    # for product in data_from_db:
    #     dict_product = {
    #         "product_id": product[0],
    #         "product_name": product[1],
    #         "unit_price": product[2],
    #         "category": product[3],
    #         "stock_date": str(product[4]),
    #         "quantity": product[5],
    #         "acceptable_minimum": product[6]
    #     }
    #     list_products.append(dict_product)
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


@products_bp.route('/products', methods=['POST'])
@admin_authorised    
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
    list_products = get_all_items()
    response = Response(json.dumps(list_products), content_type="application/json", status=202)
    return response

@products_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    request_data = request.get_json()
    product_name = request_data.get("product_name")
    unit_price = request_data.get("unit_price")
    minimum_quantity = request_data.get("minimum_quantity")
    stock_date = request_data.get("stock_date")
    quantity = request_data.get("quantity")
    category_name = request_data.get("category_name")

    database_connect_obj.update_data_product(product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category_name, product_id)

    list_products = get_all_items()

    response = Response(json.dumps(list_products), content_type="application/json", status=202)
    return response

@products_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    database_connect_obj.delete_data_product(product_id)
    list_products = get_all_items()
    response = Response(json.dumps(list_products), content_type="application/json", status=200)
    return response
            
def get_all_items():
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
    return list_products