import unittest
from app.views.pdt_category_view import get_db_categories, add_category
from app import create_app
from flask import Response
from config import env_config, runtime_mode
import json

class TestPdtCategoryView(unittest.TestCase):
    def setup(self):
        self.app = create_app(env_config.get("{}".format(runtime_mode)))
        # self.products_obj = Products()
        # self.products_list  = self.products_obj.products
        self.client = self.app.test_client(self)
        self.categories_list = [
            {
                'product_id': 1,
                'category_name': 'Food'
            },
            {   
                'product_id': 2,
                'category_name': 'Drinks'
            },
            {
                'product_id': 3,
                'category_name': 'snacks'
            }]

