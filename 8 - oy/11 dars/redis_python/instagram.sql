DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE IF NOT EXISTS users(
	userId SERIAL PRIMARY KEY,
	fullName VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS friends(
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users(userId),
	friend_id INTEGER REFERENCES users(userId)
);


INSERT INTO users(fullname) VALUES
('Toxir Toxirov'),
('Sobir Sobirov'),
('Ali Valiyev'),
('Bakir Bakirov'),
('Jamshid Valiyev');


INSERT INTO friends(user_id, friend_id) VALUES
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 3),
(3, 1),
(3, 5),
(4, 1),
(4, 3),
(5, 1),
(5, 4);

