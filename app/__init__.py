from flask import Flask, Blueprint, jsonify
from app.models.products import Products
from app.views.products_view import *
from .utilities import blueprint, endpoints_list

def create_app(config_filename):
    app = Flask(__name__)
    app.register_blueprint(get_products)
    return app


app = Flask(__name__)
# Landing Page
@blueprint.route("/", methods=["GET"])
def index():
    return endpoints_list

app.register_blueprint(blueprint, url_prefix='/api/v1')