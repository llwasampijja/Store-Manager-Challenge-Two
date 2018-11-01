def valid_product(request_object):
    if "product_name" in request_object and "unit_price" in request_object and\
        "category_name" in request_object and "quantity" in request_object and \
        "acceptable_minimum" in request_object:
        return True
    else:
        return False

def product_not_in_db(request_object, products_list):
    req_product_name = request_object.get("product_name")
    if any(req_product_name == item.get("product_name") for item in products_list):
        return False
    else:
        return True

def product_available(request_object, data_base_products):
    product_name_to_add = request_object.get("product_name")
    product_name_available = data_base_products.get("product_name")
    if product_name_available == product_name_to_add:
        return True
    else:
        return False

def invalid_user(request_object):
    if "user_name" in request_object and "username" in request_object and \
        "password" in request_object and "user_role" in request_object :
        return False
    else:
        return True

def invalid_sale (request_object):
    if "product_name" in request_object and \
        "unit_price" in request_object and "category_name" in request_object and \
        "sale_made_by" in request_object:
        return False
    else:
        return True

def check_item_in_list(index_label, item_index, items):
    if any(item.get("{0}".format(index_label)) == item_index for item in items):
        return True
    else:
        return False

#def edit