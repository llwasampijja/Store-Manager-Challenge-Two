"""
This module includes routes to endpoints which are concerned with sales.
"""
from app.models.sales import Sales
from flask import Response, request, Blueprint
from app.utilities import admin_authorised, store_attendant_authorised, publisher_and_admin, doesnt_exist
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
# @admin_authorised
def get_a_sale(sale_id):
    """
    This route is for the endpoint for getting a sale by its sale_id or id.
    It is available to only the admin and the store attendant who carried out that sale
    """
    if not is_valid_id(sale_id):
        message = {"Message:": "There is no such sale record on the system"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        return response

    sales_data_from_db = list(database_connect_obj.get_data_sale_byid(sale_id))
    product_id = sales_data_from_db[1]
    products_data_from_db = database_connect_obj.get_data_product_byid(product_id)
    category_data_from_db = database_connect_obj.get_data_category_byid(sales_data_from_db[3])
    user_data_from_db = database_connect_obj.get_data_app_users_by_id(sales_data_from_db[7])[0]
    print("this iso: ", user_data_from_db)
    
    dict_sale = {
            "sale_id": sales_data_from_db[0],
            "product_name": products_data_from_db[1],
            "unit_price": products_data_from_db[2],
            "category": category_data_from_db[1],
            "sale_date": str(sales_data_from_db[4]),
            "sale_quantity": sales_data_from_db[5],
            "total_sale":  (products_data_from_db[2])*(sales_data_from_db[5]),
            "sale_made_by": user_data_from_db[0]
        }
    response = Response(json.dumps(dict_sale), content_type="application/json", status=200)
    return response

@sales_bp.route('/sales', methods=['POST'])  
# @store_attendant_authorised  
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
    # sale_made_by = request_data.get("sale_made_by")
    sale_made_by = database_connect_obj.get_logged_in_users( "jetli")[0]
    
    # print("This is ut: ", quantity_instock[0])

    returned_product = list(database_connect_obj.product_exist_not(product_name))
    returned_category= list(database_connect_obj.category_exist_not(category_name))
    print(len(request_data))
    if len(returned_category)==0:
        return doesnt_exist()
    else:
        if len(returned_product)==0:
            message = {"Message:": "There is no such product in the database"}
            response = Response (json.dumps(message), content_type="application/json", status=201)
            return response
        else:
            quantity_instock = database_connect_obj.get_product_quantity(product_name)[0]
            if quantity_instock[0] < sale_quantity:
                message = {"Message:": "Not Enough Products in Stock"}
                response = Response (json.dumps(message), content_type="application/json", status=201)
                return response
            else:
                new_quantity = quantity_instock[0] - sale_quantity
                database_connect_obj.update_data_product_quantity(new_quantity, product_name)
                database_connect_obj.insert_data_sales(product_name, unit_price, category_name, sale_date,\
                category_name, sale_quantity, total_sale, sale_made_by[0])
                list_products = get_database_sales()
                response = Response(json.dumps(list_products), content_type="application/json", status=202)
                return response

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
        data_from_db = database_connect_obj.get_data_product_byid(x[1])
        result = database_connect_obj.get_data_category_byid(data_from_db[5])
        returned_user = database_connect_obj.get_data_app_users_by_id(x[7])[0]
        print(returned_user[0])
        dict_product = {
            "product_id": data_from_db[0],
            "product_name": data_from_db[1],
            "unit_price": data_from_db[2],
            "category": result[1],
            "stock_date": str(data_from_db[4]),
            "quantity": data_from_db[6],
            "acceptable_minimum": data_from_db[3]
        }



        dict_sale = {
        "sale_id": x[0],
        "product_name": dict_product.get("product_name"),
        "unit_price": dict_product.get("unit_price"),
        "category": dict_product.get("category"),
        "sale_date": str(x[4]),
        "sale_quantity": x[5],
        "total_sale": (x[5])*(dict_product.get("unit_price")),
        "sale_made_by": returned_user[0]
        }
        list_sales.append(dict_sale)
    return list_sales

def not_valid_sale(request_data):
    if invalid_sale(request_data):
        message = {"Message": "Invalid Sale"}
        return Response(json.dumps(message), content_type="application/json", status=201)

def is_valid_id(sale_id):
    returned_product = list(database_connect_obj.sale_id_invalid())
    ids = []
    for item in returned_product:
        ids.append((item[0]))
    print(ids[0])
    if sale_id in ids: 
        return True
    else:
        return False