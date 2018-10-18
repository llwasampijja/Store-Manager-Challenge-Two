from flask import Flask, Blueprint, jsonify
from app.models.sales import Sales
from app.views.sales_view import get_sales
from .utilities import bp, endpoints_list
import os

def create_app(config_filename):
    app = Flask(__name__)
    app.register_blueprint(get_sales)

    # beginning of tests

    if config_filename is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(config_filename)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ending of test
    return app


app = Flask(__name__)
# Landing Page
@app.route("/", methods=["GET"])
def index():
    return endpoints_list

app.register_blueprint(bp, url_prefix='/api/v1')