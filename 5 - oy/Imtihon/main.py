import psycopg2

class Datbase:
    def __init__(self) -> None:
        self.connect = psycopg2.connect(
            database = 'postgres',
            user = 'Able',
            host = 'localhost',
            password = '123'
        )
    
    def manager(self, sql, *args, commit=False, fetchall=False, fetchone=False):
        with self.connect as connect:
            result = None
            with connect.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    connect.commit()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchone:
                    result = cursor.fetchone()
            return result
        
        self.cursor = self.connect.cursor()
        
    def create_employees(self):
        sql = '''CREATE TABLE IF NOT EXISTS employees(
            employee_id SERIAL PRIMARY KEY,
            full_name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            email VARCHAR(50) NOT NULL,
            phone VARCHAR(13) NOT NULL,
            address VARCHAR(50) NOT NULL
        );'''

        self.cursor.execute()
        self.connect.commit(sql)

    def insert_employees(self):
        sql = '''INSERT INTO employees(full_name, age, email, phone, address)VALUES
        ('Sobir', 15, 'sobir@gmail.com',  '+998 .. ... .. ..', 'Tashkent'),
        ('Jobir', 15, 'jobir@gmail.com',  '+998 .. ... .. ..', 'Fargona'),
        ('Nodir', 15, 'nodir@gmail.com',  '+998 .. ... .. ..', 'Andijon'),
        ('Ali', 15, 'ali@gmail.com',  '+998 .. ... .. ..', 'Samarqand');
        '''
        self.cursor.execute(sql)
        self.connect.commit()

    def select_employees(self):
        sql = '''SELECT * FROM employees;'''
        
        self.cursor.execute()
        self.connect.fetchall(sql)
        
    def alter_employees(self):
        sql = '''ALTER TABLE DROP COLUMN address;'''

        for employee in employee:
            sql = '''
                INSERT TABLE employees(employee_id, full_name, age, phone, adress) VALUES
                (%s, %s, %s, %s, %s);
            '''
            self.manager(sql, *employee, commit=True)

    def select_employees(self):
        sql = '''
            SELECT * FROM emplyees;
        '''
        employees = self.manager(sql, fetchall=True)
        for employee in employees:
            print(employee)

db = Datbase()