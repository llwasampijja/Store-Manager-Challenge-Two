import unittest
import json
from app import app
from app.utilities import blueprint, user_role, author
from app.models.products import Products
from flask import jsonify, request
import requests



class TestProducts(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.products_obj = Products()
        self.products_list  = self.products_obj.get_all_products()
        self.client = self.app.test_client(self)
        self.products_url = 'api/v1/products'

    def test_get_all_products(self):
        http_response = self.client.get(self.products_url)
        self.assertEqual(http_response.status_code, 200)
        self.assertNotEqual(http_response.status_code, 404)

    def test_get_a_product(self):   
        get_product_url = 'api/v1/products/{0}'.format(2)
        http_response = self.client.get(get_product_url, content_type='application/json')
        self.assertEqual(http_response.status_code, 200)
        self.assertFalse(self.is_product_avaialble(32))
        self.assertTrue(self.is_product_avaialble(2))

    def is_product_avaialble(self, product_id):
        if any(product_id == item["product_id"] for item in self.products_list):
            return True
        return False

    def test_add_product(self):
        json_new_product = json.dumps(self.products_obj.admin_add_product())
        add_products_url = "api/v1/products/add"
        http_response = self.client.post(add_products_url, data = json_new_product)
        if user_role == 2:
            self.assertEqual(http_response.status_code, 200)
        else:
            self.assertEqual(http_response.status_code, 403)