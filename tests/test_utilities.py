import unittest
from app.utilities import get_all_items
from app import utilities

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

    def test_get_all_items(self):
        self.assertEqual(utilities.get_all_items(self.test_items), self.test_items)
        self.assertNotEqual(utilities.get_all_items(self.test_items), self.test_items[1])
        self.assertEqual(utilities.get_all_items(self.test_list2), {"message": "List is Empty"})

    def test_get_chosen_item(self):
        self.assertEqual(utilities.get_chosen_item("product_id", 1, self.test_items), self.test_items[0])
        self.assertNotEqual(utilities.get_chosen_item("product_id", 1, self.test_items), self.test_items[1])
