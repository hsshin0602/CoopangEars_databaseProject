import datetime
import pymysql

def total_cost(cursor):
    cursor.execute("call total_cost()")
    for result in cursor.fetchall():

        print(result)


if __name__ == '__main__':
    conn = pymysql.connect(user='root', password='airshinta7@', host='127.0.0.1', database='coopang_eats', charset='utf8') 
    cursor = conn.cursor() 
    
    cursor.execute("select GET_PRICE(%s);", (input("음식 이름 : "),))
    for data in cursor:
        print(data)

    cursor.close()
    conn.close() 