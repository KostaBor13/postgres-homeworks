-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)

);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100),
	employee_id int,
	order_date date,
	ship_city varchar(100)

);

SELECT * FROM customers;
SELECT * FROM employees;
SELECT * FROM orders;