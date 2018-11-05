from app import create_app
from app.store_managerdb import DatabaseConnect
from flask import request, Response
import json
import os
from config import env_config, runtime_mode
from app.utilities import create_admin_user

app = create_app(env_config.get("{}".format(runtime_mode)))




if __name__ == '__main__':
    database_connect = DatabaseConnect()
    database_connect.create_tables()
    create_admin_user()
    app.run()
    
    """run the app with debug true"""
    print("Thop op thu :", os.environ['APP_SETTINGS'])


