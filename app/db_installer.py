from app.store_managerdb import DatabaseConnect

def initialize_db():
    db_connect = DatabaseConnect()
    db_connect.create_tables()

if __name__ == "__main__":
    initialize_db()