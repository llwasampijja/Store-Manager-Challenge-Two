class Products():

    def __init__(self, **kwargs):

        self.product_id = kwargs.get("product_id")
        self.product_name = kwargs.get("product_name")
        self.unit_price = kwargs.get("unit_price")
        self.category = kwargs.get("category")
        self.stock_date = kwargs.get("stock_date")
        self.quantity = kwargs.get("stock_date")
        self.acceptable_minimum = kwargs.get("acceptable_minimum")
        
        self.products = [
            {
            "product_id": 0,
            "product_name": "Tumpeco",
            "unit_price": 500,
            "category": "Utencils",
            "stock-date": "11/12/2018",
            "quantity": 50,
            "acceptable-minimum": 10
            },
            {
            "product_id": 1,
            "product_name": "1 Dozen Spoons",
            "unit_price": 10000,
            "category": "Utencils",
            "stock-date": "11/11/2018",
            "quantity": 12,
            "acceptable-minimum": 2
            },
            {
            "product_id": 2,
            "product_name": "500g Noodles Packet",
            "unit_price": 1000,
            "category": "food",
            "stock-date": "12/12/2018",
            "quantity": 100,
            "acceptable-minimum": 20
            },
            {
            "product_id": 3,
            "product_name": "Smirnoff Black",
            "unit_price": 3500,
            "category": "alcohol",
            "stock-date": "11/24/2018",
            "quantity": 250,
            "acceptable-minimum": 50
            },
            {
            "product_id": 4,
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "category": "Utencils",
            "stock-date": "11/12/2018",
            "quantity": 288,
            "acceptable-minimum": 72
            }
    ]

    def get_all_products(self):
        if len(self.products) == 0:
            message = {"message": "You are completely out of stock"}
            return message
        else:
            return self.products

    def get_product_by_id (self, product_id):
        for item in self.products:
            if item["product_id"] == product_id:
                return item

    def admin_add_product(self):
        product_new = {
            "product_id": "5",
            "product_name": "Nile Special",
            "unit_price": 4000,
            "category": "alcohol",
            "stock-date": "10/17/2018",
            "quantity": 300,
            "acceptable-minimum": 80
        }

        for product in self.products:
            # test if product already exists in the inventory
            if product_new["product_name"] == product["product_name"]:
                return "That product is already in the system, consider modifying that."
                # check to see if user enters nothing in any of the fields
            else:
                self.products.append(product_new)
                return self.products