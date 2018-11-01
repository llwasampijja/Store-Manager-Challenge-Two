from app import create_app
from app.store_managerdb import DatabaseConnect
from flask import request, Response
import hashlib
import json

app = create_app()

def create_admin_user():
    # request_data = request.get_json()
    user_name = "Edward Army"
    username = "edward"
    password = "myname"
    hashed_password = hashlib.sha224(b"{}").hexdigest().format(password)
    user_role = "admin"
    returned_user = list(database_connect.user_exist_not(username))

    if len(returned_user)==0:
        message = {"Message:": "User Successifully Added", "Username:": username,\
         "Name ": user_name, "Password": hashed_password}
        database_connect.insert_data_users(user_name, username, hashed_password, user_role)
        # response = Response (json.dumps(message), content_type="application/json", status=201)
        # return response
    else:
        message = {"Message:": "The User Already Exists"}
        # response = Response (json.dumps(message), content_type="application/json", status=201)
        # return response

if __name__ == '__main__':
    database_connect = DatabaseConnect()
    database_connect.create_tables()
    create_admin_user()
    app.run(debug=True)
    """run the app with debug true"""


