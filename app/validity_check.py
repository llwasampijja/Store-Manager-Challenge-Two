def check_empty_fields(user_name, username, password, user_role):
    if not user_name.strip() or not username.strip() or not password.strip() or not user_role.strip():
        return True
    else:
        return False

def correct_data_type(user_name, username, password, user_role):
    if isinstance(user_name, str) and isinstance(username, str) and isinstance(password, str) and isinstance(user_role, str):
        return True
    else:
        return False

def check_role(user_role):
    if user_role == "admin":
        return True
    elif user_role == "attendant":
        return True
    else:
        return False


def empty_category(category_name):
    if not category_name.strip():
        return True
    else:
        return False

def wrong_type_category(category_name):
    if not isinstance(category_name, str):
        return True
    else:
        return False 

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


def check_empty_fields_products(product_name, unit_price, category_name, quantity, acceptable_minimum):
    if not product_name.strip() or not unit_price or not category_name.strip() \
        or not quantity or not acceptable_minimum:
        return False
    else:
        return True

def correct_type_products(product_name, unit_price, category_name, quantity, acceptable_minimum):
    if isinstance(product_name, str) and isinstance(unit_price, int) and isinstance(category_name, str) \
        and isinstance(quantity, int) and isinstance(acceptable_minimum, int):
        return True
    else:
        return False

def check_empty_fields_sales(product_name, unit_price, category_name, \
    sale_quantity):
    if not product_name.strip() or not unit_price or not category_name.strip() or not sale_quantity:
        return True
    else:
        return False

def correct_type_sales(product_name, unit_price, category_name, \
    sale_quantity):
    if isinstance(product_name, str) and isinstance(unit_price, int) \
        and isinstance(category_name, str) and isinstance(sale_quantity, int):
        return True
    else:
        return False