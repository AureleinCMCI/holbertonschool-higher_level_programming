#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)

    # Create cursor
    cur = db.cursor()

    # Execute SQL query to fetch states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    cur.execute(query)

    # Fetch and display results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Clean up
    cur.close()
    db.close()
