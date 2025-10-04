DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS news;
DROP TABLE IF EXISTS comments;

CREATE TABLE IF NOT EXISTS categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    descriptions TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS news(
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_published BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS comments(
    id SERIAL PRIMARY KEY,
    news_id INT REFERENCES news(id),
    author_name VARCHAR(100) NOT NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE news
ADD COLUMN views INTEGER DEFAULT 0;

ALTER TABLE comments
ALTER COLUMN author_name TYPE TEXT;

INSERT INTO categories (name, descriptions) 
VALUES 
    ('Technology', 'All about technology and gadgets'),
    ('Sports', 'Latest news in the world of sports'),
    ('Health', 'Health tips and wellness news');

INSERT INTO news (category_id, title, content, published_at, is_published) 
VALUES 
    (1, 'Latest Tech Trends in 2024', 'Technology is evolving rapidly. In 2024, AI and machine learning will dominate...', CURRENT_TIMESTAMP, TRUE);

INSERT INTO news (category_id, title, content, published_at, is_published) 
VALUES 
    (2, 'The Exciting World Cup Final', 'The World Cup final was held last weekend. The final game was unforgettable...', CURRENT_TIMESTAMP, TRUE);

INSERT INTO news (category_id, title, content, published_at, is_published) 
VALUES 
    (3, '10 Tips for a Healthier Lifestyle', 'Living a healthier life requires dedication. Here are 10 practical tips...', CURRENT_TIMESTAMP, TRUE);

INSERT INTO comments (news_id, author_name, comment_text)
VALUES 
    (1, 'John Doe', 'This article is very insightful! AI will definitely change everything.');

INSERT INTO comments (news_id, author_name, comment_text, created_at)
VALUES 
    (2, 'Jane Smith', 'What an exciting match! The final was really a nail-biter.', CURRENT_TIMESTAMP);

INSERT INTO comments (news_id, author_name, comment_text, created_at)
VALUES 
    (3, 'Alice Brown', 'Great tips! I will start drinking more water and exercising regularly.', CURRENT_TIMESTAMP);

UPDATE news
SET views = views + 1;

UPDATE news
SET is_published = TRUE
WHERE is_published = FALSE
    AND published_at <= CURRENT_DATE - INTERVAL '1 day';

DELETE FROM comments
WHERE created_at <= CURRENT_DATE - INTERVAL '1 year';

ALTER TABLE news
ADD CONSTRAINT unique_title UNIQUE(title);

SELECT * FROM categories;
SELECT * FROM news;
SELECT * FROM comments;

SELECT * FROM news
WHERE views BETWEEN 10 AND 100;
