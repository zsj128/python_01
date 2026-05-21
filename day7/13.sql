#SET SQL_SAFE_UPDATES = 0;
update employees set salary=salary+2000 where department='技术部' and gender='男';
select * from employees;
