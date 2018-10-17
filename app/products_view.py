from flask import Flask, jsonify, request, Response, json
from models.products import Products
app = Flask(__name__)

products_model = Products()

# GET all products
@app.route('/products')
def get_products():
    return jsonify({'products': products_model.get_all_products})

app.run(port=5000)