#!/usr/bin/env python3
import psycopg2
import psycopg2.extras
import sys
#import pprint


def main():
    conn_string = "host='nfs.myopenshift.com' dbname='mydb' user='postgres' password='mysecret'"

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute("delete from puzzle;")
    cursor.copy_from(sys.stdin, table='puzzle', columns=('solution',))
    conn.commit()
    count = cursor.rowcount
    print("Copy", count, "records") 


if __name__ == "__main__":
    main()

