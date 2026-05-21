create database if not exists database1;
use database1;

create table users(
	用户ID int primary key auto_increment,
    用户名 varchar(50),
    手机号 int ,
    注册时间 DATETIME,
    邮箱 varchar(50) Unique
);

create table orders(
	订单ID int primary key
    auto_increment,
    订单时间 DATETIME,
    总金额 int,
    订单状态 varchar(50),
    收货地址 varchar(50),
    用户ID int,
    Foreign Key (用户ID) REFERENCES users(用户ID)
);

create table products(
	商品ID int primary key auto_increment,
    商品名称 varchar(50),
    价格 Decimal(10,2) ,
    库存 int,
    订单ID int,
	Foreign Key (订单ID) REFERENCES orders(订单ID)
);

create table order_items(
	ID int primary key auto_increment,
    订单ID int,
    Foreign Key (订单ID) REFERENCES orders(订单ID),
    商品ID int,
    Foreign Key (商品ID) REFERENCES products(商品ID),
    购买数量 int,
    商品单价 int,
    小计金额 int
);