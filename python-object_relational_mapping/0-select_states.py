#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the results
    rows = cursor.fetchall()
    
    # Print each row
    for row in rows:
        print(row)
    
    # Close the cursor and the connection
    cursor.close()
    db.close()
