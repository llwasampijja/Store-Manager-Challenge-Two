from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import bp

app = Flask(__name__)
    
@bp.route('/products', methods=['GET'])    
def get_products():   
    products_list = Products()
    return jsonify(products_list.get_all_products())


# appl = Flask(__name__)

# products_model = Products()

# GET all products





# if __name__ == "__main__":
#     appl.run(port=5000)
