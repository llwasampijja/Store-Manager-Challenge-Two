"""
This module includes a "Products" class with methods which are rreusable from other modules.
"""

from app.utilities import get_all_items, get_chosen_item
from app.data_stored import products_in_inventory
from app.validity_check import check_item_in_list

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
        self.products = products_in_inventory

    def get_all_products(self):
        """Return all the products in the inventory"""
        return get_all_items(self.products)

    def get_product_by_id(self, product_id):
        """Returns a product by its id"""
        if check_item_in_list("product_id", product_id, self.products):
            return get_chosen_item("product_id", product_id, self.products)
        else:
            return {"Message": "Sale Record is not in the list"}

    # def admin_add_product(self):
    #     """Adds a product. This method is mainly used for unit testing"""
    #     product_new = {
    #         "product_id": "5",
    #         "product_name": "Nile Special",
    #         "unit_price": 4000,
    #         "category": "alcohol",
    #         "stock_date": "10/17/2018",
    #         "quantity": 300,
    #         "acceptable_minimum": 80

    #     }

    #     for product in self.products:
    #         # test if product already exists in the inventory
    #         if product_new.get("product_name") == product.get("product_name"):
    #             return "That product is already in the system, consider modifying that."
    #             # check to see if user enters nothing in any of the fields
    #         else:
    #             self.products.append(product_new)
    #             return self.products


