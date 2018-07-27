# FileName : pyConnPg_practice.py
# Author   : Adil
# DateTime : 2018/7/27 16:04
# SoftWare : PyCharm



import psycopg2

conn = psycopg2.connect(database='bike_report',user='bike_report_rw',password='bike_report_rw',host='101.37.152.70',port='3503')


print(conn)

cur = conn.cursor()

sqltest = "select * from t_app_loadtime limit 1"

cur.execute(sqltest)

rows = cur.fetchone()

print(rows)

conn.close()





