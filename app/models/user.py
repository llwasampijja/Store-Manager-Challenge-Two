ACCESS = {
    'user'
    'store_attendant': 1,
    'admin': 2,
    'store_owner': 3
}

class User():
    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.contact_num = kwargs.get('contact_num')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.access = kwargs.get('access')

        self.users = [
            {
                "first_name": "Ann",
                "last_name": "Night",
                "username": "ann",
                "password": "owner",
                "contact_num": 980930023,
                "access": ACCESS['store_owner']
            },
            {
                "first_name": "Dall",
                "last_name": "Kased",
                "username": "dallkased",
                "password": "admin",
                "contact_num": 8467902742,
                "access": ACCESS['admin']
            },
            {
                "first_name": "No",
                "last_name": "One",
                "username": "noone",
                "password": "store_attendant",
                "contact_num": 53937964927,
                "access": ACCESS['store_owner']
            }
        ]

    def get_all_users(self):
        return self.users
            
    def is_store_attendant(self):
        return self.access == ACCESS['store_attendant']

    def is_admin(self):
        return self.access == ACCESS['admin']

    def is_store_owner(self):
        return self.access == ACCESS['store_owner']

    def allowed(self, access_level):
        return self.access >= access_level

    def find_by_username(self, username):
        for item in self.users:
            if item["username"] == username:
                return item
