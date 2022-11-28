import datetime
import pymysql

def food1_cost(cursor):
    cursor.execute("call food1_cost()")
    for result in cursor.fetchall():
        print(result[0])


if __name__ == '__main__':
    conn = pymysql.connect(user='root', password='airshinta7@', host='127.0.0.1', database='coopang_eats', charset='utf8') 
    cursor = conn.cursor() 
    
    food1_cost(cursor)

    cursor.close()
    conn.close() 


'''
import datetime
import pymysql


conn = pymysql.connect(host='localhost', user='root', password='airshinta7@', db='coopang_eats', charset='utf8') 
cursor = conn.cursor() 

def max_price():
    return "SELECT sum(order_total_cost) FROM eatsorder"

sql = max_price()
cursor.execute(sql)
rows = cursor.fetchall()
for data in rows:
    print(data)

cursor.close()'''