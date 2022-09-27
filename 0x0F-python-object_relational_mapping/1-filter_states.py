#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    print(sys.argv[4])
    cursor.execute("""
        SELECT * FROM states 
        WHERE name LIKE 'N%s'
    """)
    states = cursor.fetchall()
    [print(state) for state in states]