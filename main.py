from app import create_app
from app.store_managerdb import DatabaseConnect

app = create_app()

if __name__ == '__main__':
    database_connect = DatabaseConnect()
    database_connect.create_tables()
    
    app.run(debug=True)
    database_connect.insert_data_users()
    """run the app with debug true"""