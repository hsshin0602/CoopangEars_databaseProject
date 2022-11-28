import datetime
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='airshinta7@', db='coopang_eats', charset='utf8') 
cursor = conn.cursor() 


print("------1-1-------")  # find user whose nickname is ‘사랑꾼’ from user table
sql = "SELECT * FROM user where user_nickname = %s"
v = input("nickname을 입력: ")
cursor.execute(sql, (v)) 
rows = cursor.fetchall()
for data in rows: 
    print(data)  


    


