#!/usr/bin/env python3
import psycopg2
import psycopg2.extras
import sys
import pprint
import os
import re

#line = sys.stdin.readlines()
#count = int((line[0].split("="))[1])
params = os.environ['QUERY_STRING']
count = 0
try:
    count = int((params.split("="))[1])
finally:
    if not count:
        print("Please input number!")
        sys.exit()
#print(count)

print("Content-type: text/html")
print("")
print("<HTML>")
print("<BODY>")
print("<PRE>")

col = 11

# if len(sys.argv) > 1:
#     count = int(sys.argv[1])
# else:
#     count = 10
    
str = "select solution from puzzle order by random() limit %d;" % count
#print(str);

def main():
    conn_string = "host='nfs.myopenshift.com' dbname='mydb' user='postgres' password='mysecret'"
    conn = psycopg2.connect(conn_string)
    #cursor = conn.cursor()
    cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(str)
    #records = cursor.fetchall()
    #pprint.pprint(records)
    for row in cursor:
        #print(repr(row))
        m = re.match(r'\[\'(.*)\'\]', repr(row))
        #m = re.match(r'(^.*$)', row)
        #print(m.group(1))
        s = m.group(1)
        for i in range(0, len(s), col):
            for ch in s[i:i+col]:
                print("%c " % ch, end='')
            print("")
        print("")


if __name__ == "__main__":
    main()

print("</PRE>")
print("</BODY>")
print("</HTML>")

