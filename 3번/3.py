import datetime
import pymysql

def firstpage():    # 첫번째 페이지 : 회원가입 / 로그인
    print("********** Welcome to CoopangEats **********")
    print("1.로그인")
    print("2.회원가입")
    num = input("번호를 선택해 주세요 : ")
    print()
    
    if(num == '1'):
        while(1):
            check,user_id = login()
            if(check == 1): # 로그인 성공
                print("로그인 되었습니다")
                order_id = Insert_eatsorder(user_id) #로그인에 성공한 사용자의 주문목록 생성
                secondpage(user_id,order_id)
                break
            else:   # 로그인 실패
                print("존재하지 않는 아이디 또는 비밀번호가 틀렸습니다. 다시 로그인 해주세요.")
                need_reg = input("회원가입을 원하시면 y를 입력해주세요(y/n) : ")
                print()
                if(need_reg == 'y'):   
                    user_reg()
                    break
    elif(num == '2'): # 회원가입
        user_reg()
        return
    else:
        print("잘못된 번호입니다. 다시 선택해주세요")
        firstpage()
        return


def Insert_eatsorder(user_id): # 초기 eatsorder테이블 값 생성
    flg = init_flg()
    order_id = 3001
    while(flg): # order_id 중복체크
        flg = check_duplicate("order_id", str(order_id))  
        if(flg == 1):
            order_id+=1
    today = datetime.date.today()
    sql = "INSERT INTo EatsOrder VALUES(%s, %s, null, %s, 0, null)"
    cursor.execute(sql,(order_id,user_id,today))
    conn.commit()
    return order_id


def user_reg(): # 회원가입
    print("********** 회원가입 **********")
    flg = init_flg()
    user_id = 10
    while(flg): # user_id 중복체크
        flg = check_duplicate("user_id", str(user_id))  
        if(flg == 1):
            user_id+=1
    user_name = input("\n성함을 입력해주세요(ex.홍길동) : ")
    flg = init_flg()
    print()
    while(flg): # user_nickname 중복체크
        user_nickname = input("닉네임을 입력해주세요(ex.batman) : ")
        flg = check_duplicate("user_nickname", user_nickname)
        if(flg == 1):
            print(user_nickname + " 은/는 이미 존재하는 닉네임입니다. 다시 입력해주세요")
            print()
    flg = init_flg()
    print()        
    while(flg): # user_nickname 중복체크
        user_password = input("비밀번호를 입력해주세요(ex.password0) : ")
        flg = check_duplicate("user_password", user_password)
        if(flg == 1):
            print(user_password + " 은/는 이미 존재하는 닉네임입니다. 다시 입력해주세요")
    flg = init_flg()
    print()
    while(1):
        user_birth = input("생일을 입력해주세요(ex.2022-11-27) : ")
        type_date = validate_date(user_birth)
        if type_date:
            break
    flg = init_flg()
    print()
    while(flg): # user_phone_number 중복체크
        user_phone_number = input("휴대폰번호를 입력해주세요(ex.010-0000-0000) : ")
        flg = check_duplicate("user_phone_number", user_phone_number)
        if(flg == 1):
            print(user_phone_number + " 은/는 이미 존재하는 휴대폰번호입니다. 다시 입력해주세요")
            print()
            
    sure = input("회원가입하려면 y를 입력해주세요.(y/n) : ")
    if(sure == 'y'):
        print("\n회원가입 되었습니다. 반갑습니다.")   # 회원가입 성공
        sql = "INSERT INTO User VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (str(user_id),user_name,user_nickname,user_password,user_birth,user_phone_number))
        conn.commit()
        firstpage() # 초기페이지로 이동
        return
    else:
        print("\n회원가입에 실패했습니다.") # 회원가입 실패
        firstpage() # 초기페이지로 이동
        return


def validate_date(date_text):
	try:
		datetime.datetime.strptime(date_text,"%Y-%m-%d")
		return True
	except ValueError:
		print("잘못된 날짜형식입니다. YYYY-MM-DD형태로 입력해주세요.")
		return False


def check_duplicate(form, data):    # 회원가입 시 중복 확인 : 중복 시 flg 에 1 반환
    sql = sql_form(form)
    cursor.execute(sql, (data))
    data_exist = cursor.fetchall()

    if(data_exist == ()):
        return 0
    else:
        return 1
   
def sql_form(form): # SQL 접근시 어떤 attribute 에 접근할 것인지 확인
    if(form == "user_id"):
        return "SELECT user_id FROM User WHERE user_id = %s"
    elif(form == "user_nickname"):
        return "SELECT user_nickname FROM User WHERE user_nickname = %s"
    elif(form == "user_phone_number"):
        return "SELECT user_phone_number FROM User WHERE user_phone_number = %s"
    elif(form == "order_id"):
        return "SELECT order_id FROM EatsOrder WHERE order_id = %s"
    elif(form == "orderlist_id"):
        return "SELECT orderlist_id FROM EatsOrderMenu WHERE orderlist_id = %s"
    elif(form == "user_password"):
        return "SELECT user_password FROM User WHERE user_password = %s"
    else:
        return

def init_flg(): # flg 초기화
    return 1

def login():    # 로그인 화면
    print("********** 로그인 **********")
    user_id = input("ID : ")
    user_pwd = input("PASSWORD : ")
    
    sql_id = "SELECT user_id FROM User WHERE user_nickname = %s"
    sql_pwd = "SELECT user_id FROM User WHERE user_password = %s"
    cursor.execute(sql_id, (user_id))
    data_id = cursor.fetchall()
    cursor.execute(sql_pwd, (user_pwd))
    data_pwd = cursor.fetchall()
        
    if(data_id[0] == data_pwd[0]) and data_id != () and data_pwd != ():   # 올바른 ID / Password 인지 확인
        return 1, data_id[0]
    else:
        return 0, data_id[0]

    
def secondpage(user_id,order_id):   # 두번째 페이지 : 매장 검색 /  주문 조회 / 로그아웃
    print("\n********** Welcome to CoopangEats **********")
    print("1.주문 가능한 매장 보기")
    print("2.주문 조회")
    print("3.로그아웃")
    work = input("번호를 선택해 주세요 : ")
    
    while(1):
        if(work == "1"):    # 매장 검색
            show_restaurant(user_id,order_id)
            break
        elif(work == "2"):  # 주문 조회
            show_order_list(user_id,order_id)
            break
        elif(work == "3"):  # 로그아웃
            print("로그아웃 되었습니다.\n")
            firstpage() # 초기페이지로 이동
        else:
            work = input("번호를 다시 선택해 주세요 : ")
        
    
def show_restaurant(user_id,order_id):  # 주문 가능한 매장을 보여줌
    print('\n'+ "******** Restaurant Chioce ***********")
    idx=0
    arr =[]
    name1=[]
    sql = "select Restaurant_name, Restaurant_status from Restaurant"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for data in rows: 
        idx+=1
        res_name = str(idx) +'. '+ data[0]+'  '+data[1] # 주문 가능한 레스토랑 목록
        name1.append(res_name) # ex 1. 엽기떡볶이 open
        arr.append([data[0],data[1],idx]) # 가게 이름 / 상태 / 번호
       
    
    flg=True
    while(flg):
        for a in name1:
            print(a)
        name = input('가게를 선택해 주세요(가게번호도 가능) : ') # 가게이름 or 가게반호로 가게 선택하기
        count=0
        for o in arr:
            if flg: # 원하는 값을 찾았는지 확인 
                if name == o[0] or name == str(o[2]):
                    if 'open' == o[1]:
                        if name == o[0]:
                            print(name + '를 선택하였습니다.')
                            print()
                            res_select = name
                            flg=False
                            break
                        elif name == str(o[2]):
                            print('\n'+o[0] + '를 선택하였습니다.')
                            print()
                            res_select = o[0]
                            flg=False
                            break

                    elif 'close' == o[1]:
                        print("현재 미운영중입니다. 다른 가게를 선택해 주세요.\n") # 존재하지만 close 상태인 가게
                else:
                    count+=1  
        if(count == idx):   # 입력이 잘못된 경우
            print("잘못된 입력입니다. 다시 입력해주세요.\n") 
        
    menu_choise(res_select,user_id,order_id) # 선택한 가게의 메뉴판 보기
    

def menu_choise(res_select, user_id, order_id):
    print_res(res_select)
    menu_info = show_menu(res_select)   # 메뉴판을 보여줌
    menu_count = menu_info[-1][2]   # 메뉴의 갯수
    total_order_cost=0
    min_cost = return_min_cost(res_select)  # 레스토랑 최소 주문 금액 
    print_min_cost(res_select)    
    num = int(input("메뉴를 선택해주세요(돌아가기 : 0, 주문하기 : %d) : " % (menu_count + 1)))  # 0번 입력시 이전단계로 돌아감

    while(1):
        if(num == 0):   # 두번째 페이지로 이동
            total_order_cost=0
            show_restaurant(user_id, order_id)
            break
        elif(num > 0 and num <= menu_count):    # 메뉴 선택
            for data in menu_info:
                if num == data[2]:
                    menu_select = data[0]   # 메뉴이름
                    order_cost = data[1]
                    count, menu_id = order_menu(data, menu_select, res_select, user_id)  # 주문한 가격
                    Insert_eatsordermenu(order_id, menu_id,order_cost,count)
            total_order_cost += (int(order_cost)*int(count))
            sql = "UPDATE EatsOrder SET order_total_cost = %s"
            cursor.execute(sql,total_order_cost)
            conn.commit()
            print_res(res_select)
            menu_info = show_menu(res_select)   # 메뉴 보여주기
            print_min_cost(res_select)
            print("현재 주문금액은 : "+ str(total_order_cost) + "원 입니다.")  # 현재 주문금액
            num = int(input("메뉴를 선택해주세요(돌아가기 : 0, 주문하기 : %d) : " % (menu_count + 1)))
        elif(num == menu_count + 1):
            if min_cost <= total_order_cost:
                print("주문에 성공하였습니다. 총 주문 금액은 %d원 입니다" %(total_order_cost))    # 주문금액이 최소금액을 초과하면 주문성공
                secondpage(user_id,order_id)    # 주문성공시 두번째 페이지로 이동
            else:
                print("최소주문금액을 확인해주세요. %d원이 부족합니다." %(min_cost - total_order_cost))
                print()
                print_res(res_select)
                menu_info = show_menu(res_select)
                print_min_cost(res_select)
                print("현재 주문금액은 : "+ str(total_order_cost) + "원 입니다.")
                num = int(input("메뉴를 선택해주세요(돌아가기 : 0, 주문하기 : %d) : " % (menu_count + 1)))
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.\n")
            print_res(res_select)
            menu_info = show_menu(res_select)
            print_min_cost(res_select)
            print("현재 주문금액은 : "+ str(total_order_cost) + "원 입니다.")
            num = int(input("메뉴를 선택해주세요(돌아가기 : 0, 주문하기 : %d) : " % (menu_count + 1)))

def print_res(res_select):
    print("********** " + res_select + " **********")
    return

def order_menu(data, menu_select, res_select, user_id): # 주문 수량, menu_id 리턴
    print("\n선택한 음식 :  " + menu_select)
    sql = "SELECT menu_id FROM Menu WHERE menu_name = %s"
    cursor.execute(sql,menu_select)
    menu_num = cursor.fetchall()
    for n in menu_num:
        menu_id = n[0]
    num = int(input("주문할 수량을 선택해주세요(취소 : 0) : "))
    print()
    while(1):
        if num == 0:
            menu_choise(res_select,user_id)
        elif 0 < num and num < 100: 
            return num, menu_id


def Insert_eatsordermenu(order_id, menu_id, order_cost,conut): 
    flg = init_flg()
    orderlist_id = 5001
    while(flg): # orderlist_id 중복체크
        flg = check_duplicate('orderlist_id' , str(orderlist_id))  
        if(flg == 1):
            orderlist_id+=1
    sql = "INSERT INTO Eatsordermenu VALUES(%s,%s,%s, %s, %s)"
    cursor.execute(sql,(orderlist_id,order_id,menu_id,conut,order_cost))
    conn.commit()


def return_min_cost(res_select):
    sql = "select restaurant_min_cost from restaurant where restaurant_name = %s"
    cursor.execute(sql, res_select)
    rows = cursor.fetchall()
    for data in rows:
        return data[0]
    print_min_cost()

def print_min_cost(res_select):
    print("최소 주문금액은 " + str(return_min_cost(res_select)) + "원 입니다.")

def show_menu(res_select):
    idx2 = 0
    arr2 = []   # 이름, 가격, 메뉴번호 담을 리스트
    sql = "select Menu_name, Menu_price, Menu_description from Menu natural join restaurant where restaurant_name=%s"
    cursor.execute(sql,res_select)
    rows = cursor.fetchall()
    for data in rows: 
        idx2 += 1
        menu_name = str(idx2) +'. '+ data[0]+'  '+data[1]+ "  " + data[2] # 현재 존재하는 레스토랑 목록
        arr2.append([data[0],data[1],idx2])
        print(menu_name)
    
    return arr2  # 리스트 반환

def show_order_list(user_id,order_id):
    sql = "SELECT user_nickname, order_total_cost FROM User NATURAL JOIN EatsOrder WHERE user_id = %s and order_id=%s"
    cursor.execute(sql,(user_id,order_id))
    c = cursor.fetchall()
    if c == ():
        print('총 주문금액은 0원입니다.')
    else:
        print("총 주문금액은 " +str(c[0][1]) + '원 입니다.')

    inp = input("돌아가기(0) :")
    if inp == str(0):
        secondpage(user_id, order_id)
    else:
        secondpage(user_id, order_id)
    

if __name__ == '__main__':
    conn = pymysql.connect(user='root', password='airshinta7@', host='127.0.0.1', database='coopang_eats', charset='utf8') 
    cursor = conn.cursor() 
    firstpage()

    cursor.close()
    conn.close() 
    