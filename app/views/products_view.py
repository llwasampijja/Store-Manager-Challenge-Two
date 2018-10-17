from app.models.products import Products
from flask import Flask, jsonify
from app.utilities import bp

app = Flask(__name__)
products_list = Products()
#get all products  
@bp.route('/products', methods=['GET'])    
def get_products():   
    products_list = Products()
    return jsonify(products_list.get_all_products())

#add product
@bp.route('/products/add', methods=['POST'])    
def add_product():   
    products_list = Products()
    return jsonify(products_list.admin_add_product())


# GET a product by its id
@bp.route('/products/<int:product_id>' , methods=['GET'])
def get_a_product(product_id):
    return jsonify(products_list.get_a_product(product_id))





# if __name__ == "__main__":
#     appl.run(port=5000)
