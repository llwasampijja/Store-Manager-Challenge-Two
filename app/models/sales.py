class Sales():

    def __init__(self, **kwargs):

        self.sale_index = kwargs.get("sale_index")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category = kwargs.get("category")
        self.sale_date = kwargs.get("sale_date")
        self.sale_quantity = kwargs.get("sale_quantity")
        self.total_sale = kwargs.get("total_sale")
        self.sale_made_by = kwargs.get("sale_made_by")
        
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
        if len(self.sale_records) == 0:
            message = {"message": "You just opened up a few seconds ago, Nothing sold yet"}
            return message
        else:
            return self.sale_records

    def get_single_sale (self, sale_index):
        for item in self.sale_records:
            if item["sale_index"] == sale_index:
                return item

    def make_sale_order(self):
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
