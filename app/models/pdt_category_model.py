from app.data_stored import pdt_categories
from app.utilities import get_chosen_item
class PdtCategory():

    def __init__(self, **kwargs):
        self.pdt_category_id = kwargs.get("pdt_category_id")
        self.pdt_category_name = kwargs.get("pdt_category_name")

    # def get_all_categories(self):
    #     return pdt_categories

    # def get_category_by_id(self, pdt_category_id):
    #     return get_chosen_item("pdt_category_id", pdt_category_id, self.get_all_categories())
        


