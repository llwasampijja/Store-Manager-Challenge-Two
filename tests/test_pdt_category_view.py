import unittest
from app.views.pdt_category_view import get_db_categories, add_category
from app import create_app
from flask import Response
from config import env_config, runtime_mode
import json
from app.store_managerdb import DatabaseConnect
from app.utilities import create_admin_user

class TestPdtCategoryView(unittest.TestCase):
    def setUp(self):
        self.app = create_app(env_config.get("{}".format(runtime_mode)))
        self.client = self.app.test_client(self)
        self.database_connect_obj = DatabaseConnect()
        self.database_connect_obj.delete_table_categories()
        self.database_connect_obj.create_tables()
        login_creds = {"username": "edward", "password": "myname"}
        self.login_response = self.client.post("api/v1/auth/login", data = json.dumps(login_creds),\
         content_type="application/json")
        self.database_connect_obj.insert_data_categories("snacksrf")
        

    def create_admin_user(self):
        create_admin_user()

    def test_add_category(self):
        jwt_token = json.loads(self.login_response.data)["Access Token"]
        category = {"category_name": "snacks"}
        response = self.client.post("api/v1/categories", headers=dict(Authorization='Bearer '+ jwt_token), \
        data = json.dumps(category), content_type="application/json") 
        self.assertEqual(response.status_code, 201)

    def test_add_category_empty(self):
        jwt_token = json.loads(self.login_response.data)["Access Token"]
        category_2 = {"category_name": "  "}
        response_2 = self.client.post("api/v1/categories", headers=dict(Authorization='Bearer '+ jwt_token), \
        data = json.dumps(category_2), content_type="application/json")
        self.assertEqual(response_2.status_code, 201)

    def test_get_all_product_categories(self):
        jwt_token = json.loads(self.login_response.data)["Access Token"]
        response = self.client.get("api/v1/categories", headers=dict(Authorization='Bearer '+ jwt_token),\
         content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_get_category(self):
        jwt_token = json.loads(self.login_response.data)["Access Token"]
        response = self.client.get("api/v1/categories/1", headers=dict(Authorization='Bearer '+ jwt_token),\
         content_type="application/json")
        self.assertEqual(response.status_code, 200)

    
