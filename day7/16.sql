delete from employees where salary < 10000 and entry_date < date_sub(curdate(),interval 5 year);
delete from employees where entry_date > date_sub(curdate(),interval 2 year) and department = '技术部';
select * from employees;