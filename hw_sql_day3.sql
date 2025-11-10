-- You are working for a local bookstore that sells books both online and offline. The manager has asked you to help prepare reports from the books table. The table has the following columns:
-- id (number)
-- title (text)
-- author (text)
-- price (number)
-- stock_status (text: either 'In Stock' or 'Out of Stock')
-- genre (text)
-- Your tasks are:
-- Show all the different genres available in the store (no duplicates).
-- List all books that are in stock and priced below 400.
-- List all books that are either out of stock or have a price above 700.
-- Show the title and price of every book along with a new column that adds 10% GST to the price.

-- Display the title, price, and stock_status of all books, sorted by price from highest to lowest.


INSERT INTO books (id,title,author,price,stock_status,genre) VALUES
('101','The Great Gatsby','F.Scott Fitgerald','499','In Stock','Fiction'),
('102','The Da Vinci Code','Dan Brown','899','Out of Stock','Mystery'),
('103','400 Days','Chetan Bagat','299','In Stock','Science'),
('104','To Kill a Mockingbird','Harper Lee','650','In Stock','History'),
('105','This Thing Called Love','Deblina Bhattacharya','390','In Stock','History');

1)
SELECT DISTINCT genre from books;

2)
SELECT * from books WHERE stock_status="In Stock" AND price<400;

3)
SELECT * from books WHERE stock_status="Out of Stock" OR price>700;

4)
SELECT title,price,price * 1.10 AS price_with_gst FROM books;

5)
SELECT title,price,stock_status FROM books ORDER BY price desc;
