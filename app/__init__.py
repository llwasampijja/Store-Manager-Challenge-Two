from flask import Flask
from app.views.products_view import *
from .utilities import blueprint
from .landing_page import webpage

# Landing Page
@blueprint.route("/", methods=["GET"])
def index():
    return webpage

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/api/v1')