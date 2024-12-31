#!/usr/bin/python3
"""module to list cities in ascending order"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
    """, (sys.argv[4],))
    state_rows = cur.fetchall()
    print(", ".join(row[0] for row in state_rows))
    cur.close()
    conn.close
