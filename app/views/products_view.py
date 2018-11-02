"""
This module includes the routes for the endpoints relating to products
"""
from app.models.products import Products
from flask import request, Response, Blueprint
from app.utilities import admin_authorised, admin_and_attendant, doesnt_exist
from app.validity_check import valid_product, product_not_in_db
from app.store_managerdb import DatabaseConnect
import json
import uuid
import datetime

products_bp = Blueprint("products", __name__)
products_obj = Products()
# products = products_obj.get_all_products()

database_connect_obj = DatabaseConnect()


@products_bp.route('/products', methods=['GET'])
@admin_and_attendant
def get_products():
    """This is the route for the endpoint for viewing all the products.
     It's accessible to both admin and the store attendants"""
    # data_from_db = database_connect_obj.get_data_products()
    # dict_product = {}
    list_products = get_all_items()
    response = Response(json.dumps(list_products), content_type="application/json", status=200) 
    return response

# GET a product by its id
@products_bp.route('/products/<int:product_id>' , methods=['GET'])
@admin_and_attendant
def get_a_product(product_id):
    """
    This route is for the endpoint for getting a product by its id. It is also accessible to 
    both admin and the store attendants.
    """
    if not is_valid_id(product_id):
        return not_valid_response(product_id)

    data_from_db = database_connect_obj.get_data_product_byid(product_id)
    result = database_connect_obj.get_data_category_byid(data_from_db[5])
    print(result[1])
    dict_product = {
            "product_id": data_from_db[0],
            "product_name": data_from_db[1],
            "unit_price": data_from_db[2],
            "category": result[1],
            "stock_date": str(data_from_db[4]),
            "quantity": data_from_db[6],
            "acceptable_minimum": data_from_db[3]
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
    not_valid_product(request_data)

    product_name = request_data.get("product_name")
    unit_price = request_data.get("unit_price")
    acceptable_minimum = request_data.get("acceptable_minimum")
    stock_date = datetime.datetime.now()
    quantity = request_data.get("quantity")
    category_name = request_data.get("category_name")

    if not products_obj.check_empty_fields(product_name, unit_price, category_name, quantity, \
    acceptable_minimum):
        message = {"Message": "No empty fields allowed"}
        return Response(json.dumps(message), content_type="application/json", status=201)

    if not products_obj.correct_type(product_name, unit_price, category_name, quantity, acceptable_minimum):
        message = {"Message": "Entered a wrong type"}
        return Response(json.dumps(message), content_type="application/json", status=201)

    returned_category= list(database_connect_obj.category_exist_not(category_name))
    returned_product = list(database_connect_obj.product_exist_not(product_name))
    print(len(request_data))
    if len(returned_category)==0:
        return doesnt_exist()
    else:
        if len(returned_product)==0:
            database_connect_obj.insert_data_products(product_name, unit_price, quantity, \
            category_name, acceptable_minimum, stock_date)
            list_products = get_all_items()
            response = Response(json.dumps(list_products), content_type="application/json", status=202)
            return response
        else:
            message = {"Message:": "Product Already Exists"}
            response = Response (json.dumps(message), content_type="application/json", status=201)
            return response

    # category_id = database_connect_obj.get_id_categories("food")

    database_connect_obj.insert_data_products(product_name, unit_price, quantity, category_name, \
    acceptable_minimum, stock_date)
    list_products = get_all_items()
    response = Response(json.dumps(list_products), content_type="application/json", status=202)
    return response

@products_bp.route("/products/<int:product_id>", methods=["PUT"])
@admin_authorised 
def update_product(product_id):
    if not is_valid_id(product_id):
        return not_valid_response(product_id)

    request_data = request.get_json()
    product_name = request_data.get("product_name")
    unit_price = request_data.get("unit_price")
    minimum_quantity = request_data.get("minimum_quantity")
    stock_date = datetime.datetime.now()
    quantity = request_data.get("quantity")
    category_name = request_data.get("category_name")


    if products_obj.check_empty_fields(product_name, unit_price, category_name, quantity, \
    minimum_quantity):
        message = {"Message": "No empty fields allowed"}
        return Response(json.dumps(message), content_type="application/json", status=201)

    if not products_obj.correct_type(product_name, unit_price, category_name, quantity, minimum_quantity):
        message = {"Message": "Entered a wrong type"}
        return Response(json.dumps(message), content_type="application/json", status=201)

    returned_product = list(database_connect_obj.product_exist_not(product_name))

    if len(returned_product)==0:
        database_connect_obj.update_data_product(product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category_name, product_id)
        list_products = get_all_items()
        response = Response(json.dumps(list_products), content_type="application/json", status=202)
        return response
    else:
        message = {"Message:": "Product Already Exists"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

    

@products_bp.route("/products/<int:product_id>", methods=["DELETE"])
@admin_authorised 
def delete_product(product_id):
    if is_valid_id(product_id):
        database_connect_obj.delete_data_product(product_id)
        list_products = get_all_items()
        response = Response(json.dumps(list_products), content_type="application/json", status=200)
        return response
    else:
        return doesnt_exist()
            
def get_all_items():
    data_from_db = database_connect_obj.get_data_products()
    dict_product = {}
    list_products = []
    for product in data_from_db:
        result = database_connect_obj.get_data_category_byid(product[5])
        
        dict_product = {
            "product_id": product[0],
            "product_name": product[1],
            "unit_price": product[2],
            "category": str(result[1]),
            "stock_date": str(product[4]),
            "quantity": product[6],
            "acceptable_minimum": product[3]
        }
        list_products.append(dict_product)
    return list_products

def is_valid_id(product_id):
    returned_product = list(database_connect_obj.product_id_invalid())
    ids = []
    for item in returned_product:
        ids.append(item[0])
    # print(returned_product)
    if product_id in ids: 
        return True
    else:
        return False



def not_valid_response(product_id):
    if not is_valid_id(product_id):
        return doesnt_exist()

def not_valid_product(request_data):
    if not valid_product(request_data):
        message = {"Message": "Invalid product"}
        return Response(json.dumps(message), content_type="application/json", status=201)