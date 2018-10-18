import unittest
import json
from app import app
from app.utilities import bp
from app.models.sales import Sales


class TestSales(unittest.TestCase):
    def setUp(self):
        self.app = app
        # self.app = create_app_environment('testing')
        # self.app.config['JWT_TOKEN_LOCATION'] = BaseConfig.JWT_TOKEN_LOCATION
        self.app.register_blueprint(bp, url_prefix='/api/v1')
        self.sales_obj = Sales()
        # self.jwt = jwt
        self.sales  = self.sales_obj.sale_records
        self.client = self.app.test_client(self)
        self.sales_uri = 'api/v1/sales'
        self.sample_sale = dict(
            product_name = "Cooker",
            product_category="Electronics",
            quantity=37,
            unit_cost=13000000
        )

        self.empty_product = dict(
            product_name = "",
            product_category="",
            quantity=None,
            unit_cost=None
        )

    def test_get_sales(self):
        http_response = self.client.get(self.sales_uri)
        self.assertEqual(http_response.status_code, 200)
        self.assertNotEqual(http_response.status_code, 404)

    def test_get_a_sale(self):
            
        sale_url = 'api/v1/sales/{0}'.format(2)
        http_response = self.client.get(sale_url, content_type='application/json')
        self.assertEqual(http_response.status_code, 200)
        self.assertFalse(self.is_sale_avaialble(32))
        self.assertTrue(self.is_sale_avaialble(2))

    def is_sale_avaialble(self, sale_id):
        if any(sale_id == item["sale_index"] for item in self.sales):
            return True
        return False

    def test_add_sale(self):
        pass
        
        
        
        # res = self.client.get(
        #     'api/v1/products/{0}'.format(id),
        #     content_type='application/json'
        # )
        # data = json.loads(res.data)
        # data2 = res.json()
        # self.assertEqual(200, data2[-1], msg="found the sale"

        # data = json.loads(res.data)
        
        # self.assertEqual(200, data[-1], msg="found product")
