#!/usr/bin/python3
"""Script that lists all cities of a given state from the database
hbtn_0e_4_usa, safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Safe query using a parameterized input (SQL injection free)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch results and format output
    results = cursor.fetchall()
    print(", ".join([row[0] for row in results]))

    # Clean up
    cursor.close()
    db.close()
