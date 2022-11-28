import datetime
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='airshinta7@', db='coopang_eats', charset='utf8') 
cursor = conn.cursor() 


print("------1-3-------") # show user who lives in ‘중구 장충로’
sql = "select * from User as U, Address as A where U.user_id = A.user_id and A.address_address in \
    (select address_address from Address where address_address = %s)"
v= input("살고있는 주소 입력: ")
cursor.execute(sql, (v))
rows = cursor.fetchall()
for data in rows: 
    print(data)