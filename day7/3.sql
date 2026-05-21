create table products(
	商品ID int primary key auto_increment,
    商品名称 varchar(50),
    价格 Decimal(10,2) ,
    库存 int,
    订单ID int,
	Foreign Key (订单ID) REFERENCES orders(订单ID)
);

