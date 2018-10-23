from flask import Flask, Blueprint, jsonify
<<<<<<< HEAD
from .utilities import bp, endpoints_list
import os

def create_app(config_filename):
    app = Flask(__name__)
    return app

app = Flask(__name__)
# Landing Page
@bp.route("/", methods=["GET"])
def index():
    return endpoints_list

app.register_blueprint(bp, url_prefix='/api/v1')
=======
# from app.models.sales import Sales
from app.views.sales_view import get_sales
from app.views.products_view import get_products
from .utilities import blueprint
from .landing_page import webpage


# Landing Page
@blueprint.route("/", methods=["GET"])
def index():
    return webpage

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/api/v1')
>>>>>>> feature
