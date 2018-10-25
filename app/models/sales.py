"""
This module includes a "Sales" class  and different methods which can be used by other modules.
"""
from app.utilities import get_all_items, get_chosen_item
class Sales():

    def __init__(self, **kwargs):
        """
        This constructor declares and initialises the different variables that are to
         be used within the class as well as its objects created outside of it.
         The "**kwargs" indicates that there are multiple "key:value" variables in the constructor.
        """
        self.sale_index = kwargs.get("sale_index")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category = kwargs.get("category")
        self.sale_date = kwargs.get("sale_date")
        self.sale_quantity = kwargs.get("sale_quantity")
        self.total_sale = kwargs.get("total_sale")
        self.sale_made_by = kwargs.get("sale_made_by")
        
        """" This list is for testing purposes until a db is created"""
        self.sale_records = [
            {
            "sale_index": 1,
            "product_name": "1 Dozen Spoons",
            "unit_price": 10000,
            "category": "Utencils",
            "sale_date": "11/12/2018",
            "sale_quantity": 1,
            "total_sale": 10000,
            "sale_made_by": "Dall Kased"
            },
            {
            "sale_index": 2,
            "product_name": "Tumpeco",
            "unit_price": 500,
            "category": "Utencils",
            "sale_date": "11/12/2018",
            "sale_quantity": 2,
            "total_sale": 1000,
            "sale_made_by": "John Snow"
            },
            {
            "sale_index": 3,
            "product_name": "500g Noodles Packet",
            "unit_price": 1000,
            "category": "food",
            "sale_date": "11/12/2018",
            "sale_quantity": 3,
            "total_sale": 3000,
            "sale_made_by": "No One"
            },
            {
            "sale_index": 4,
            "product_name": "Smirnoff Black",
            "unit_price": 3500,
            "category": "alcohol",
            "sale_date": "11/12/2018",
            "sale_quantity": 4,
            "total_sale": 1400,
            "sale_made_by": "Dall Kased"
            },
            {
            "sale_index": 5,
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "category": "food",
            "sale_date": "11/12/2018",
            "sale_quantity": 10,
            "total_sale": 10000,
            "sale_made_by": "No One"
            }
    ]

    def get_all_sales(self):
        """ This method returns all the sales by the deifferent store attendants"""
        return get_all_items(self.sale_records)

    def get_single_sale(self, sale_index):
        """This method returns a sale by its index (sale_index) or id """
        return get_chosen_item("sale_index", sale_index, self.sale_records)

    def make_sale_order(self):
        """
        This method is for creating a sale record. It's method is mainly used for unit testing
        """
        sale_order_new = {
            "sale_index": 6,
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "category": "food",
            "sale_date": "10/18/2018",
            "sale_quantity": 3,
            "total_sale": 6000,
            "sale_made_by": "Jon Snow"
        }

        self.sale_records.append(sale_order_new)
        return self.sale_records
