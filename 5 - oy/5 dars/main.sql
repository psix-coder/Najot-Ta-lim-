-- 1-TOPSHIRIQ 
DROP TABLE IF EXISTS authors CASCADE;

CREATE TABLE IF NOT EXISTS authors (
    author_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO authors (first_name, last_name, bio) VALUES 
('Alex', 'Turner', 'Alex is a science fiction writer and technology enthusiast.'),
('Marie', 'Curie', 'Marie is known for her groundbreaking work in scientific literature.'),
('Leo', 'Fitz', 'Leo specializes in mystery novels with a twist.');
-- ------------------------------------------------------------------------------------------------------------------------------------------------------

-- 2-TOPSHIRIQ
DROP TABLE IF EXISTS books CASCADE;

CREATE TABLE IF NOT EXISTS books(
	book_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	summary TEXT,
	published_date DATE,
	metadata JSON,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO books (title, summary, published_date, metadata) VALUES 
('Galactic Chronicles', 
 'A futuristic exploration of space and humanity’s role in it.', 
 '2022-01-10', 
 '{"genre": "Science Fiction", "format": "Hardcover"}'),

('Whispers in the Dark', 
 'A collection of mysterious and thrilling short stories.', 
 '2019-11-05', 
 '{"genre": "Mystery", "format": "Paperback"}'),

('Journey to the Future', 
 'A look at technological advancements and their impacts on society.', 
 '2023-08-22', 
 '{"genre": "Non-Fiction", "format": "Ebook"}');
-- ---------------------------------------------------------------------------------------------------------------------------------------------

-- 3-TOPSHIRIQ
DROP TABLE IF EXISTS publishers CASCADE;

CREATE TABLE IF NOT EXISTS publishers(
	publisher_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	country CHAR(2) NOT NULL,
	founded_year INTEGER,
	details JSON,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO publishers (name, country, founded_year, details) VALUES 
('Galactic Publishing', 'US', 2005, '{"genres": ["Science Fiction", "Fantasy", "Thriller"], "employees": 2500}'),
('Mystery House', 'GB', 1980, '{"genres": ["Mystery", "Crime", "Suspense"], "headquarters": "London"}'),
('TechWorld Press', 'CA', 2015, '{"genres": ["Technology", "Non-Fiction", "Science"], "branches": ["Canada", "US"]}'),
('Manga Universe', 'JP', 1930, '{"genres": ["Manga", "Fantasy"], "famous_works": ["Dragon Ball", "Bleach"]}');
-- -------------------------------------------------------------------------------------------------------------------------------------------------

-- 4-TOPSHIRIQ
DROP TABLE IF EXISTS lib;

CREATE TABLE lib (
    library_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location TEXT NOT NULL,
    open_time TIME,
    close_time TIME,
    facilities JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO lib (name, location, open_time, close_time, facilities) VALUES 
('Galactic Central Library', 
 '789 Star Blvd, Cosmos City', 
 '07:30', 
 '21:00', 
 '{"Wi-Fi": true, "study_room": true, "VR_station": true}'),
('Old Town Library', 
 '123 Heritage St, Historicville', 
 '09:30', 
 '19:00', 
 '{"Wi-Fi": true, "children_section": true, "cafe": true}'),
('Techie Library', 
 '101 Future Way, Silicon Valley', 
 '08:00', 
 '22:00', 
 '{"Wi-Fi": true, "study_room": true, "3D_printer": true}');
-- -------------------------------------------------------------------------------------------------------------------------------------------------------

-- 5-TOPSHIRIQ
-- 1-topshiriq
DROP TABLE IF EXISTS author_book;

CREATE TABLE IF NOT EXISTS author_book (
    author_id UUID REFERENCES authors(author_id) ON DELETE CASCADE,
    book_id UUID REFERENCES books(book_id) ON DELETE CASCADE,
    PRIMARY KEY (author_id, book_id)  
);

SELECT * FROM author_book;

-- ---------------------------------------------------------------------------------

-- 2-topshiriq
DROP TABLE IF EXISTS book_publisher CASCADE;

CREATE TABLE IF NOT EXISTS book_publisher (
    book_id UUID REFERENCES books(book_id) ON DELETE CASCADE,
    publisher_id UUID REFERENCES publishers(publisher_id) ON DELETE CASCADE,
    PRIMARY KEY (book_id, publisher_id)
);

SELECT * FROM book_publisher;
-- ---------------------------------------------------------------------------------

-- 3-topshiriq
DROP TABLE IF EXISTS l_book CASCADE;

CREATE TABLE IF NOT EXISTS l_book (
    library_id UUID REFERENCES lib(library_id) ON DELETE CASCADE,
    book_id UUID REFERENCES books(book_id) ON DELETE CASCADE,
    PRIMARY KEY (library_id, book_id)
);

SELECT * FROM l_book;
