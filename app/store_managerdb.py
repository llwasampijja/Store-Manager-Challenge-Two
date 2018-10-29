import psycopg2

class DatabaseConnect():
    def __init__(self, **kwargs):
        self.db_connect = psycopg2.connect(\
    "dbname='store_manager_db' \
    user='andela' \
    host='localhost' \
    password='bootcamp'")
        self.db_connect.autocommit = True

        self.cursor_db = self.db_connect.cursor()
    
    def drop_tables(self):
        self.cursor_db.execute("DROP TABLE")
    
    def create_tables(self):
        """create users table"""
        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS app_users(\
        id serial PRIMARY KEY, \
        user_id varchar, \
        user_name varchar, \
        username varchar, \
        password varchar(16),\
        user_role varchar)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS categories(\
        id serial PRIMARY KEY, \
        category_id varchar, \
        category_name varchar)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS products(\
        id serial PRIMARY KEY, \
        product_id varchar, \
        product_name varchar, \
        unit_price int, \
        minimum_quantity int, \
        stock_date TIMESTAMP, \
        category int4 REFERENCES categories(category_id) ON DELETE RESTRICT,\
        quantity int)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS sales(\
        id serial PRIMARY KEY,\
        sales_id varchar UNIQUE,\
        product_name int4 REFERENCES products(product_id) ON DELETE RESTRICT,\
        unit_price  int4 REFERENCES products(product_id) ON DELETE RESTRICT,\
        category  int4 REFERENCES categories(category_id) ON DELETE RESTRICT,\
        sale_date TIMESTAMP, \
        sale_quantity int, \
        total_sale int, \
        sale_made_by int4 REFERENCES app_users(user_id) ON DELETE RESTRICT)")

        self.cursor_db.close()
        self.db_connect.close()

        
        




