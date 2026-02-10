"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3

DB_PATH = "tickets.db"

def get_connection(db_path="tickets.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect("tickets.db")

    conn.row_factory = sqlite3.Row

    return conn

# the query is treated as a 'string', not a query
def customer_tickets(conn, customer_id):
    db = get_connection()
    conn.row_factory = sqlite3.Row
    query = """SELECT 
    films.title, screenings.screen, tickets.price
    FROM 
    films JOIN screenings
    ON films.film_id = screenings.film_id
    JOIN tickets
    ON screenings.screening_id = tickets.screening_id
    ORDER BY films.title;
    """
    cursor = db.cursor()  

    for row in cursor.execute(query):
        return(list(row))
    
    db.close()
    


    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """


def screening_sales(conn):

    db = get_connection()

    query = """SELECT
    screenings.screening_id, films.title, COUNT(ticket_id) AS tickets_sold
    FROM 
    films JOIN screenings
    ON films.film_id = screenings.screening_id
    JOIN tickets
    ON screenings.screening_id = tickets.ticket_id
    ORDER BY tickets_sold DESC;"""
    
    cursor = db.cursor()

    for row in cursor.execute(query):
        return(row)
    
    db.close()

    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """



def top_customers_by_spend(conn, limit):
    
    db = get_connection()
    query = """SELECT
    customers.customer_name, SUM(tickets.price) AS total_spent
    FROM 
    customers JOIN tickets
    ON customers.customer_id = tickets.customer_id
    GROUP BY customers.customer_id
    ORDER BY total_spend LIMIT limit DESC
    WHERE total_spent > 0;"""
    
    cursor = db.cursor()

    for row in cursor.execute(query):
        return(list(row))
    
    db.close()
    
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

