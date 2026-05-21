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