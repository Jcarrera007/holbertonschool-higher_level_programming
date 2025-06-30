#!/usr/bin/python3
"""
Module for listing all states from database
"""

import MySQLdb
import sys


def main():
    """
    Main function to connect to database and list all states
    """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()