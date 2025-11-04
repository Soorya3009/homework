1)
INSERT INTO library (id,title,author,price,genre) VALUES
('101','The Great Gatsby','F.Scott Fitgerald','499','Fiction'),
('102','The Da Vinci Code','Dan Brown','899','Mystery'),
('103','400 Days','Chetan Bagat','299','Science'),
('104','To Kill a Mockingbird','Harper Lee','650','History'),
('105','This Thing Called Love','Deblina Bhattacharya','390','History');

2)
SELECT * FROM library WHERE price > 400;

3)
SELECT * FROM library WHERE genre IN('History','Science','Fiction');

4)
SELECT * FROM library WHERE title='The Great Gatsby';

5)
SELECT * FROM library WHERE author <> 'Dan Brown';