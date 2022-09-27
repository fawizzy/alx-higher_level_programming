#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('''
        SELECT cities.name FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name LIKE %s
        ORDER BY cities.id
    ''', [sys.argv[4]])
    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))
    cursor.close()
    db.close()