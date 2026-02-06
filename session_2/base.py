import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl


def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect("orders.db")

    conn.row_factory = sqlite3.Row

    return conn

def main():

    db = get_connection()

    query = """SELECT orders.customer_id,
    order_items.quantity * products.price AS TotalSpend
    FROM 
    orders JOIN order_items
    ON orders.order_id = order_items.order_id
    JOIN products
    ON order_items.product_id = products.product_id 
    GROUP BY orders.customer_id
    ORDER BY TotalSpend DESC LIMIT 5;"""


    cursor = db.cursor()

    for row in cursor.execute(query):
        print(list(row))

    db.close()


if __name__=="__main__":
    main()
