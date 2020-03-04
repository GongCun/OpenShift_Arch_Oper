#!/usr/bin/env python3
import psycopg2
import sys
import pprint


def main():
    conn_string = "host='nfs.myopenshift.com' dbname='mydb' user='postgres' password='mysecret'"

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    cursor.execute("select count(*) from puzzle;")
    records = cursor.fetchone()
    pprint.pprint(records)


if __name__ == "__main__":
    main()

