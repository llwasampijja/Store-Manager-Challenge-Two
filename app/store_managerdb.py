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
        username varchar UNIQUE, \
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
        category int REFERENCES categories(id) ON DELETE RESTRICT,\
        quantity int)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS sales(\
        id serial PRIMARY KEY,\
        sales_id varchar UNIQUE,\
        product_name int REFERENCES products(id) ON DELETE RESTRICT,\
        unit_price  int REFERENCES products(id) ON DELETE RESTRICT,\
        category  int REFERENCES categories(id) ON DELETE RESTRICT,\
        sale_date TIMESTAMP, \
        sale_quantity int, \
        total_sale int, \
        sale_made_by int REFERENCES app_users(id) ON DELETE RESTRICT)")

        # self.cursor_db.close()
        # self.db_connect.close()

    def insert_data_users(self, user_id, user_name, username, password, user_role):
        sql_query = "INSERT INTO app_users(user_id, user_name, username, password, \
        user_role) VALUES ('{}', '{}','{}', '{}', '{}')".format(user_id, user_name, \
        username, password, user_role)
        self.cursor_db.execute(sql_query)

    def insert_data_categories(self, category_id, category_name):
        sql_query = "INSERT INTO categories(category_id, category_name) VALUES('{}',{})"\
        .format(category_id, category_name)
        self.cursor_db.execute(sql_query)

    def insert_data_products(self, product_id, product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category):
        sql_query = "INSERT INTO products(product_id, product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category) VALUES('{}','{}','{}','{}',\
        '{}','{}',SELECT id from categories WHERE category_name='{}')".format(category,\
         product_id, product_name, unit_price, minimum_quantity,stock_date, quantity)
        self.cursor_db.execute(sql_query)

    def insert_data_sales(self, sales_id, product_name, unit_price, category, sale_date, \
        sale_quantity, total_sale, sale_made_by):
        sql_query = "INSERT INTO sales(sales_id, product_name, unit_price, category, sale_date, \
        sale_quantity, total_sale, sale_made_by) VALUES('{}',SELECT id from products WHERE \
        product_name='{}', SELECT id from products WHERE product_name='{}', SELECT id from \
        categories WHERE category_name='{}', '{}', '{}', '{}', SELECT id \
        from app_users WHERE username='{}')".format(sales_id, product_name, unit_price, \
        category, sale_date, sale_quantity, total_sale, sale_made_by)
        self.cursor_db.execute(sql_query)

    
    def get_data_users(self):
        pass
    # def insert_data_products(self):
    #     sql_query = "INSERT INTO products(product_id, product)"
    #     self.cursor_db = self.db_connect.connect()

        




