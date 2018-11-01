from app.data_stored import users_store_attendants
from app.validity_check import check_item_in_list
from app.utilities import get_chosen_item
class StoreAttendant():
    def __init__(self, **kwargs):
        self.user_id_store_attendat = kwargs.get("user_id")
        self.name_store_attendant = kwargs.get("user_name")
        self.username_store_attendant = kwargs.get("username")
        self.password_store_attendant = kwargs.get("password")
        self.user_role_store_attendant = kwargs.get("user_role")

    def get_all_store_attendants(self):
        return users_store_attendants

    def get_user_by_id(self, user_id):
        if check_item_in_list("user_id", user_id, self.get_all_store_attendants()):
            return get_chosen_item("user_id", user_id, self.get_all_store_attendants())
        else:
            return {"Message": "User not registered on the system"}

    def check_empty_fields(self, user_id_store_attendat, name_store_attendant, \
        username_store_attendant, password_store_attendant, user_role_store_attendant):
        if self.user_id_store_attendat or self.name_store_attendant or self.username_store_attendant \
            or self.password_store_attendant or self.user_role_store_attendant == "":
            return True
        else:
            return False


    
