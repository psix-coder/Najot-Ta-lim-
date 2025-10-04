-- drop table if exists students;

-- create table if not exists students(
-- 	sudent_id serial primary key,
-- 	f_name text not null,
-- 	age int,
-- 	adress text
-- );

-- insert into students(sudent_id, f_name, age, adress) values
-- (1,'Bakir', 17, 'Fargona'),
-- (2,'Zokir', 21, 'tashkent'),
-- (3,'Zokir', 40, 'Nyu York');

-- select * from students;

-- DROP TABLE IF EXISTS products;

-- CREATE TABLE IF NOT EXISTS products (
--     product_id SERIAL UNIQUE,
--     name TEXT NOT NULL, 
--     price INT,
--     description TEXT
-- );

-- INSERT INTO products (product_id, name, price, description) VALUES
-- (1, 'Coca Cola', 12000, 'Coca-Cola - dunyodagi eng mashhur ichimliklardan biri bo‘lib, o‘ziga xos shirin ta’m va tetiklantiruvchi xususiyatlari bilan tanilgan. Coca-Cola tabiiy tarkibiy qismlar asosida tayyorlanadi va yuqori sifatli karbonat bilan boyitilgan. Ichimlik sovuq holda ichish uchun ideal va har qanday tadbir yoki taomga mos keladi. Hozirgi kunda Coca-Cola butun dunyoda sevib iste’mol qilinadigan gazli ichimliklardan biridir.'),
-- (2, 'Pepsi', 13000, 'Pepsi - eng mashhur gazli ichimliklardan biri bo‘lib, o‘ziga xos shirin va yangilovchi ta’mga ega. 1893-yilda yaratilgan Pepsi, yillar davomida ko‘plab sevuvchilarning e’tiborini qozongan. Ushbu ichimlik karbonatlangan va butun dunyoda kuchli brend sifatida tanilgan. Pepsi qizil va ko‘k ranglar bilan bezatilgan qutichalarda, shuningdek, stakanlarda mavjud bo‘lib, har qanday tadbir, oziq-ovqat yoki yoqimli muhitda iste’mol qilish uchun ideal tanlovdir.'),
-- (3, 'Fanta', 12000, 'Fanta - yorqin va shirin gazli ichimlik bo‘lib, ko‘plab mevalar ta’miga ega. Fanta dastlab 1940-yillarda yaratilgan bo‘lib, bugungi kunda ko‘plab rang va ta’mda mavjud. Bu ichimlik eng yaxshi meva aromalaridan biri bo‘lib, issiq kunlarda tetiklantiruvchi va qoniqarli ichimlik sifatida tanilgan. Fanta qizil, to‘q sariq va boshqa ranglarda, shuningdek, har qanday tadbirda, piknikda yoki quvnoq muhitda iste’mol qilish uchun ideal tanlovdir.');

-- SELECT * FROM products;

-- DROP TABLE IF EXISTS buyurtma;

-- CREATE TABLE IF NOT EXISTS buyurtma (
--     b_id SERIAL UNIQUE,
--     "user" TEXT,  -- 'user' so‘zi kvadrat qavs ichida
--     product TEXT,
--     amount INT
-- );

-- INSERT INTO buyurtma ("user", product, amount) VALUES
-- ('Abdulloh', 'Stiker', 2),
-- ('Jamoliddin', 'Ruchka', 5),
-- ('Davron', 'Sichqoncha', 1),
-- ('Muhammadjon', 'Quloqchin', 3);

-- SELECT * FROM buyurtma;



-- DROP TABLE IF EXISTS xodim;

-- CREATE TABLE IF NOT EXISTS xodim (
--     x_id SERIAL UNIQUE,
--     name TEXT,
--     position TEXT,
--     annual_salary INT
-- );

-- INSERT INTO xodim (name, position, annual_salary) VALUES
-- ('Able', 'Senior', 20000),
-- ('David', 'Architect', 20000),
-- ('Jama', 'Medium', 15000);

-- SELECT * FROM xodim;


-- DROP TABLE IF EXISTS delivery;

-- CREATE TABLE IF NOT EXISTS delivery (
--     Deliver_id SERIAL UNIQUE,
--     Name_company TEXT NOT NULL,
--     Phone_number TEXT,
--     location TEXT
-- );

-- INSERT INTO delivery (Name_company, Phone_number, location) VALUES
-- ('Uzum', '+998 ... .. ..', 'Tashkent'),
-- ('Amazon', '+1 ... ... ..', 'Amerika'),
-- ('Alibaba', '+7.. .. ....', 'Xitoy');

-- SELECT * FROM delivery;  
