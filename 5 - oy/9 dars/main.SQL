DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

INSERT INTO categories (category_id, category_name) VALUES
(1, 'Electronics'),
(2, 'Clothing'),
(3, 'Furniture'),
(4, 'Toys'),
(5, 'Books');

INSERT INTO products (product_id, product_name, category_id) VALUES
(1, 'Laptop', 1),
(2, 'Smartphone', 1),
(3, 'T-Shirt', 2),
(4, 'Jeans', 2),
(5, 'Sofa', 3),
(6, 'Table', 3),
(7, 'Doll', 4),
(8, 'Car Toy', 4),
(9, 'Novel', 5),
(10, 'Textbook', 5),
(11, 'Headphones', NULL),
(12, 'Charger', NULL),
(13, 'Pen', NULL),
(14, 'Notebook', NULL),
(15, 'Bag', NULL);

SELECT c.category_name, p.product_name
FROM categories c
JOIN products p ON c.category_id = p.category_id;

SELECT c.category_name, p.product_name
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id;

SELECT c.category_name, p.product_name
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
UNION
SELECT c.category_name, p.product_name
FROM categories c
RIGHT JOIN products p ON c.category_id = p.category_id;

SELECT product_name
FROM products
WHERE category_id IS NULL;

SELECT category_name
FROM categories
WHERE category_id NOT IN (SELECT DISTINCT category_id FROM products);

SELECT * FROM categories;
SELECT * FROM products;

SELECT category_name
FROM categories
WHERE category_id NOT IN (SELECT DISTINCT category_id FROM products)
UNION
SELECT product_name
FROM products
WHERE category_id IS NULL;

SELECT c.category_name, p.product_name
FROM categories c
CROSS JOIN products p;

SELECT c.category_name, p.product_name
FROM categories c
NATURAL JOIN products;
 

 