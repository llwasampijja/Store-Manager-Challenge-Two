"""
This module includes a "Sales" class  and different methods which can be used by other modules.
"""
from app.utilities import get_all_items, get_chosen_item
from app.data_stored import sale_records_stored
from app.validity_check import check_item_in_list
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
        
    #     """" This list is for testing purposes until a db is created"""
    #     self.sale_records = sale_records_stored

    # def get_all_sales(self):
    #     """ This method returns all the sales by the deifferent store attendants"""
    #     return get_all_items(self.sale_records)

    # def get_single_sale(self, sale_id):
    #     """This method returns a sale by its id (sale_id) or id """
    #     if check_item_in_list("sale_id", sale_id, self.sale_records):
    #         return get_chosen_item("sale_id", sale_id, self.sale_records)
    #     else:
    #         return {"Message": "Sale Record is not in the list"}


    def check_empty_fields(self, product_name, unit_price, category_name, \
        sale_quantity):
        if not product_name.strip() or not unit_price.strip() or not category_name.strip() or not sale_quantity.strip():
            return True
        else:
            return False

    def correct_sale_type(self, product_name, unit_price, category_name, \
        sale_quantity):
        if isinstance(product_name, str) and isinstance(unit_price, int) \
            and isinstance(category_name, str) and isinstance(sale_quantity, int):
            return True
        else:
            return False

