from flask import Flask, Blueprint, jsonify
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