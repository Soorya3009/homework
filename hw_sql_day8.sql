1
CREATE DATABASE BookStoreDB;

2
USE BookStoreDB;

3
CREATE TABLE authors (author_id INT PRIMARY KEY,name VARCHAR(100),country VARCHAR(100));

4
CREATE TABLE books (book_id INT PRIMARY KEY,title VARCHAR(200),price DECIMAL(10,2),author_id INT,FOREIGN KEY (author_id) REFERENCES authors(author_id));

5
ALTER TABLE books ADD published_year INT;

6
DELETE FROM books;

7
DROP DATABASE BookStoreDB;