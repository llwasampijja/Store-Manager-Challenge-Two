"""
This module includes a "Products" class with methods which are rreusable from other modules.
"""

from app.data_stored import products_in_inventory
# from app.validity_check import check_item_in_list

class Products():
   

    def __init__(self, **kwargs):
        """
        This constructor declares and initialises variables that are going to be used in the class.
        The "**kwargs" indicates that there are multiple "key:value" variables in the constructor. 
        """
        self.product_id = kwargs.get("product_id")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category_name = kwargs.get("category_name")
        self.stock_date = kwargs.get("stock_date")
        self.quantity = kwargs.get("stock_date")
        self.acceptable_minimum = kwargs.get("acceptable_minimum")





