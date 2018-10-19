from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import bp

app = Flask(__name__)
    
@bp.route('/products', methods=['GET'])    
def get_products():   
    return jsonify(products_list.get_all_products())


@bp.route('/products/add', methods=['POST'])    
def add_product():   
    return jsonify(products_list.admin_add_product())


# appl = Flask(__name__)

# products_model = Products()

# GET all products





# if __name__ == "__main__":
#     appl.run(port=5000)
