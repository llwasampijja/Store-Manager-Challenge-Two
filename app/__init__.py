from flask import Flask, Blueprint, jsonify
from app.models.sales import Sales
from app.views.sales_view import get_sales
from .utilities import bp, endpoints_list

def create_app(config_filename):
    app = Flask(__name__)
    app.register_blueprint(get_sales)
    return app


app = Flask(__name__)
# Landing Page
@app.route("/", methods=["GET"])
def index():
    return endpoints_list

app.register_blueprint(bp, url_prefix='/api/v1')