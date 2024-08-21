import sqlite3

def creat_table(db_file, sql):
    with sqlite3.connect(db_file) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except sqlite3.Error as error:
            print(error)

sql_to_creat_products_table = """
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL DEFAULT '0.0',
quantity INTEGER NOT NULL DEFAULT '0')
"""

def insert_product(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = """ INSERT INTO products (product_title, price, quantity)
            VALUES (?, ?, ?)
            """
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def update_quantity(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = """ UPDATE products SET quantity = ? WHERE id = ?
            """
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def update_price(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = """
            UPDATE products SET price = ? WHERE id = ?"""
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def delete_product(db_file, id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as error:
            print(error)

def select_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

def select_products(db_file, limit):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
            cursor = connection.cursor()
            cursor.execute(sql, limit)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

def search_products_by_title(db_file, product_title):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = """SELECT * FROM products WHERE product_title LIKE ?
            """
            cursor = connection.cursor()
            cursor.execute(sql, ('%' + product_title + '%',))
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)

db_name = 'products.db'
creat_table(db_name, sql_to_creat_products_table)
# insert_product(db_name, ("молоко", 72.2, 12))
# insert_product(db_name, ('кефир', 75.5, 8))
# insert_product(db_name, ("яйца", 15.4, 120))
# insert_product(db_name,('горький шоколад', 156.9, 35))
# insert_product(db_name, ('молочный шоколад', 115.86, 40))
# insert_product(db_name, ("печенье день и ночь", 306.36, 5))
# insert_product(db_name, ("cтиральный порошок (ручная стирка)", 350.5, 7))
# insert_product(db_name, ('cтиральный порошок (автомат)', 335.8, 9))
# insert_product(db_name, ('мука первый сорт', 91.0, 13))
# insert_product(db_name, ('мука высший сорт', 120.33, 17))
# insert_product(db_name, ('рис байдала', 140.2, 15))
# insert_product(db_name, ('рис камолина', 165.89, 24))
# insert_product(db_name, ('рис краснодарский', 174.0, 13))
# insert_product(db_name, ('хозяйственное мыло', 63.0, 6))
# insert_product(db_name, ('жидкое мыло', 180.6, 3))

# update_quantity(db_name, (15, 2))
# update_price(db_name, (87.7, 9))
# delete_product(db_name, 6)
# search_products_by_title(db_name, 'рис')
# select_products(db_name, (100, 10))

# select_all_products(db_name)

