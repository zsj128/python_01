ALTER table employees add hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
alter table employees modify salary decimal(10,2);
alter table employees add sex ENUM('男','女');
describe employees