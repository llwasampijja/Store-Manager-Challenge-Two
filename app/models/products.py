# add github pivotal integration
class Products():
    products = [
        {
            "product_name": "Tumpeco",
            "unit_price": 500,
            "category": "Utencils",
            "stock-date": "11/12/2018",
            "quantity": 50,
            "acceptable-minimum": 10
        },
        {
            "product_name": "1 Dozen Spoons",
            "unit_price": 10000,
            "category": "Utencils",
            "stock-date": "11/11/2018",
            "quantity": 12,
            "acceptable-minimum": 2
        },
        {
            "product_name": "500g Noodles Packet",
            "unit_price": 1000,
            "category": "food",
            "stock-date": "12/12/2018",
            "quantity": 100,
            "acceptable-minimum": 20
        },
        {
            "product_name": "Smirnoff Black",
            "unit_price": 3500,
            "category": "alcohol",
            "stock-date": "11/24/2018",
            "quantity": 250,
            "acceptable-minimum": 50
        },
        {
            "product_name": "1 Liter Soda",
            "unit_price": 2000,
            "category": "Utencils",
            "stock-date": "11/12/2018",
            "quantity": 288,
            "acceptable-minimum": 72
        }
    ]

    def __init(self, products):
        pass
    # def __init__(self, product_name, unit_price, category, stock_date, quantity, acceptable_minimum):
    #     self.product_name = product_name
    #     self.unit_price = unit_price
    #     self.category = category
    #     self.stock_date = stock_date
    #     self.quantity = stock_date
    #     self.acceptable_minimum = acceptable_minimum

    def get_all_products(self):
        if len(self.products) == 0:
            message = {"message": "You are completely out of stock"}
            return message
        return self.products
