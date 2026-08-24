CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    bio TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    isbn NUMERIC UNIQUE,
    price NUMERIC(10,2) NOT NULL,
	stock NUMERIC NOT NULL DEFAULT 0,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    created_date DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price NUMERIC(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


------------------------------------------------------------------

INSERT INTO authors (name, bio) VALUES
('Mark Lutz', NULL),
('Wes McKinney', NULL),
('Alex Martelli', NULL),
('Luciano Ramalho', NULL),
('Justin Seitz', NULL),
('R. Nageswara Rao', NULL),
('Al Sweigart', NULL),
('Allen B. Downey', NULL),
('Joshua Welsh', NULL),
('Brett Slatkin', NULL),
('Martin C. Brown', NULL),
('Eric Matthes', NULL),
('James R. Payne', NULL),
('Paul Barry', NULL),
('Steve Chimombo', NULL),
('Charles R. Severance', NULL),
('Atharva Phadtare', NULL);


INSERT INTO books
(title, isbn, price, stock, author_id)
VALUES
('Learning Python', 978101, 120, 1, 1),
('Python For Data Analysis', 978102, 120, 1, 2),
('Python Cookbook', 978103, 120, 1, 3),
('Python', 978104, 120, 1, 1),
('Fluent Python', 978105, 120, 1, 4),
('Black Hat Python', 978106, 120, 1, 5),
('Programming Python', 978107, 120, 1, 1),
('Core Python Programming', 978108, 120, 1, 6),
('Automate the Boring Stuff with Python', 978109, 120, 1, 7),
('Think Python', 978110, 120, 1, 8),
('Python', 978111, 120, 1, 9),
('Effective Python', 978112, 120, 1, 10),
('Python, The Complete Reference', 978113, 120, 1, 11),
('Python Crash Course, 2nd Edition', 978114, 120, 1, 12),
('Python Crash Course, 3rd Edition', 978115, 120, 1, 12),
('Beginning Python', 978116, 120, 1, 13),
('Head First Python', 978117, 120, 1, 14),
('Python! python!', 978118, 120, 1, 15),
('Python for Everybody', 978119, 120, 1, 16),
('Atharva', 978120, 100, 20, 17);

-------------------------------------------------------------------------------

SELECT b.title, b.price, b.stock, a.name AS author FROM books b JOIN authors a ON b.author_id = a.id;

SELECT title, price FROM books WHERE price < 20;

SELECT title, stock FROM books WHERE stock <= 5 ORDER BY stock ASC;

SELECT a.name AS author, COUNT(b.id) AS number_of_books FROM authors a LEFT JOIN books b ON a.id = b.author_id GROUP BY a.id, a.name ORDER BY number_of_books DESC;

SELECT a.name AS author, COUNT(b.id) AS number_of_books FROM authors a JOIN books b ON a.id = b.author_id GROUP BY a.id, a.name HAVING COUNT(b.id) > 1 ORDER BY number_of_books DESC;

SELECT AVG(price) AS average_price, MIN(price) AS cheapest_price, MAX(price) AS most_expensive_price FROM books;

SELECT title, price FROM books ORDER BY price DESC LIMIT 5;

SELECT o.id AS order_id, u.email, o.status, o.created_date FROM orders o JOIN users u ON o.user_id = u.id ORDER BY o.created_date DESC;

SELECT oi.id AS order_item_id, o.id AS order_id, b.title AS book, oi.quantity, oi.price FROM order_items oi JOIN orders o ON oi.order_id = o.id JOIN books b ON oi.book_id = b.id;

SELECT b.title, COALESCE(SUM(oi.quantity), 0) AS total_sold FROM books b LEFT JOIN order_items oi ON b.id = oi.book_id GROUP BY b.id, b.title ORDER BY total_sold DESC;
