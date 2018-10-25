"""
This module is for unit tests of methods in  the sales.py 
module as well as those in sales_views.py module
"""

import unittest
import json
from app import create_app
from app.utilities import user_role, author
from app.models.sales import Sales


class TestSales(unittest.TestCase):

    def setUp(self):
        """
        Declare and initialize the variables
        """
        self.app = create_app()
        self.sales_obj = Sales()
        self.sales  = self.sales_obj.sale_records
        self.client = self.app.test_client(self)

    def test_get_sales(self):
        """
        Unit test for method get_sales
        """
        http_response = self.client.get('api/v1/sales')
        self.assertNotEqual(http_response.status_code, 404)
        if user_role == 2:
            self.assertEqual(http_response.status_code, 200)
        else:
            self.assertEqual(http_response.status_code, 403)

    def test_get_a_sale(self):
        """
        Unit test for method get_a_sale
        """
        sale_url = 'api/v1/sales/{0}'.format(2)
        http_response = self.client.get(sale_url, content_type='application/json')
        self.assertFalse(self.is_sale_avaialble(32))
        self.assertTrue(self.is_sale_avaialble(2))
        if user_role == 2:
            self.assertEqual(http_response.status_code, 200)
        elif author:
            self.assertEqual(http_response.status_code, 200)
        else:
            self.assertEqual(http_response.status_code, 403)

    def is_sale_avaialble(self, sale_id):
        """"
        Check if a sale record in the sales list. This method is used to create a unit test for sale not available.
        """
        if any(sale_id == item.get("sale_index") for item in self.sales):
            return True
        return False

    def test_add_sale(self):
        """
        Unit test for add_sale method
        """
        json_new_sale = json.dumps(self.sales_obj.make_sale_order())
        add_sale_url = "api/v1/sales/add"
        add_sale_wrong_url = "api/v1/sales/add/"
        http_response = self.client.post(add_sale_url, data = json_new_sale)
        http_response_wrong = self.client.post(add_sale_wrong_url, data = json_new_sale)
        if user_role == 1:
            self.assertEqual(http_response.status_code, 200)
        else:
            self.assertEqual(http_response.status_code, 403)
        self.assertEqual(http_response_wrong.status_code, 404)
        