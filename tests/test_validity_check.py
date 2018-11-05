import unittest
from app.validity_check import valid_product, invalid_sale, invalid_user#, product_available

class TestValiditCheck(unittest.TestCase):
    def setUp(self):
        self.test_product_one = {
                "product_name": "Tumpeco",
                "unit_price": 500,
                "category_name": "Utencils",
                "quantity": 50,
                "acceptable_minimum": 10
            }

        self.test_product_two = {
                "product_id": 1,
                "product_name": "Tumpeco",
                "unit_price": 500,
                "acceptable_minimum": 10
            }

        self.test_sale_one = {
            "product_name": "pen" ,
            "unit_price": 300,
            "category_name": 2,
            "sale_quantity":3
            }

        self.test_sale_two = {
            "product_name": "pen" ,
            "category_name": 2,
            "sale_quantity":3
            }

        self.test_user_one = {
            "user_name":"Eddy Gee",
             "username":"eddy",
             "password":"iam",
             "user_role":"attendant"
        }

        self.test_user_two = {
            "user_name":"Eddy Gee",
             "usename":"eddy",
             "password":"iam",
             "user_role":"attendant"
        }

    def test_valid_product(self):
        self.assertTrue(valid_product(self.test_product_one))
        self.assertFalse(valid_product(self.test_product_two))

    def test_invalid_user(self):
        self.assertFalse(invalid_user(self.test_user_one))
        self.assertTrue(invalid_user(self.test_user_two))

    def test_invalid_sale(self):
        self.assertFalse(invalid_sale(self.test_sale_one))
        self.assertTrue(invalid_sale(self.test_sale_two))

