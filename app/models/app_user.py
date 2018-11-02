from app.validity_check import check_item_in_list
from app.utilities import get_chosen_item
class AppUser():
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.user_name= kwargs.get("user_name")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.user_role = kwargs.get("user_role")


    def check_empty_fields(self, user_name, username, password, user_role):
        if user_name or not username or not password or not user_role:
            return True
        else:
            return False

    def correct_data_type(self, user_name, username, password, user_role):
        if isinstance(user_name, str) and isinstance(username, str) and isinstance(user_role, str):
            return True
        else:
            return False

    def check_role(self, user_role):
        if user_role == "admin":
            return True
        elif user_role == "attendant":
            return True
        else:
            return False

    
    
