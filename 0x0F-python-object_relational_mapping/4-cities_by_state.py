#!/usr/bin/python3
"""module to list cities in ascending order"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities JOIN states
        ON cities.state_id = states.id
    """)
    state_rows = cur.fetchall()
    for row in state_rows:
        print(row)
    cur.close()
    conn.close
