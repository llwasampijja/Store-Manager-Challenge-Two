from app.data_stored import product_categories
class Category():

    def __init__(self, **kwargs):
        self.category_name = kwargs.get("category_name")
        self.category_id = kwargs.get("category_id")

    def get_all_categories(self):
        return product_categories