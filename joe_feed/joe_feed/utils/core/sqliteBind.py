import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
# -----------------------------------------------
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
# -----------------------------------------------
def insert_item(conn, insert_sql, item):
    """
    return id integer
    """
    cur = conn.cursor()
    cur.execute(insert_sql, item)
    conn.commit()
    return cur.lastrowid
# -----------------------------------------------
def select_items(conn, table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows
# -----------------------------------------------
def select_items_by_property(conn, table, p,v):
    cur = conn.cursor()
    sqlselect = f"""SELECT * FROM {table} WHERE {p}="{v}"
    """
    cur.execute(sqlselect)
    rows = cur.fetchall()
    return rows
