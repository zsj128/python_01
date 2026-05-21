SET SQL_SAFE_UPDATES = 0;

create database if not exists school;
use school;

-- CREATE TABLE classes(
--     class_id INT PRIMARY KEY, class_name VARCHAR(50)
-- );
-- CREATE TABLE student(
--     id INT PRIMARY KEY,name VARCHAR(50),c_id int
-- );
-- INSERT INTO classes VALUES(1,'计算机一班'),(2,'AI班');
-- INSERT INTO student VALUES(1,'张三',1),(2,'李四',1),(3,'王五',2),(4,'赵六',NULL); 

-- SELECT s.name,c.class_name FROM student s INNER JOIN classes c ON s.c_id = c.class_id
-- SELECT s.name,c.class_name FROM student s LEFT JOIN classes c ON s.c_id = c.class_id 
-- SELECT c.class_name,s.student_count 
-- FROM classes c
-- left join (
-- 	select c_id,count(*) as student_count
--     from student
--     group by c_id
-- ) s
-- on c.class_id = s.c_id
SELECT 
	s.id as student_id,
	s.name,
    (select class_name
    from classes c
    where c.class_id=s.c_id) as class_name
from student s;


