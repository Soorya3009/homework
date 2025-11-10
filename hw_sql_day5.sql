-- You are helping manage a small online bookstore's database. The table is called books, and it stores the following details:
-- id (number)
-- title (text)
-- author (text)
-- price (number)
-- stock (number)
-- Perform the following tasks:
-- Add the following five books to the table:
-- (1, 'The Alchemist', 'Paulo Coelho', 350, 50)
-- (2, 'Atomic Habits', 'James Clear', 450, 40)
-- (3, 'The Psychology of Money', 'Morgan Housel', 400, 30)
-- (4, 'Ikigai', 'Francesc Miralles', 300, 60)
-- (5, 'Deep Work', 'Cal Newport', 500, 20)
-- Display all books that cost less than 450 and have stock more than 30.
-- Update the stock to 45 and reduce the price to 420 for the book titled ‘Deep Work’.
-- Delete the book titled ‘Ikigai’.
-- Show the average book price and total number of books currently in the table.
-- Display the top 3 most expensive books available.




1. INSERT INTO bookss(ID,TITLE,AUTHOR,PRICE,STOCK)
    VALUES('1','The Alchemist','Paulo Coelho','350','50'),
	      ('2','Atomic Habits','James Clear','450','40'),
          ('3','The Psychology of Money','Morgan Housel','400','30'),
	      ('4','Ikigai','Francesc Miralles','300','60'),
	      ('5','Deep Work','Cal Newport','500','20');

2. SELECT * FROM bookss WHERE PRICE < 450 AND STOCK > 30;

3. UPDATE bookss SET STOCK = '45', PRICE = '420' WHERE TITLE = 'deep work';

4. DELETE FROM bookss WHERE TITLE = 'Ikigai';

5. SELECT AVG(PRICE) AS Average, COUNT(*) AS Totalbooks FROM bookss;

6. SELECT * FROM bookss ORDER BY PRICE DESC LIMIT 3;