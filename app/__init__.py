from flask import Flask
from app.views.sales_view import sales_bp
from app.views.products_view import products_bp


def create_app(debug=True):
    app =  Flask(__name__)
    app.register_blueprint(sales_bp, url_prefix='/api/v1')
    app.register_blueprint(products_bp, url_prefix='/api/v1')
    return app