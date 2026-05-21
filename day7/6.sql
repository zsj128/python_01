create database if not exists company;
use company;

create table employees(
	id int primary key auto_increment,
    name varchar(50),
    position VARCHAR(50),
    salary INT
);