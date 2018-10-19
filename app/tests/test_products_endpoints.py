import unittest
import json
from app import app
from app.utilities import blueprint
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