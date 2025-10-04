import psycopg2

class Database:
    def __init__(self) -> None:
        self.database = psycopg2.connect(
            database = '8dars-amaliyot',
            user = 'postgres',
            host = 'localhost',
            password = '1'
        ) 
        
            
    def manager(self,sql,*args,commit = False,fetchone=False,fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql,args)
                if commit:
                     db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()
                    
    def create_tables(self):
        sqls = [
        '''
        create table if not exists classes(
            id serial primary key,
            clas_name varchar(50) not null,
            teacher_id integer references teachers(teacher_id),
            student_id integer references  students(student_id) 
            
         );''',
         
         '''
         create table if not exists teachers(
             id serial primary key,
             first_name varchar(50) not null,
             last_name varchar(50) not null,
             stagi integer

         );
         '''
         
         '''
         create table if not exists students(
            id serial primary key,
            first_name varchar(50) not null,
            last_name varchar(50) not null
         )
         '''
        ]
    

