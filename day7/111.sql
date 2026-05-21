SET SQL_SAFE_UPDATES = 0;

create database if not exists school;
use school;

create table students(
	id INT PRIMARY KEY AUTO_INCREMENT COMMENT '学号',
    name VARCHAR(20) NOT NULL COMMENT '学生姓名',
    gender CHAR(1) COMMENT '性别',
    age INT COMMENT '年龄',
    major VARCHAR(20) COMMENT '专业'
);

INSERT INTO students (name,gender,age,major) 
VALUE 
('张三', '男',18,'计算机科学'),
('李四', '女',21,'计算机科学'),
('王五', '男',20,'数学'),
('赵六', '男',21,'数学'),
('钱七', '女',19,'数学'),
('孙八', '女',22,'英语'),
('周九', '男',20,'计算机科学');

select * from students where age < 20 order by age asc,name desc;
update students set age = age + 1 where major = '计算机科学';
delete from students where name = '王五';
delete from students where gender = '女' and age > 20;
select major, count(*) as 人数, avg(age) as 平均年龄 from students group by major;
select * from students; 