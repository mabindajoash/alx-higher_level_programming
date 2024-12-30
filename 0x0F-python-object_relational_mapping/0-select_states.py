#!/usr/bin/python3
"""module for listing all states"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    state_rows = cur.fetchall()
    for row in state_rows:
        print(row)
    cur.close()
    db.close()
