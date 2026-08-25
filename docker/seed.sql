-- Insert authors
INSERT INTO authors (name)
VALUES
    ('Eric Matthes'),
    ('Robert C. Martin'),
    ('Martin Fowler'),
    ('James Clear'),
    ('J.K. Rowling'),
    ('George Orwell'),
    ('J.R.R. Tolkien'),
    ('Yuval Noah Harari'),
    ('Stephen King'),
    ('Agatha Christie');

-- Insert 20 books
INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Python Crash Course', 9781593279288, 120, 15, id
FROM authors WHERE name = 'Eric Matthes';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Clean Code', 9780132350884, 500, 12, id
FROM authors WHERE name = 'Robert C. Martin';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Clean Architecture', 9780134494166, 550, 10, id
FROM authors WHERE name = 'Robert C. Martin';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Refactoring', 9780134757599, 450, 8, id
FROM authors WHERE name = 'Martin Fowler';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Design Patterns', 9780201633610, 600, 7, id
FROM authors WHERE name = 'Martin Fowler';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Atomic Habits', 9780735211292, 350, 20, id
FROM authors WHERE name = 'James Clear';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Harry Potter and the Philosopher''s Stone', 9780747532699, 300, 18, id
FROM authors WHERE name = 'J.K. Rowling';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Harry Potter and the Chamber of Secrets', 9780747549604, 320, 16, id
FROM authors WHERE name = 'J.K. Rowling';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT '1984', 9780451524935, 250, 25, id
FROM authors WHERE name = 'George Orwell';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Animal Farm', 9780451526342, 220, 22, id
FROM authors WHERE name = 'George Orwell';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'The Hobbit', 9780547928227, 400, 14, id
FROM authors WHERE name = 'J.R.R. Tolkien';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'The Fellowship of the Ring', 9780547928210, 450, 12, id
FROM authors WHERE name = 'J.R.R. Tolkien';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'The Two Towers', 9780547928203, 450, 11, id
FROM authors WHERE name = 'J.R.R. Tolkien';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'The Return of the King', 9780547928197, 475, 10, id
FROM authors WHERE name = 'J.R.R. Tolkien';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Sapiens', 9780062316097, 380, 17, id
FROM authors WHERE name = 'Yuval Noah Harari';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Homo Deus', 9780062464316, 390, 13, id
FROM authors WHERE name = 'Yuval Noah Harari';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'The Shining', 9780307743657, 420, 9, id
FROM authors WHERE name = 'Stephen King';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'It', 9781501142970, 500, 8, id
FROM authors WHERE name = 'Stephen King';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'Murder on the Orient Express', 9780062693662, 280, 19, id
FROM authors WHERE name = 'Agatha Christie';

INSERT INTO books (title, isbn, price, stock, author_id)
SELECT 'And Then There Were None', 9780062073488, 280, 21, id
FROM authors WHERE name = 'Agatha Christie';