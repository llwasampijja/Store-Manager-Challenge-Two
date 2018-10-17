#add github pivotal integration
products = [
    {
        "product-name": "Tumpeco",
        "unit-price": 500,
        "category": "Utencils",
        "stock-date": "11/12/2018",
        "quantity": 50,
        "acceptable-minimum": 10
    },
    {
        "product-name": "1 Dozen Spoons",
        "unit-price": 10000,
        "category": "Utencils",
        "stock-date": "11/11/2018",
        "quantity": 12,
        "acceptable-minimum": 2
    },
    {
        "product-name": "500g Noodles Packet",
        "unit-price": 1000,
        "category": "food",
        "stock-date": "12/12/2018",
        "quantity": 100,
        "acceptable-minimum": 20
    },
    {
        "product-name": "Smirnoff Black",
        "unit-price": 3500,
        "category": "alcohol",
        "stock-date": "11/24/2018",
        "quantity": 250,
        "acceptable-minimum": 50
    },
    {
        "product-name": "1 Liter Soda",
        "unit-price": 2000,
        "category": "Utencils",
        "stock-date": "11/12/2018",
        "quantity": 288,
        "acceptable-minimum": 72
    }
]

from flask import Flask, jsonify, request, Response, json
app = Flask(__name__)

# GET all products
@app.route('/products')
def get_products():
    return jsonify({'products': products})

app.run(port=5000)