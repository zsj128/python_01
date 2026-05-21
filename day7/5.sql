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