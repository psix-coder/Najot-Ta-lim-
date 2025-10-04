import psycopg2

connection = psycopg2.connect(
    host="localhost",      
    database="postgres",  
    user="Able", 
    password="123" 
)

cursor = connection.cursor()

try:
    cursor.execute("""
        DROP TABLE IF EXISTS students CASCADE;
        DROP TABLE IF EXISTS courses CASCADE;
        DROP TABLE IF EXISTS enrollments CASCADE;
        DROP TABLE IF EXISTS teachers CASCADE;
        DROP TABLE IF EXISTS course_assignments CASCADE;
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            age INT CHECK (age > 0),
            email VARCHAR(100) UNIQUE NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            course_code VARCHAR(10) UNIQUE NOT NULL,
            credits INT CHECK (credits BETWEEN 1 and 5)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id SERIAL PRIMARY KEY,
            enrollment_date DATE DEFAULT CURRENT_DATE,
            student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(course_id) ON DELETE SET NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            experience_years INT CHECK (experience_years >= 0)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS course_assignments (
            assignment_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
            teacher_id INT REFERENCES teachers(teacher_id) ON DELETE SET DEFAULT
        );
    """)

    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, email) VALUES 
        ('John', 'Doe', 20, 'john.doe@example.com'),
        ('Jane', 'Smith', 22, 'jane.smith@example.com'),
        ('Emily', 'Davis', 19, 'emily.davis@example.com'),
        ('Michael', 'Johnson', 23, 'michael.johnson@example.com'),
        ('Sarah', 'Brown', 21, 'sarah.brown@example.com'),
        ('David', 'Wilson', 20, 'david.wilson@example.com'), 
        ('Emma', 'Taylor', 22, 'emma.taylor@example.com');
    """)

    cursor.execute("""
        INSERT INTO courses (course_name, course_code, credits) VALUES 
        ('Mathematics', 'MATH101', 4),
        ('English Literature', 'ENG202', 3),
        ('Computer Science', 'CS303', 5);
    """)

    cursor.execute("""
        INSERT INTO teachers (first_name, last_name, experience_years) VALUES 
        ('Alan', 'White', 10), 
        ('Laura', 'Green', 8);
    """)

    cursor.execute("""
        INSERT INTO course_assignments (course_id, teacher_id) VALUES 
        (1, 1),  
        (3, 2);
    """)

    cursor.execute("ALTER TABLE students RENAME TO student_info;")

    cursor.execute("ALTER TABLE student_info RENAME COLUMN age TO student_age;")

    cursor.execute("""
        UPDATE student_info
        SET student_age = 25
        WHERE student_id IN (1, 3);
    """)
   
    cursor.execute("""
        DELETE FROM student_info
        WHERE student_id IN (2, 5);
    """)

    connection.commit()

    cursor.execute("SELECT * FROM student_info;")
    print("Students:", cursor.fetchall())

    cursor.execute("SELECT * FROM courses;")
    print("Courses:", cursor.fetchall())

    cursor.execute("SELECT * FROM enrollments;")
    print("Enrollments:", cursor.fetchall())

    cursor.execute("SELECT * FROM teachers;")
    print("Teachers:", cursor.fetchall())

    cursor.execute("SELECT * FROM course_assignments;")
    print("Course Assignments:", cursor.fetchall())

except Exception as e:
    print("Xatolik:", e)
    connection.rollback()
finally:
    cursor.close()
    connection.close()
