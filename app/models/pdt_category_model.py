from app.data_stored import pdt_categories
class PdtCategory():

    def __init__(self, **kwargs):
        self.pdt_category_id = kwargs.get("pdt_category_id")
        self.pdt_category_name = kwargs.get("pdt_category_name")
        


