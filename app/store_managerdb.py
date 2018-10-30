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
        user_id serial PRIMARY KEY, \
        user_name varchar, \
        username varchar UNIQUE, \
        password varchar(16),\
        user_role varchar)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS categories(\
        category_id serial PRIMARY KEY, \
        category_name varchar UNIQUE)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS products(\
        product_id serial PRIMARY KEY, \
        product_name varchar UNIQUE, \
        unit_price int, \
        minimum_quantity int, \
        stock_date varchar, \
        category_name int REFERENCES categories(category_id) ON DELETE RESTRICT,\
        quantity int)")

        self.cursor_db.execute("CREATE TABLE IF NOT EXISTS sales(\
        sales_id serial PRIMARY KEY,\
        product_name int REFERENCES products(product_id) ON DELETE RESTRICT,\
        unit_price  int REFERENCES products(product_id) ON DELETE RESTRICT,\
        category  int REFERENCES categories(category_id) ON DELETE RESTRICT,\
        sale_date TIMESTAMP, \
        sale_quantity int, \
        total_sale int, \
        sale_made_by int REFERENCES app_users(user_id) ON DELETE RESTRICT)")

    def insert_data_users(self, user_name, username, password, user_role):
        sql_query = "INSERT INTO app_users(user_name, username, password, \
        user_role) VALUES ('{}','{}', '{}', '{}')".format(user_name, \
        username, password, user_role)
        self.cursor_db.execute(sql_query)

    def insert_data_categories(self, category_name):
        sql_query = "INSERT INTO categories(category_name) VALUES('{}')"\
        .format( category_name)
        self.cursor_db.execute(sql_query)

    def get_id_foreign_categories(self, category_name):
        category_query = """SELECT category_id FROM categories WHERE category_name = '{}'""".format(category_name)
        self.cursor_db.execute(category_query)
        result = self.cursor_db.fetchone()
        return result[0]

    def get_id_foreign_products(self, product_name):
        product_query = """SELECT product_id FROM products WHERE product_name = '{}'""".format(product_name)
        self.cursor_db.execute(product_query)
        result = self.cursor_db.fetchone()
        return result[0]

    def get_id_foreign_users(self, username):
        user_query = """SELECT user_id FROM app_users WHERE username = '{}'""".format(username)
        self.cursor_db.execute(user_query)
        result = self.cursor_db.fetchone()
        return result[0]

    def insert_data_products(self, product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category_name):
        category_id_foreign = self.get_id_foreign_categories(category_name)

        sql_query = "INSERT INTO products( product_name, unit_price,\
        minimum_quantity, stock_date, quantity, category) VALUES('{}','{}','{}',\
        '{}','{}', '{}')"\
        .format(product_name, unit_price, minimum_quantity,stock_date, quantity, category_id_foreign)
        self.cursor_db.execute(sql_query)

    def insert_data_sales(self, product_name, unit_price, category, sale_date, category_name,
        sale_quantity, total_sale, sale_made_by):
        category_id_foreign = self.get_id_foreign_categories(category_name)
        product_id_foreign = self.get_id_foreign_products(product_name)
        username_id_foreign = self.get_id_foreign_users(sale_made_by)

        



        sql_query = "INSERT INTO sales(product_name, unit_price, category, sale_date, \
        sale_quantity, total_sale, sale_made_by) VALUES('{}','{}','{}', '{}', '{}', '{}','{}')"\
        .format( product_id_foreign, product_id_foreign, category_id_foreign, sale_date, \
        sale_quantity, total_sale, username_id_foreign)
        self.cursor_db.execute(sql_query)

    def get_data_categories(self):
        sql_query = """SELECT * FROM categories"""
        self.cursor_db.execute(sql_query)
        
    def get_data_products(self):
        sql_query = """SELECT * FROM products"""
        self.cursor_db.execute(sql_query)

    def get_data_sales(self):
        sql_query = """SELECT * FROM sales"""
        self.cursor_db.execute(sql_query)

    def get_data_product_byindex(self, product_id):
        sql_query = """SELECT product_name FROM products WHERE product_id = '{}'""".format(product_id)
        self.cursor_db.execute(sql_query)

    def get_data_sale_byindex (self, sale_id):
        sql_query = """SELECT sale_name FROM sales WHERE sale_id = '{}'""".format(sale_id)
        self.cursor_db.execute(sql_query)

    def get_data_category_byid(self, category_id):
        sql_query = """SELECT category_name FROM categories WHERE category_id = '{}'""".format(category_id)
        self.cursor_db.execute(sql_query)

    def update_data_product(self, product_name, product_id):
        sql_query = """UPDATE products SET product_name = '{}' WHERE \
        product_id = '{}'""".format(product_name, product_id)
        self.cursor_db.execute(sql_query)

    def update_data_categories(self, category_name, category_id):
        sql_query = """UPDATE categories SET category_name = '{}' WHERE category_id = '{}'""".format(category_name, category_id)
        self.cursor_db.execute(sql_query)

    def delete_data_product(self, product_id):
        sql_query = """DELETE FROM products WHERE product_id = '{}'""".format(product_id)
        self.cursor_db.execute(sql_query)

    def delete_data_categories(self, category_id):
        sql_query = """DELETE FROM categories WHERE category_id = '{}'""".format(category_id)
        self.cursor_db.execute(sql_query)
    


    # def insert_data_products(self):
    #     sql_query = "INSERT INTO products(product_id, product)"
    #     self.cursor_db = self.db_connect.connect()