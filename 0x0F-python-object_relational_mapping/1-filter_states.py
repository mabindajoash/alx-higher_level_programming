#!/usr/bin/python3
"""module to list all states with a name starting with N"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    state_rows = cur.fetchall()
    for row in state_rows:
        print(row)
    cur.close()
    conn.close()
