"""
This module is for unit tests of methods in  the products.py
module as well as those in product_views.py module
"""
import unittest
import json
from app import create_app
from app.models.products import Products
from config import env_config, runtime_mode
from app.utilities import create_admin_user


class TestProducts(unittest.TestCase):

    def setUp(self):
        """Declaration and initialization of variables"""

        self.app = create_app(env_config.get("{}".format(runtime_mode)))
        self.products_obj = Products()
        self.client = self.app.test_client(self)

    def test_get_all_products(self):
        """unit tests for the get_all_products() method"""
        pass

    def test_get_a_product(self):
        """unit tests for the get_a_product() method"""   
        pass

    def is_product_avaialble(self, product_id):
        """this method is to assist in doing a unit test in case a product is available or not"""
        pass

    def test_add_product(self):
        """Unit tests for the add_product method """
        pass
    