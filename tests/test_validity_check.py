import unittest
from app.validity_check import valid_product, invalid_sale, invalid_user, \
    check_empty_fields, check_role, correct_data_type, empty_category, wrong_type_category,\
    check_empty_fields_products, correct_type_products, check_empty_fields_sales, correct_type_sales

class TestValiditCheck(unittest.TestCase):
    def setUp(self):
        pass
        self.test_product_one = {
                "product_name": "Tumpeco",
                "unit_price": 500,
                "category_name": "Utencils",
                "quantity": 50,
                "acceptable_minimum": 10
            }

        self.test_product_two = {
                "product_id": 1,
                "product_name": "   ",
                "unit_price": 500,
                "acceptable_minimum": 10
            }

        self.test_sale_one = {
            "product_name": "pen" ,
            "unit_price": 300,
            "category_name": "2",
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
             "username":" ",
             "password":9,
             "user_role":"attendeant"
        }

        self.test_user_three = {
            "user_name":"Eddy Gee",
             "usename":"  ",
             "password":9,
             "user_role":"admin"
        }

        self.test_category_one = {
            "category_name": "food",
            "category_name2": "  ",
            "category_name3": "food",
            "category_name4": 88
        }

    def test_check_empty_fields(self):
        self.assertFalse(check_empty_fields("edwa  ard", "edward", "password", "attendant"))
        self.assertTrue(check_empty_fields("  ", "edward", "password", "attendant"))

    def test_correct_data_type(self):
        self.assertTrue(correct_data_type("edwa  ard", "edward", "password", "attendant"))
        self.assertFalse(correct_data_type(43,"edward", "password", "attendant"))

    def test_check_role(self):
        self.assertTrue(check_role("admin"))
        self.assertTrue(check_role("attendant"))
        self.assertFalse(check_role("atendant"))

    def test_valid_product(self):
        self.assertTrue(valid_product(self.test_product_one))
        self.assertFalse(valid_product(self.test_product_two))

    def test_invalid_user(self):
        self.assertFalse(invalid_user(self.test_user_one))
        self.assertTrue(invalid_user(self.test_user_three))

    def test_invalid_sale(self):
        self.assertFalse(invalid_sale(self.test_sale_one))
        self.assertTrue(invalid_sale(self.test_sale_two))
    
    def test_empty_category(self):
        self.assertFalse(empty_category("food"))
        self.assertTrue(empty_category("  "))


    def test_wrong_type_category(self):
        self.assertFalse(wrong_type_category("food"))
        self.assertTrue(wrong_type_category(67))

    def test_check_empty_fields_products(self):
        self.assertTrue(check_empty_fields_products("bread", 4500, "food", 20, 10))
        self.assertFalse(check_empty_fields_products("  ", 3000, "drinks", 44, 11))

    def test_correct_type_products(self):
        self.assertTrue(correct_type_products("cassava", 1000, "food", 30, 5))
        self.assertFalse(correct_type_products(34, 32, 23, 43, 3))

    def test_check_empty_fields_sales(self):
        self.assertTrue(check_empty_fields_sales("  ", 900, "food",12))
        self.assertFalse(check_empty_fields_sales(\
            self.test_sale_one.get("product_name"),\
            600,\
            self.test_sale_one.get("category_name"),\
            self.test_sale_one.get("sale_quantity")
        ))

    def test_correct_type_sales(self):
        self.assertTrue(correct_type_sales(\
            self.test_sale_one.get("product_name"),\
            self.test_sale_one.get("unit_price"),\
            self.test_sale_one.get("category_name"),\
            self.test_sale_one.get("sale_quantity")
        ))
        self.assertFalse(correct_type_sales(\
            self.test_sale_one.get("product_name"),\
            "  ",\
            self.test_sale_one.get("category_name"),\
            self.test_sale_one.get("sale_quantity")
        ))

