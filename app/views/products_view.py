from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import blueprint, admin_authorised

app = Flask(__name__)
products_list = Products()
#get all products  
@blueprint.route('/products', methods=['GET'])    
def get_products():   
    products_list = Products()
    return jsonify(products_list.get_all_products())

#add product
@blueprint.route('/products/add', methods=['POST']) 
@admin_authorised   
def add_product():   
    products_list = Products()
    return jsonify(products_list.admin_add_product())


# GET a product by its id
@blueprint.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    return jsonify(products_list.get_a_product(product_id))