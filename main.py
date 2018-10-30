from app import create_app
from app.store_managerdb import DatabaseConnect

app = create_app()

if __name__ == '__main__':
    database_connect = DatabaseConnect()
    database_connect.create_tables()
    # database_connect.create_admin_user()
    app.run(debug=True)
    """run the app with debug true"""