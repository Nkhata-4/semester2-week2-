-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

SELECT Books.title, Members.name, Loans.loan_date
FROM 
Books JOIN Loans
ON Books.id = Loans.book_id
JOIN Members
ON Loans.member_id = Members.id;


SELECT Books.title, Loans.loan_date
FROM 
Loans JOIN Books
ON Loans.book_id = Books.id;

SELECT LibraryBranch.name AS Library, Books.title
FROM
Books JOIN LibraryBranch
ON Books.branch_id = LibraryBranch.id;

SELECT LibraryBranch.name AS Library, COUNT(Books.title)
FROM 
Books JOIN LibraryBranch
ON Books.branch_id = LibraryBranch.id
GROUP BY Library;

SELECT LibraryBranch.name AS Library, COUNT(Books.title) AS Amount
FROM 
Books JOIN LibraryBranch
ON Books.branch_id = LibraryBranch.id
WHERE Amount > 7
GROUP BY Library; 
