"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

def customer_tickets(conn, customer_id):

    query = """SELECT 
    films.title, screenings.screen, tickets.price
    FROM 
    films JOIN screenings
    ON films.film_id = screenings.film_id
    JOIN tickets
    ON screenings.screening_id = tickets.screening_id
    WHERE customer_id = ?
    ORDER BY films.title;
    """
    cursor.execute(query, (customer_id,))
    rows = cursor.fetchall()
    return rows
    
    conn.close()

    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """


def screening_sales(conn):

    query = """SELECT
    screenings.screening_id, films.title, COUNT(ticket_id) AS tickets_sold
    FROM 
    films JOIN screenings
    ON films.film_id = screenings.film_id
    LEFT JOIN tickets
    ON screenings.screening_id = tickets.screening_id
    GROUP BY screenings.screening_id, films.title
    ORDER BY tickets_sold DESC;"""
    
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
    
    conn.close()

    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """



def top_customers_by_spend(conn, limit):

    query = """SELECT
    customers.customer_name, SUM(tickets.price) AS total_spent
    FROM 
    customers JOIN tickets
    ON customers.customer_id = tickets.customer_id
    GROUP BY customers.customer_id
    ORDER BY total_spent DESC
    LIMIT ?;""" 
    cursor.execute(query, (limit,))
    rows = cursor.fetchall()
    return rows
    
    conn.close()

    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """

