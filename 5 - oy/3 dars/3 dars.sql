DROP TABLE IF EXISTS schools CASCADE;
DROP TABLE IF EXISTS teachers CASCADE;
DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS classes CASCADE;
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS grades CASCADE;
DROP TABLE IF EXISTS attendance CASCADE;
DROP TABLE IF EXISTS subjects CASCADE;

CREATE TABLE IF NOT EXISTS schools (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    contact_number CHAR(15),
    davlat_maktabi BOOL
);

CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    contact_number CHAR(15),
    school_id INT REFERENCES schools(id)
);

CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE,
    school_id INT REFERENCES schools(id),
    gender CHAR(1)
);

CREATE TABLE IF NOT EXISTS classes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INT REFERENCES teachers(id),
    school_id INT REFERENCES schools(id)
);

CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    class_id INT REFERENCES classes(id),
    teacher_id INT REFERENCES teachers(id)
);

CREATE TABLE IF NOT EXISTS enrollments (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    class_id INT REFERENCES classes(id),
    enrollment_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    subject_id INT REFERENCES subjects(id),
    grade_value INT,
    date_given TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS attendance (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    class_id INT REFERENCES classes(id),
    date DATE DEFAULT CURRENT_DATE
);

-- Ma'lumotlarni qo'shish
INSERT INTO schools (name, address, contact_number, davlat_maktabi)
VALUES 
    ('23 - MAKTAB', 'OLTIARIQ', '+99899...', TRUE),
    ('39 - MAKTAB', 'HAMZA', '+99890...', FALSE);

INSERT INTO teachers (first_name, last_name, email, contact_number, school_id)
VALUES 
    ('Ali', 'Valiyev', 'ali@example.com', '+99897...', 1),
    ('Olim', 'Karimov', 'olim@example.com', '+99893...', 2);

INSERT INTO students (first_name, last_name, dob, gender, school_id)
VALUES 
    ('Ahmad', 'Aliyev', '2005-05-10', 'M', 1),
    ('Mavluda', 'Sodiqova', '2006-07-12', 'F', 2);

INSERT INTO classes (name, teacher_id, school_id)
VALUES 
    ('10-A', 1, 1),
    ('11-B', 2, 2);

INSERT INTO subjects (name, class_id, teacher_id)
VALUES 
    ('Matematika', 1, 1),
    ('Ingliz tili', 2, 2);

INSERT INTO enrollments (student_id, class_id)
VALUES 
    (1, 1),
    (2, 2);

INSERT INTO grades (student_id, subject_id, grade_value)
VALUES 
    (1, 1, 90),
    (2, 2, 85);

INSERT INTO attendance (student_id, class_id)
VALUES 
    (1, 1),
    (2, 2);

-- Ma'lumotlarni chiqarish
SELECT id, student_id, TO_CHAR(enrollment_date, 'YYYY-MM-DD') AS enrollment_date FROM enrollments;
SELECT id, student_id, TO_CHAR(date_given, 'YYYY-MM-DD HH24:MI') AS date_given FROM grades;
SELECT id, student_id, TO_CHAR(date, 'YYYY-MM-DD') AS date FROM attendance;

-- Ma'lumotlarni yangilash
UPDATE schools SET name = '45 - MAKTAB' WHERE id = 1;
UPDATE teachers SET email = 'ali_valiyev@example.com' WHERE id = 1;
UPDATE classes SET name = '10-B' WHERE id = 1;

-- Ma'lumotlarni o'chirish
DELETE FROM enrollments WHERE id = 1;
DELETE FROM grades WHERE id = 1;
DELETE FROM attendance WHERE id = 1;
DELETE FROM subjects WHERE id = 1;

-- Jadval nomlarini o'zgartirish
ALTER TABLE schools RENAME TO maktab;
ALTER TABLE teachers RENAME TO oqituvchi;
ALTER TABLE students RENAME TO oquvchi;
ALTER TABLE classes RENAME TO clalar;
ALTER TABLE subjects RENAME TO fanlar;
ALTER TABLE enrollments RENAME TO enrolmantlar;
ALTER TABLE grades RENAME TO gradeslar;
ALTER TABLE attendance RENAME TO attendancelar;

SELECT * FROM maktab;
SELECT * FROM oqituvchi;
SELECT * FROM oquvchi;
SELECT * FROM clalar;
SELECT * FROM fanlar;
SELECT * FROM enrolmantlar;
SELECT * FROM gradeslar;
SELECT * FROM attendancelar;

-- Jadvalni o'chirish
DROP TABLE IF EXISTS maktab CASCADE;
DROP TABLE IF EXISTS oqituvchi CASCADE;
DROP TABLE IF EXISTS oquvchi CASCADE;
DROP TABLE IF EXISTS clalar CASCADE;
DROP TABLE IF EXISTS fanlar CASCADE;
DROP TABLE IF EXISTS enrolmantlar CASCADE;
DROP TABLE IF EXISTS gradeslar CASCADE;
DROP TABLE IF EXISTS attendancelar CASCADE;




