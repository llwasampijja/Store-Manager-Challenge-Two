import psycopg2
from app.store_managerdb import DatabaseConnect
from app.utilities import create_admin_user


database_connect_obj = DatabaseConnect()
# db_connect = psycopg2.connect(\
# "dbname='store_manager_db' \
# user='andela' \
# host='localhost' \
# password='bootcamp'")
# db_connect.autocommit = True

# cursor_db = db_connect.cursor()
    
    
# def create_tables():
#     """create users table"""
#     cursor_db.execute("CREATE TABLE IF NOT EXISTS app_users(\
#     user_id serial PRIMARY KEY, \
#     user_name varchar, \
#     username varchar UNIQUE, \
#     password varchar,\
#     user_role varchar)")

#     cursor_db.execute("CREATE TABLE IF NOT EXISTS categories(\
#     category_id serial PRIMARY KEY, \
#     category_name varchar UNIQUE)")

#     cursor_db.execute("CREATE TABLE IF NOT EXISTS products(\
#     product_id serial PRIMARY KEY, \
#     product_name varchar UNIQUE, \
#     unit_price int, \
#     minimum_quantity int, \
#     stock_date TIMESTAMP, \
#     category_name int REFERENCES categories(category_id) ON DELETE RESTRICT,\
#     quantity int)")

#     cursor_db.execute("CREATE TABLE IF NOT EXISTS sales(\
#     sales_id serial PRIMARY KEY,\
#     product_name int REFERENCES products(product_id) ON DELETE RESTRICT,\
#     unit_price  int REFERENCES products(product_id) ON DELETE RESTRICT,\
#     category_name  int REFERENCES categories(category_id) ON DELETE RESTRICT,\
#     sale_date TIMESTAMP, \
#     sale_quantity int, \
#     total_sale int, \
#     sale_made_by int REFERENCES app_users(user_id) ON DELETE RESTRICT)")


if __name__ == "__main__":
    # create_tables()
    database_connect_obj.create_tables()
    create_admin_user()

