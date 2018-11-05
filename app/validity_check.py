def valid_product(request_object):
    if "product_name" in request_object and "unit_price" in request_object and\
        "category_name" in request_object and "quantity" in request_object and \
        "acceptable_minimum" in request_object:
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
        "unit_price" in request_object and "category_name" in request_object:
        return False
    else:
        return True