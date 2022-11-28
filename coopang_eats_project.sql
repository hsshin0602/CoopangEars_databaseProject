create database coopang_eats;
use coopang_eats;
create table User(
	user_id varchar(20),
    user_name varchar(20) not null,
    user_nickname varchar(20),
    user_password varchar(20) not null,
    user_birth date,
    user_phone_number varchar(20),
    Primary key(user_id));
    
create table Address(
	address_id varchar(20),
	user_id varchar(20),
    address_address varchar(20),
    address_details varchar(20),
    Primary key(address_id),
    foreign key(user_id) references User(user_id));
    
create table EatsOrder(
	order_id varchar(20),
    user_id varchar(20),
    address_id varchar(20),
    order_date date,
    order_total_cost int(20), 
    order_request varchar(20),
    Primary key(order_id),
    foreign key(user_id) references User(user_id),
    foreign key(address_id) references Address(address_id));
    
create table Restaurant(
	restaurant_id varchar(20),
    restaurant_name varchar(20),
    restaurant_address varchar(20),
    restaurant_phone_number varchar(20),
    restaurant_status varchar(20),
    restaurant_min_cost int(20),
    Primary key(restaurant_id));

create table Menu(
	menu_id varchar(20),
    restaurant_id varchar(20),
    menu_name varchar(20) not null,
    menu_description varchar(20),
    menu_price varchar(20) not null,
    # menu_count int,
    Primary key(menu_id),
    foreign key(restaurant_id) references Restaurant(restaurant_id));
    
create table EatsOrderMenu(
	orderlist_id varchar(20),
    order_id varchar(20),
    menu_id varchar(20),
    orderlist_count int,
    orderlist_cost int,
    Primary key(orderlist_id),
    foreign key(order_id) references EatsOrder(order_id),
    foreign key(menu_id) references Menu(menu_id));

show tables;

insert into User values('1', '신현식', '투슬리스', 'password1', '1999-06-02','010-1234-1234');
insert into User values('2', '백하늘', '사랑꾼', 'password2', '1998-11-03','010-1236-1234');
insert into User values('3', '최환', '난봉꾼', 'password3', '1998-11-04','010-1274-1134');
select * from User;

insert into Restaurant values('1001','엽기떡볶이','동대문', '010-1111-1111','open','14000');
insert into Restaurant values('1002','bhc 치킨','충무로', '010-2222-2222','open','17000');
insert into Restaurant values('1003','맥도날드','명동', '010-3333-3333','close','12000');
insert into Restaurant values('1004','굽네치킨','충무로', '010-4444-4444','open','17000'); 
insert into Restaurant values('1005','피자마루','장충동', '010-5555-5555','open','13000'); 
insert into Restaurant values('1006','동국반점','회현', '010-6666-6666','open','12000'); 
select * from Restaurant;

insert into Address values('2001', '1','중구 동호로', '1동 1호');
insert into Address values('2002', '2','중구 장충로', '2동 2호');
insert into Address values('2003', '3','중구 장충로', '3동 3호');
select * from Address;
    
insert into Menu values('4001','1001','매운 떡볶이','많이 매운 떡볶이입니다', 14000);
insert into Menu values('4002','1001','로제 떡볶이','로제 떡볶이입니다', 15000);
insert into Menu values('4003','1001','크림 떡볶이','크리미한 떡볶이입니다', 15000);
insert into Menu values('4004','1002','뿌링클','치즈맛 치킨입니다', 18000);
insert into Menu values('4008','1002','맛쵸킹','달달하면서 매콤한 치킨입니다', 18000);
insert into Menu values('4009','1002','치즈볼','쫄듯한 치즈볼입니다', 5000);


insert into Menu values('4005','1003','빅맥','큰 버거입니다', 6500);
insert into Menu values('4010','1003','더블 불고기버거','패티가 2개인 버거입니다', 5500);
insert into Menu values('4011','1003','감자튀김','짭잘합니다', 2500);
insert into Menu values('4012','1003','콜라','콜라', 2000);

insert into Menu values('4006','1004','고추 바사삭','매콤한 치킨입니다', 18000); 
insert into Menu values('4007','1004','치즈 떡볶이','치킨과 곁들어 먹는 떡볶이입니다', 6500); 
insert into Menu values('4013','1004','갈비천왕','갈비맛 치킨입니다', 17000);
insert into Menu values('4014','1004','볼케이노','많이 매콤한 치킨입니다', 18000);
insert into Menu values('4015','1004','콜라','콜라', 2000);

insert into Menu values('4016','1005','치즈피자','치즈가 듬뿍들어간 피자입니다', 12000);
insert into Menu values('4017','1005','불고기피자','볼고기맛 피자입니다', 9000);
insert into Menu values('4018','1005','포테이토피자','감자와 베이컨이 들어간 피자입니다', 10000);

insert into Menu values('4019','1006','짜장면','짜장면입니다', 6500);
insert into Menu values('4020','1006','짬뽕','많이 맵습니다', 7000);
insert into Menu values('4021','1006','탕수육','찹쌉 탕수육입니다', 13000);
select * from Menu;

select * from eatsorder;
select * from eatsordermenu;

## 1. use where
select * 
from user
where user_nickname = '사랑꾼';

select EatsOrder.user_id
from EatsOrder
where order_total_cost >25000;

## 2. more than one tables in from

select *
from User as U, EatsOrder as E
where U.user_id = E.user_id; 

#User의 id와 일치하는 주소의 값 찾기
select U.user_name,A.address_address
from User as U, Address as A
where U.user_id = A.user_id; 


# 3. use SET opration
(select *
from User
where user_name = '신현식')
union
(select * 
from User
where user_name = '백하늘');


(select Restaurant.restaurant_name
from Restaurant
where restaurant_address = '충무로')
union
(select Restaurant.restaurant_name
from Restaurant
where restaurant_address = '동대문');


# use aggregate function and/or GROUP BY
select sum(order_total_cost)
from EatsOrder;


select restaurant_id, restaurant_name,max(menu_price)
from Menu natural join Restaurant
group by restaurant_id, restaurant_name;


# 5. use SUBQUERY

# 11월1일에 주문했던 유저
select user_name, user_birth, order_date, order_total_cost
from User natural join EatsOrder
where order_date in (select order_date
from Eatsorder 
where order_date = '2022-11-01');

# 중구 장충로에 살고있는 user이름 출력
select *
from User as U, Address as A
where U.user_id = A.user_id and A.address_address in (select address_address
from Address
where address_address = '중구 장충로');


# 6 use EXISTS or UNIQUE

# 메뉴가 떡볶이가 없는 가게이름 
select restaurant_name
from Restaurant as E
where not exists(select *
from Menu as M
where E.restaurant_id = M.restaurant_id and M.menu_name like '%떡볶이');

# 중구 동호로에 사는 user이름 과 별명
select user_name, user_nickname
from User
where exists(select *
from Address
where User.user_id = Address.user_id and Address.address_address = '중구 동호로');


#3.1 before
select * from Menu;

#after 
update Menu 
set menu_price = menu_price*0.9;

select * from Menu;

#before 
select * 
from Restaurant
where restaurant_status ='open';

#after 
update Restaurant set restaurant_status = 'close'
where restaurant_name ='맥도날드' or restaurant_name ='굽네치킨';

select * 
from Restaurant
where restaurant_status ='open';


# 4번

select restaurant_name, menu_name, menu_price
from Restaurant natural join Menu ;


select restaurant_name, restaurant_address, menu_name, menu_description ,menu_price
from Menu natural join restaurant
where Menu_price > 15000;


select restaurant_name
from Restaurant as E
where restaurant_address = '충무로';


select * 
from Restaurant
where restaurant_status ='open';


select user_nickname, user_birth, order_date, order_total_cost
from User natural join eatsorder
where user_id = '0002'
order by order_date asc;

select Menu_name, Menu_price, Menu_description from Menu natural join restaurant where restaurant_name='엽기떡볶이'



delimiter $$
create procedure food1_cost()
begin
	select sum(menu_price)
	from menu natural join restaurant
    where restaurant_name='bhc 치킨';
end $$
delimiter ;




SET GLOBAL log_bin_trust_function_creators = 1;
delimiter $$
CREATE FUNCTION GET_PRICE(
	MENU VARCHAR(20)
) RETURNS varchar(20)
BEGIN
	DECLARE MENU_TITLE VARCHAR(20);
	DECLARE PRICE_TITLE VARCHAR(20);
	DECLARE RETURN_VALUE VARCHAR(20);

	SELECT CONCAT(MENU, ' IS ')
	  INTO MENU_TITLE;

	SELECT menu_price
	FROM menu
	WHERE menu_name = MENU
	INTO PRICE_TITLE;

	SET RETURN_VALUE = CONCAT(MENU_TITLE, PRICE_TITLE);

	RETURN RETURN_VALUE;
END $$
delimiter ;