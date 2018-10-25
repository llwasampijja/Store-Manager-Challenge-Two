"""
This module includes a "Products" class with methods which are rreusable from other modules.
"""

from app.utilities import get_all_items, get_chosen_item

class Products():
   

    def __init__(self, **kwargs):
        """
        This constructor declares and initialises variables that are going to be used in the class.
        The "**kwargs" indicates that there are multiple "key:value" variables in the constructor. 
        """
        self.product_id = kwargs.get("product_id")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category = kwargs.get("category")
        self.stock_date = kwargs.get("stock_date")
        self.quantity = kwargs.get("stock_date")
        self.acceptable_minimum = kwargs.get("acceptable_minimum")

        """Sample list of products"""
        self.products = [
            {
                "product_id": 0,
                "product_name": "Tumpeco",
                "unit_price": 500,
                "category": "Utencils",
                "stock_date": "11/12/2018",
                "quantity": 50,
                "acceptable_minimum": 10
            },
            {
                "product_id": 1,
                "product_name": "1 Dozen Spoons",
                "unit_price": 10000,
                "category": "Utencils",
                "stock_date": "11/11/2018",
                "quantity": 12,
                "acceptable_minimum": 2
            },
            {
                "product_id": 2,
                "product_name": "500g Noodles Packet",
                "unit_price": 1000,
                "category": "food",
                "stock_date": "12/12/2018",
                "quantity": 100,
                "acceptable_minimum": 20
            },
            {
                "product_id": 3,
                "product_name": "Smirnoff Black",
                "unit_price": 3500,
                "category": "alcohol",
                "stock_date": "11/24/2018",
                "quantity": 250,
                "acceptable_minimum": 50
            },
            {
                "product_id": 4,
                "product_name": "1 Liter Soda",
                "unit_price": 2000,
                "category": "Utencils",
                "stock_date": "11/12/2018",
                "quantity": 288,
                "acceptable_minimum": 72
            }
        ]

    def get_all_products(self):
        """Return all the products in the inventory"""
        return get_all_items(self.products)

    def get_product_by_id(self, product_id):
        """Returns a product by its id"""
        return get_chosen_item("product_id", product_id, self.products)

    def admin_add_product(self):
        """Adds a product. This method is mainly used for unit testing"""
        product_new = {
            "product_id": "5",
            "product_name": "Nile Special",
            "unit_price": 4000,
            "category": "alcohol",
            "stock_date": "10/17/2018",
            "quantity": 300,
            "acceptable_minimum": 80

        }

        for product in self.products:
            # test if product already exists in the inventory
            if product_new.get("product_name") == product.get("product_name"):
                return "That product is already in the system, consider modifying that."
                # check to see if user enters nothing in any of the fields
            else:
                self.products.append(product_new)
                return self.products


