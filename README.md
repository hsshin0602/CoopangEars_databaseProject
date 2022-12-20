# CoopangEats_databaseProject
# 데이터베이스 프로젝트

### 기능
- 로그인(회원id로만 가능하게)
- 회원가입(입력 형식에 맞지 않으면 다시 입력하도록)
- 주문기능(레스토랑 선택)
- 선택한 레스토랑에서 메뉴보고 담기
- 음식 주문하기(만약 최소 주문금액보다 주문금액이 적을 시, 음식을 더 추가해달라고 요청)
- 모든 기능에 돌아가기 버튼 구현
- 주문조회(주문한 총금액 확인가능)
- 로그아웃


### 설치
langauge: python
<pre>
<code>
 $ pip install pymysql
 $ pip install cryptography
</code>
</pre>

로그인,회원가입부터 시작하도록..!

## Todo Service
#### 1. When you first run system. You can choose between ‘login’ and ‘register’.
![image](https://user-images.githubusercontent.com/86701879/208558712-2d4f7b33-6d76-447e-8d45-f2d28083095c.png)

#### 2. login and register
![image](https://user-images.githubusercontent.com/86701879/208558740-4fe032cf-fdbe-471a-a8fc-0a8a735dafa6.png)
![image](https://user-images.githubusercontent.com/86701879/208558767-b143eaac-4ddd-40bf-98a9-b11c0f8f83ab.png)

#### 3. you can see list of the restaurants and their status. (open / close) 
![image](https://user-images.githubusercontent.com/86701879/208558901-9a3650cc-cc3b-44d6-88be-d95a2a14be2e.png)

#### 4. restaurant & menu choice
![image](https://user-images.githubusercontent.com/86701879/208558936-23b6feb1-d72e-40c4-90b6-1033959d5f15.png)
![image](https://user-images.githubusercontent.com/86701879/208558961-d68fc7ff-242d-4391-94ca-e476f43b5d4d.png)
![image](https://user-images.githubusercontent.com/86701879/208558969-1df3c23b-b862-4d79-9de4-e444b24a613a.png)

#### 5. If your total cost is higher than minimum cost, you can order your menus and you go back to the second page. However, if your total cost is lower than minimum cost, you cannot order your menus and you can get error message from system. Also, you can go back to the restaurant selection page by entering “0”.

< Success order : higher than minimum cost >

![image](https://user-images.githubusercontent.com/86701879/208559239-e513018e-1c00-4c91-b53f-05b0ba1590d6.png)
< Fail order : lower than minimum cost >

![image](https://user-images.githubusercontent.com/86701879/208559242-62dc64d7-a1aa-4bcb-b1ad-f9d0e4384890.png)
< Go back to the restaurant selection page >

![image](https://user-images.githubusercontent.com/86701879/208559283-2ddb75d6-9597-495d-9e8d-463abc4353c1.png)

#### 6. If you select “주문 조회” you can see the total amount of the order. When you enter ‘0’, you can go back to the second page.
< Before order : total cost 0원 >

![image](https://user-images.githubusercontent.com/86701879/208559330-25bf39f8-bf0b-439b-98c5-ab33c17a3aca.png)
< After order : total cost 15000원 >

![image](https://user-images.githubusercontent.com/86701879/208559340-393cf129-2e69-430d-8a56-b22cf8a36d22.png)

#### 7. logout
![image](https://user-images.githubusercontent.com/86701879/208559487-f9cbdcbb-72a6-49f3-9bc3-1bf2354f792f.png)











