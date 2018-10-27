import unittest
from app.validity_check import valid_product, valid_sale

class TestValiditCheck(unittest.TestCase):
    def setUp(self):
        self.test_product_one = {
                "product_id": 1,
                "product_name": "Tumpeco",
                "unit_price": 500,
                "category": "Utencils",
                "stock_date": "11/12/2018",
                "quantity": 50,
                "acceptable_minimum": 10
            }

        self.test_product_two = {
                "product_id": 1,
                "product_name": "Tumpeco",
                "unit_price": 500,
                "acceptable_minimum": 10
            }

        self.test_sale_order = {
            "sale_index": 6,
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "category": "food",
            "sale_date": "10/18/2018",
            "sale_quantity": 3,
            "total_sale": 6000,
            "sale_made_by": "Jon Snow"
        }

        self.test_sale_order_two = {
            "sale_index": 6,
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "total_sale": 6000,
            "sale_made_by": "Jon Snow"
        }
    def test_valid_product(self):
        self.assertTrue(valid_product(self.test_product_one))
        self.assertFalse(valid_product(self.test_product_two))

    def test_valid_sale(self):
        self.assertTrue(valid_sale(self.test_sale_order))
        self.assertFalse(valid_sale(self.test_sale_order_two))