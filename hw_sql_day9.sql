CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE employees (id INT, name VARCHAR(100));

CREATE TABLE departments (emp_id INT,department_name VARCHAR(100));

INSERT INTO employees (id, name) VALUES (1, 'Anjali'),(2, 'Rohan'),(3, 'Meena');

INSERT INTO departments (emp_id, department_name) VALUES(1, 'HR'),(2, 'IT'),(4, 'Finance');

1
SELECT employees.name, departments.department_name FROM employees LEFT JOIN departments ON employees.id = departments.emp_id;

2
SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.id = departments.emp_id;

3
SELECT employees.name, departments.department_name FROM employees RIGHT JOIN departments ON employees.id = departments.emp_id;