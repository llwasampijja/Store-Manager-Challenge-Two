from flask import Flask, Blueprint, jsonify
from app.models.sales import Sales
from app.views.sales_view import get_sales
from app.views.products_view import get_products
from .utilities import blueprint
from .landing_page import webpage
import os

def create_app(config_filename):
    app = Flask(__name__)
    # app.register_blueprint(get_sales)
    return app


app = Flask(__name__)
# Landing Page
@blueprint.route("/", methods=["GET"])
def index():
    return webpage

app.register_blueprint(blueprint, url_prefix='/api/v1')