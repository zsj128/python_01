CREATE DATABASE IF NOT EXISTS company;
USE company;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '员工编号',
    name VARCHAR(20) NOT NULL COMMENT '员工姓名',
    salary DECIMAL(10,2) COMMENT '薪水',
    position VARCHAR(20) COMMENT '职位',
    department VARCHAR(20) COMMENT '部门',
    entry_date DATE COMMENT '入职日期',
    gender CHAR(1) COMMENT '性别'
) COMMENT='员工信息表';

INSERT INTO employees(name, salary, position, department, entry_date, gender)
VALUES
('张三', 15000.00, '开发工程师', '技术部', '2020-03-15', '男'),
('李四', 12000.00, '设计师', '设计部', '2021-07-20', '女'),
('王五', 18000.00, '高级开发', '技术部', '2019-11-05', '男'),
('赵六', 10000.00, '设计师', '设计部', '2022-01-10', '男'),
('钱七', 22000.00, '产品经理', '产品部', '2018-05-12', '女'),
('孙八', 9000.00, '设计师', '设计部', '2023-02-18', '女'),
('周九', 16000.00, '开发工程师', '技术部', '2021-09-01', '男');