create table users(
	用户ID int primary key auto_increment,
    用户名 varchar(50),
    手机号 int ,
    注册时间 DATETIME,
    邮箱 varchar(50) Unique
);