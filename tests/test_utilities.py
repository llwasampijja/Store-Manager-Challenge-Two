import unittest
from app import utilities
from flask import Response
import json

class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.test_items = [
            {
                "product_id": 1,
                "product_name": "Tumpeco",
                "unit_price": 500,
                "category": "Utencils",
                "stock_date": "11/12/2018",
                "quantity": 50,
                "acceptable_minimum": 10
            },
            {
                "product_id": 2,
                "product_name": "1 Dozen Spoons",
                "unit_price": 10000,
                "category": "Utencils",
                "stock_date": "11/11/2018",
                "quantity": 12,
                "acceptable_minimum": 2
            }]

        self.test_list2 = []

    def test_doesnt_exist(self):
        message = {"Message:": "Product or Category does not exist"}
        response = Response (json.dumps(message), content_type="application/json", status=201)
        self.assertEqual(str(utilities.doesnt_exist()), str(response))


