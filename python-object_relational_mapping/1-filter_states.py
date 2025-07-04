#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute query with case-sensitive filter using LIKE BINARY
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
