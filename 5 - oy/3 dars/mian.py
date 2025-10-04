import psycopg2 

db = psycopg2.connect(
    database='Able_me',
    user='postgres',
    host='localhost', 
    password='a369963A'
)
cursor = db.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS schools CASCADE;
    DROP TABLE IF EXISTS teachers CASCADE;
    DROP TABLE IF EXISTS students CASCADE;
    DROP TABLE IF EXISTS classes CASCADE;
    DROP TABLE IF EXISTS enrollments CASCADE;
    DROP TABLE IF EXISTS grades CASCADE;
    DROP TABLE IF EXISTS attendance CASCADE;
    DROP TABLE IF EXISTS subjects CASCADE;
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS schools (
        school_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT,
        contact_number CHAR(15),
        davlat_maktabi BOOL
    );

    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        contact_number CHAR(15),
        school_id INT REFERENCES schools(school_id)
    );

    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        dob DATE,
        school_id INT REFERENCES schools(school_id),
        gender CHAR(1)
    );

    CREATE TABLE IF NOT EXISTS classes (
        class_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        teacher_id INT REFERENCES teachers(teacher_id),
        school_id INT REFERENCES schools(school_id)
    );

    CREATE TABLE IF NOT EXISTS subjects (
        subject_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        class_id INT REFERENCES classes(class_id),
        teacher_id INT REFERENCES teachers(teacher_id)
    );

    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES students(student_id),
        class_id INT REFERENCES classes(class_id),
        enrollment_date DATE DEFAULT CURRENT_DATE
    );

    CREATE TABLE IF NOT EXISTS grades (
        grade_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES students(student_id),
        subject_id INT REFERENCES subjects(subject_id),
        grade_value INT,
        date_given TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id SERIAL PRIMARY KEY,
        student_id INT REFERENCES students(student_id),
        class_id INT REFERENCES classes(class_id),
        date DATE DEFAULT CURRENT_DATE
    );
''')

cursor.execute('''
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
''')

cursor.execute('''
    SELECT enrollment_id, student_id, TO_CHAR(enrollment_date, 'YYYY-MM-DD') AS enrollment_date FROM enrollments;
    SELECT grade_id, student_id, TO_CHAR(date_given, 'YYYY-MM-DD HH24:MI') AS date_given FROM grades;
    SELECT attendance_id, student_id, TO_CHAR(date, 'YYYY-MM-DD') AS date FROM attendance;
''')
products = cursor.fetchall()
for i in products:
    print(i)

cursor.execute('''
    UPDATE schools SET name = '45 - MAKTAB' WHERE school_id = 1;
    UPDATE teachers SET email = first_name || teacher_id || '@gmail.com';  
    UPDATE teachers SET email = 'ali_valiyev@example.com' WHERE teacher_id = 1;
    UPDATE classes SET name = '10-B' WHERE class_id = 1;
''')

cursor.execute('''
    DELETE FROM enrollments WHERE enrollment_id = 1;
    DELETE FROM grades WHERE grade_id = 1;
    DELETE FROM attendance WHERE attendance_id = 1;
    DELETE FROM subjects WHERE subject_id = 1;
''')

cursor.execute('''
    ALTER TABLE schools RENAME TO maktab;
    ALTER TABLE teachers RENAME TO oqituvchi;
    ALTER TABLE students RENAME TO oquvchi;
    ALTER TABLE classes RENAME TO classar;
    ALTER TABLE subjects RENAME TO fanlar;
    ALTER TABLE enrollments RENAME TO enrolmantlar;
    ALTER TABLE grades RENAME TO gradeslar;
    ALTER TABLE attendance RENAME TO attendancelar;
''')

cursor.execute('''
    SELECT * FROM maktab;
    SELECT * FROM oqituvchi;
    SELECT * FROM oquvchi;
    SELECT * FROM classar;
    SELECT * FROM fanlar;
    SELECT * FROM enrolmantlar;
    SELECT * FROM gradeslar;
    SELECT * FROM attendancelar;
''')
products = cursor.fetchall()
for i in products:
    print(i)

cursor.execute('''
    DROP TABLE IF EXISTS maktab CASCADE;
    DROP TABLE IF EXISTS oqituvchi CASCADE;
    DROP TABLE IF EXISTS oquvchi CASCADE;
    DROP TABLE IF EXISTS classar CASCADE;
    DROP TABLE IF EXISTS fanlar CASCADE;
    DROP TABLE IF EXISTS enrolmantlar CASCADE;
    DROP TABLE IF EXISTS gradeslar CASCADE;
    DROP TABLE IF EXISTS attendancelar CASCADE;
''')

db.commit()
db.close()

db.close()