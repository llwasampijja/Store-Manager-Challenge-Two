from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import blueprint

app = Flask(__name__)
    
@blueprint.route('/products', methods=['GET'])    
def get_products():   
    products_list = Products()
    return jsonify(products_list.get_all_products())


