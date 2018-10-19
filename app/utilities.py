from flask import Blueprint
blueprint = Blueprint('api', __name__)
users_credentials = [
    {
        "username": "admin",
        "password":"admin"
    },
    {
        "username": "attendant",
        "password": "password"
    }]
    
endpoints_list = """
<h2>Store Manager Challenge Two</h2>
               <li><a href='/api/v1/products/4'>Find a Product Product with id 4</a></li>
"""