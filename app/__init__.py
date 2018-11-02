"""
This module serves two purposes. 
1-: It informs python that the folder in which it is located should be treated as a package.
2-: It contains the application factory.
"""
from flask import Flask
from app.views.sales_view import sales_bp
from app.views.products_view import products_bp
from app.views.pdt_category_view import pdt_category_bp
from app.views.login_view import login_bp
from flask_jwt_extended import  JWTManager, verify_jwt_in_request, create_access_token, get_jwt_claims
import os


def create_app(debug=True):
    """
    This is referred to as the application factory. It creates a single instance of 
    the flask app which is used accross the modules of the application.
    This is also where configulation takes place.
    The blue prints to the different routes are also registed to the app in this method.
    """
    app =  Flask(__name__)
    app.register_blueprint(sales_bp, url_prefix='/api/v1')
    app.register_blueprint(products_bp, url_prefix='/api/v1')
    app.register_blueprint(pdt_category_bp, url_prefix='/api/v1')
    app.register_blueprint(login_bp, url_prefix='/api/v1')
    app.secret_key = os.urandom(12)


    app.config['JWT_SECRET_KEY'] = app.secret_key
    jwt_manager = JWTManager()
    jwt_manager.init_app(app)
    return app