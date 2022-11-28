import datetime
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='airshinta7@', db='coopang_eats', charset='utf8') 
cursor = conn.cursor() 


print("------1-2-------") # show restaurant name which address is 충무로 or 동대문
sql = "(select Restaurant.restaurant_name from Restaurant where restaurant_address = %s) \
    union (select Restaurant.restaurant_name from Restaurant where restaurant_address = %s) "
v,m = input("음식점 위치를 두곳 입력: ").split()
cursor.execute(sql, (v, m))
rows = cursor.fetchall()
for data in rows: 
    print(data) 
