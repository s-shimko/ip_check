import psycopg2
import os

conn = psycopg2.connect("dbname=ip_base user=postgres password=postgres")
cur = conn.cursor()
cur.execute("select * from ips;")
result = cur.fetchall()

for i in result:
    print(i[1])
    status = os.system("ping -c1 -w2 " + i[1] + " > /dev/null 2>&1")
    if status == 0:
        print("UP")
    else:
        print("DOWN")

cur.close()
conn.close()
