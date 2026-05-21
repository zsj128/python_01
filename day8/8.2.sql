-- use company;
-- -- 员工表
-- CREATE TABLE employees (
--     emp_id INT PRIMARY KEY AUTO_INCREMENT,
--     emp_name VARCHAR(20),
--     salary DECIMAL(10,2),
--     dept_id INT
-- );

-- -- 部门表
-- CREATE TABLE departments (
--     dept_id INT PRIMARY KEY AUTO_INCREMENT,
--     dept_name VARCHAR(20),
--     location VARCHAR(20)
-- );

-- -- 插入测试数据
-- INSERT INTO employees (emp_name, salary, dept_id) VALUES 
-- ('小明', 8000.00, 1),
-- ('小红', 9000.00, 1),
-- ('小刚', 12000.00, 2),
-- ('小丽', 7500.00, NULL), -- 未分配部门的员工
-- ('小强', 11000.00, 99);  -- 部门ID不存在的员工

-- INSERT INTO departments (dept_name, location) VALUES 
-- ('技术部', '北京'),
-- ('市场部', '上海'),
-- ('人事部', '广州'); -- 暂无员工的部门

-- SELECT * FROM employees e inner JOIN departments d ON e.dept_id = d.dept_id
-- SELECT * FROM employees e left JOIN departments d ON e.dept_id = d.dept_id

-- SELECT * FROM employees where salary > 8000 and dept_id = 1
-- SELECT * FROM employees where salary < 8000 or salary >11000;
-- SELECT * FROM employees where dept_id in (1,2);
-- SELECT * FROM employees where emp_id between 1 and 4;
-- SELECT * FROM employees where dept_id = 1 and ((salary between 8000 and 10000) or (salary >11000)) 
-- select * from (employees e inner JOIN departments d ON e.dept_id = d.dept_id) where location in ('北京','上海')
-- SELECT * FROM employees where emp_name like '%明';
-- SELECT * FROM employees where emp_name like '%小%';
-- SELECT * FROM employees where emp_name like '_明';
-- SELECT * FROM employees where emp_name like '%刚%' or emp_name like '%红%';
-- select 
-- 	emp_name,
--     salary, 
--     case
-- 		when salary < 10000 and salary > 8000 then '良好'
--         when salary >= 10000 then '优秀'
--         else '不合格'
-- 	end as default_res
-- from employees

