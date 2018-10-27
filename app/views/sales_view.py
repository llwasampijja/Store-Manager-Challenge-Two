"""
This module includes routes to endpoints which are concerned with sales.
"""
from app.models.sales import Sales
from flask import Response, request, Blueprint
from app.utilities import admin_authorised, store_attendant_authorised, publisher_and_admin
from app.validity_check import valid_sale
import json
import uuid

sales_bp = Blueprint('sales', __name__)
sales_records = Sales()
all_sales = sales_records.get_all_sales()

@sales_bp.route('/sales', methods=['GET'])
# @admin_authorised
def get_sales():
    """
    this is the route to the endpoint of getting all the sales made by the store attendants. 
    It is available to only the administrator
    """
    response = Response(json.dumps(sales_records.get_all_sales()), content_type="application/json", status=200) 
    return response

@sales_bp.route('/sales/<int:sale_index>' , methods=['GET'])
# @publisher_and_admin
def get_a_sale(sale_index):
    """
    This route is for the endpoint for getting a sale by its sale_index or id.
    It is available to only the admin and the store attendant who carried out that sale
    """
    response = Response(json.dumps(sales_records.get_single_sale(sale_index)), content_type="application/json", status=200)
    return response

@sales_bp.route('/sales/add', methods=['POST'])  
# @store_attendant_authorised  
def add_sale():
    """
    This route is for the endpoint for adding products in the inventory.
     It is available to only the admins
    """
    sale_index = uuid.uuid1()
    request_data = request.get_json()
    request_data.update({"sale_index": sale_index.int})
    if valid_sale(request_data):
        all_sales.append(request_data)
        response = Response(json.dumps(all_sales), content_type="application/json", status=202)
        return response
    else:
        message = {"Error": "The sale record is not valid"}
        response = Response(json.dumps(message), content_type="application/json", status=202)
        return response