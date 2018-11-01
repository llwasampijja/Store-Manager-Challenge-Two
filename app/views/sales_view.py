"""
This module includes routes to endpoints which are concerned with sales.
"""
from app.models.sales import Sales
from flask import Response, request, Blueprint
from app.utilities import admin_authorised, store_attendant_authorised, publisher_and_admin
from app.validity_check import invalid_sale
from app.store_managerdb import DatabaseConnect
from app.models.sales import Sales
import json
import datetime

sales_bp = Blueprint('sales', __name__)
sales_obj = Sales()
database_connect_obj = DatabaseConnect()

@sales_bp.route('/sales', methods=['GET'])
# @admin_authorised
def get_sales():
    """
    this is the route to the endpoint of getting all the sales made by the store attendants. 
    It is available to only the administrator
    """
    list_sales = get_database_sales()
    response = Response(json.dumps(list_sales), content_type="application/json", status=200) 
    return response

@sales_bp.route('/sales/<int:sale_id>' , methods=['GET'])
@admin_authorised
def get_a_sale(sale_id):
    """
    This route is for the endpoint for getting a sale by its sale_id or id.
    It is available to only the admin and the store attendant who carried out that sale
    """
    data_from_db = database_connect_obj.get_data_sale_byid(sale_id)
    dict_sale = {
            "sale_id": data_from_db[0],
            "product_name": data_from_db[1],
            "unit_price": data_from_db[2],
            "category": data_from_db[3],
            "sale_date": str(data_from_db[4]),
            "sale_quantity": data_from_db[5],
            "total_sale": data_from_db[6],
            "sale_made_by": data_from_db[7]
        }
    response = Response(json.dumps(dict_sale), content_type="application/json", status=200)
    return response

@sales_bp.route('/sales', methods=['POST'])  
@store_attendant_authorised  
def add_sale():
    """
    This route is for the endpoint for adding products in the inventory.
     It is available to only the admins
    """
    # sale_id = uuid.uuid1()
    request_data = request.get_json()

    if invalid_sale(request_data):
        message = {"Message": "Invalid Sale"}
        return Response(json.dumps(message), content_type="application/json", status=201)

    

        
    product_name = request_data.get("product_name")
    unit_price = request_data.get("unit_price")
    category_name = request_data.get("category_name")
    sale_date = datetime.datetime.now()
    sale_quantity = request_data.get("sale_quantity")
    total_sale = unit_price * sale_quantity
    sale_made_by = request_data.get("sale_made_by")

    # if sales_obj.check_empty_fields(product_name, unit_price, category_name, \
    #     sale_quantity, sale_made_by):
    #     message = {"Message": "No empty fields allowed"}
    #     return Response(json.dumps(message), content_type="application/json", status=201)

    database_connect_obj.insert_data_sales(product_name, unit_price, category_name, sale_date, category_name,
        sale_quantity, total_sale, sale_made_by)

    list_sales = get_database_sales()
    response = Response(json.dumps(list_sales), content_type="application/json", status=200)
    return response

def get_database_sales():
    data_from_db = database_connect_obj.get_data_sales()
    list_sales = []
    for x in data_from_db:
        dict_sale = {
        "sale_id": x[0],
        "product_name": x[1],
        "unit_price": x[2],
        "category": x[3],
        "sale_date": str(x[4]),
        "sale_quantity": x[5],
        "total_sale": x[6],
        "sale_made_by": x[7]
        }
        list_sales.append(dict_sale)
    return list_sales

def not_valid_sale(request_data):
    if invalid_sale(request_data):
        message = {"Message": "Invalid Sale"}
        return Response(json.dumps(message), content_type="application/json", status=201)