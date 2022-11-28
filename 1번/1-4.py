import datetime
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='airshinta7@', db='coopang_eats', charset='utf8') 
cursor = conn.cursor() 


print("------1-4-------") # show restaurant name which don’t have ‘떡볶이’ in menu
v= input("음식 입력: ")
sql = "select restaurant_name from Restaurant as E where not exists(select * from Menu as M \
       where E.restaurant_id = M.restaurant_id and M.menu_name like '%%%s%%')" %(v)
cursor.execute(sql)
rows = cursor.fetchall()
for data in rows: 
    print(data)
