DROP TABLE IF EXISTS manufacters CASCADE;
DROP TABLE IF EXISTS products CASCADE;

CREATE TABLE IF NOT EXISTS manufacters(
	manufacter_id SERIAL PRIMARY KEY,
	manufacter_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(50) NOT NULL,
	product_price NUMERIC(10, 2),
	stock INTEGER,
	manufacter_id INTEGER REFERENCES manufacters(manufacter_id) 
);

INSERT INTO manufacters(manufacter_name)VALUES
('BMW'),
('Lambargini'),
('Bugatti');

INSERT INTO products(product_name, product_price, stock)VALUES
('BMW M5 F90', 120000, 10),
('Lambargibi Urus', 200000, 10),
('Bugatti Chiron', 300000, 10);

UPDATE products
SET product_price = 1250
WHERE product_id = 2;

UPDATE products
SET product_price = product_price + 30
WHERE product_id = 1;

SELECT *
FROM products
WHERE product_price > (SELECT AVG(product_price) FROM products);


DELETE FROM products
WHERE product_id = 3;

DELETE FROM products WHERE product_id = 2;

ALTER TABLE products
ADD COLUMN year VARCHAR(4);

ALTER TABLE products
DROP COLUMN year;


SELECT p.*, m.manufacter_name
FROM products p
JOIN manufacters m ON p.manufacter_id = m.manufacter_id;


SELECT * FROM manufacters;
SELECT * FROM products;