# from app.validity_check import check_item_in_list
class AppUser():
    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.user_name= kwargs.get("user_name")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.user_role = kwargs.get("user_role")



    
    
