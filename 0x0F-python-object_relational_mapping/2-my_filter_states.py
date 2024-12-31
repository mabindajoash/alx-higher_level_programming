#!/usr/bin/python3
"""module that takes in an argument and
returns the state matching the argument"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    state_rows = cur.fetchall()
    for row in state_rows:
        print(row)
    cur.close()
    conn.close
