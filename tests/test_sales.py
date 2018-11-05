"""
This module is for unit tests of methods in  the sales.py 
module as well as those in sales_views.py module
"""

import unittest
import json
from flask import Response
from app import create_app
from app.utilities import user_role, author
from app.models.sales import Sales
# from flask_jwt_extended import  JWTManager, verify_jwt_in_request, create_access_token, \
# get_jwt_claims, get_jwt_identity
from config import env_config, runtime_mode
from app.utilities import create_admin_user


class TestSales(unittest.TestCase):

    def setUp(self):
        """
        Declare and initialize the variables
        """
        self.app = create_app(env_config.get("{}".format(runtime_mode)))
        self.sales_obj = Sales()
        self.client = self.app.test_client(self)

    def test_get_sales(self):
        """Unit test for method get_sales"""
        pass
        

    def test_get_a_sale(self):
        """Unit test for method get_a_sale """
        pass

    def is_sale_avaialble(self, sale_id):
        """" Check if a sale record in the sales list. This method is used to create a unit \
        test for sale not available."""
        pass

    def test_add_sale(self):
        """Unit test for add_sale method"""
        pass