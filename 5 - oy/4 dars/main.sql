CREATE TABLE IF NOT EXISTS user(
    user_id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    f_name VARCHAR(50) NOT NULL, 
    date_joining TIMESTAMP default CURRENT_TIME,
    coming TIME DEFAULT CURRENT_TIME
);

INSERT INTO users(f_name, info) VALUES
('Toxir Toxirov', '{"address": "Fergana"}')


SELECT * FROM users;
SELECT f_name