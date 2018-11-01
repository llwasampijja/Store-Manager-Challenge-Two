from app.validity_check import check_item_in_list
from app.utilities import get_chosen_item
class AppUser():
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.user_name= kwargs.get("user_name")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.user_role = kwargs.get("user_role")

    def get_all_users(self, users):
        return users

    def get_user_by_id(self, user_id, users):
        if check_item_in_list("user_id", user_id, users):
            return get_chosen_item("user_id", user_id, users)
        else:
            return {"Message": "User not registered on the system"}


    def check_empty_fields(self, user_id, user_name, username, password, user_role):
        if not user_id or not user_name or not username or not password or not user_role:
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

    
    
