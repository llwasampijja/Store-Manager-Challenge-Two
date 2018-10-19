import unittest
import json
from app import app
from app.utilities import blueprint
from app.models.sales import Sales


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.register_blueprint(blueprint, url_prefix='/api/v1')
        self.sales_obj = Sales()
        self.sales  = self.sales_obj.sale_records
        self.client = self.app.test_client(self)
        self.sales_uri = 'api/v1/sales'

    def test_get_sales(self):
        http_response = self.client.get(self.sales_uri)
        self.assertEqual(http_response.status_code, 200)
        self.assertNotEqual(http_response.status_code, 404)