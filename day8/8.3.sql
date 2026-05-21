create database if not exists database2;
use database2;
-- 1. 用户表
-- CREATE TABLE users (
--     user_id INT PRIMARY KEY,   -- 用户ID（主键）
--     username VARCHAR(50)      -- 用户名
-- );

-- 2. 订单表
-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY,    -- 订单ID
--     user_id INT,                 -- 用户ID（关联 users 表）
--     total_amount DECIMAL(10,2),  -- 订单金额
--     FOREIGN KEY (user_id) REFERENCES users(user_id)
-- );

-- INSERT INTO users VALUES
-- (1, '张三'),
-- (2, '李四'),
-- (3, '王五');

-- INSERT INTO orders VALUES
-- (101, 1, 6000),
-- (102, 1, 5000),
-- (103, 2, 3000);

SELECT 
	u.username,
    ifnull (sum(o.total_amount),0) as total_spent,
    case 
		when sum(o.total_amount) > 10000 then "VIP"
        else '普通用户'
	end as default_res
FROM users u left JOIN orders o ON u.user_id = o.user_id group by u.user_iddepartments

-- select 
-- 	name,
--     total_amount, 
--     case
-- 		when salary < 10000 and salary > 8000 then '良好'
--         when salary >= 10000 then '优秀'
--         else '不合格'
-- 	end as default_res
-- from employees