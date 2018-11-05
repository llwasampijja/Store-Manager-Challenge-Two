"""
This module includes a "Sales" class  and different methods which can be used by other modules.
"""
from app.data_stored import sale_records_stored
# from app.validity_check import check_item_in_list
class Sales():

    def __init__(self, **kwargs):
        """
        This constructor declares and initialises the different variables that are to
         be used within the class as well as its objects created outside of it.
         The "**kwargs" indicates that there are multiple "key:value" variables in the constructor.
        """
        self.sale_id = kwargs.get("sale_id")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category_name = kwargs.get("category_name")
        self.sale_date = kwargs.get("sale_date")
        self.sale_quantity = kwargs.get("sale_quantity")
        self.total_sale = kwargs.get("total_sale")
        self.sale_made_by = kwargs.get("sale_made_by")

