import unittest
import json
from app import app
from app.utilities import bp


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client(self)
        self.index_url = 'api/v1/'


    def test_index(self):
        http_response = self.client.get(self.index_url)
        self.assertEqual(http_response.status_code, 200)
        self.assertNotEqual(http_response.status_code, 404)
