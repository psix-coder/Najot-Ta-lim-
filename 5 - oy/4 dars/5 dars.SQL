DROP TABLE IF EXISTS authors CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS publishers CASCADE;
DROP TABLE IF EXISTS libraries CASCADE;
DROP TABLE IF EXISTS author_book CASCADE;
DROP TABLE IF EXISTS library_book CASCADE;



CREATE TABLE IF NOT EXISTS authors(
    id UUID,
    f_name VARCHAR(50), 
    l_name VARCHAR(50),
    bio TEXT NOT NULL,
    created_at TIMESTAMP
);

INSERT INTO authors(f_name, l_name, bio, created_at) VALUES
('Ali', 'Alijonov', 'Orta malumotli'),
('Vali', 'Valijonov', 'Oliy malumotli');



CREATE TABLE IF NOT EXISTS books(
    id UUID,
    title VARCHAR(100),
    summary TEXT,
    published_date DATE, 
    metadata  JSON, 
    update_at TIMESTAMP DEFAULT NOW()
);


INSERT INTO books(title, summary, published_date, metadata, update_at)VALUES



CREATE TABLE IF NOT EXISTS publishers(
    id UUID,
    name VARCHAR(100),
    country CHAR(2),
    founded_year INT,
    details JSON,
    created_at TIMESTAMP
);


INSERT INTO publishers(name, country, founded_year, details, created_at)VALUES




CREATE TABLE IF NOT EXISTS libraries(
    id UUID,
    name VARCHAR(100), 
    location TEXT,
    open_time TIME,
    close_time TIME,
    facilities JSON,
    created_at TIMESTAMP
);


INSERT INTO libraries(name, location, open_time, close_time, facilities, created_at)VALUES






SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM publishers;
SELECT * FROM libraries;
SELECT * FROM author_book;
SELECT * FROM library_book;