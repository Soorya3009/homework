-- You are managing a student enrollment database for a training center. The table is called students and contains these columns:
-- id (number)
-- name (text)
-- course (text)
-- fees_paid (number)
-- status (text: 'Active' or 'Inactive')
-- Complete the following tasks:
-- Insert 3 new students into the table with the following details:
-- (1, 'Alice', 'Web Development', 5000, 'Inactive')
-- (2, 'Bob', 'Data Science', 7000, 'Inactive')
-- (3, 'Charlie', 'UI/UX Design', 4000, 'Active')
-- Use a query to view only those students whose fees_paid is greater than 5000.
-- Update the status to 'Active' for students in the 'Web Development' course.
-- Increase the fees_paid by 1000 for students enrolled in 'Data Science'.
-- Update both status to 'Inactive' and reduce fees_paid by 500 for the student whose id is 3.
-- Delete the student whose id is 2.
-- Delete all students who are 'Inactive'.

INSERT INTO cw_students (id, name, course, fees_paid, status)
VALUES
(1, 'Alice', 'Web Development', 5000, 'Inactive'),
(2, 'Bob', 'Data Science', 7000, 'Inactive'),
(3, 'Charlie', 'UI/UX Design', 4000, 'Active');

1)
SELECT * FROM cw_students WHERE fees_paid > 5000;

2)
UPDATE cw_students SET status='Active' where course='Web Development';

3)
UPDATE cw_students SET fees_paid= fees_paid+1000 where course='Data Science';

4)
UPDATE cw_students SET status = 'Inactive',fees_paid = fees_paid - 500 WHERE id = 3;

5)
DELETE FROM cw_students WHERE id=2;

6)
DELETE from cw_students where status="Inactive";

