"""
This module is for unit tests of methods in  the products.py
module as well as those in product_views.py module
"""
import unittest
import json
from app import create_app
from app.utilities import user_role, author
from app.models.products import Products
import os
from config import env_config, runtime_mode


class TestProducts(unittest.TestCase):

    def setUp(self):
        """
         Declaration and initialization of variables
        """

        self.app = create_app(env_config.get("{}".format(runtime_mode)))
        self.products_obj = Products()
        # self.products_list  = self.products_obj.products
        self.client = self.app.test_client(self)

    def test_get_all_products(self):
        """
        unit tests for the get_all_products() method
        """
        # http_response = self.client.get('api/v1/products')
        # self.assertEqual(http_response.status_code, 200)
        # self.assertNotEqual(http_response.status_code, 404)
        pass

    def test_get_a_product(self):
        """
        unit tests for the get_a_product() method
        """   
        # get_product_url = 'api/v1/products/{0}'.format(2)
        # http_response = self.client.get(get_product_url, content_type='application/json')
        # self.assertEqual(http_response.status_code, 200)
        # self.assertTrue(self.is_product_avaialble(2))
        pass

    def is_product_avaialble(self, product_id):
        """
        this method is to assist in doing a unit test in case a product is available or not
        """
        # if any(product_id == item.get("product_id") for item in self.products_list):
        #     return True
        # return False

    def test_add_product(self):
        """
        Unit tests for the add_product method 
        """
        product_new = {
            "product_id": "5",
            "product_name": "Nile Special",
            "unit_price": 4000,
            "category": "alcohol",
            "stock_date": "10/17/2018",
            "quantity": 300,
            "acceptable_minimum": 80
        }
        # json_new_product = json.dumps(product_new)
        # add_products_url = "api/v1/products/add"
        # http_response = self.client.post(add_products_url, content_type='application/json', data = json_new_product)
        # self.assertEqual(http_response.status_code, 202)

        """implement after implementing user authentication
        if user_role == 2:
            self.assertEqual(http_response.status_code, 202)
        else:
            self.assertEqual(http_response.status_code, 403)"""
    