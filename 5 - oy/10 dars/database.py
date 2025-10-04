import psycopg2

class Database:
    def __init__(self):
        self.connect = psycopg2.connect(
            database='autosalon',
            user='postgres',
            host='localhost',
            password='123'
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

    def select_models(self):
        sql = """SELECT models.model_name, brands.brand_name, colors.color_name FROM models 
            JOIN brands USING(brand_id) 
            JOIN colors USING(color_id)
        """
        return self.manager(sql, fetchall=True)

    def select_email(self):
        sql = """SELECT email FROM employees UNION ALL SELECT email FROM customers;"""
        return self.manager(sql, fetchall=True)

    def select_country(self):
        sql = """
            SELECT country, COUNT(country) FROM customers GROUP BY country ORDER BY country;
        """
        return self.manager(sql, fetchall=True)

    def select_employees(self):
        sql = """
            SELECT country, COUNT(employee_id) FROM employees GROUP BY country ORDER BY country;
        """
        return self.manager(sql, fetchall=True)

    def select_brands(self):
        sql = """
            SELECT brands.brand_name, COUNT(models.model_name) FROM models JOIN brands USING(brand_id) GROUP BY brands.brand_name;
        """
        return self.manager(sql, fetchall=True)

    def select_brands_2(self):
        sql = """
            SELECT brands.brand_name, COUNT(models.model_name) FROM models JOIN brands USING(brand_id) GROUP BY brands.brand_name HAVING COUNT(models.model_name) > 5;
        """
        return self.manager(sql, fetchall=True)

    def show_tables(self):
        sql = """SELECT 
            orders.order_id,
            customers.first_name AS customer_first_name,
            customers.last_name AS customer_last_name,
            employees.first_name AS employee_first_name,
            employees.last_name AS employee_last_name,
            models.model_name,
            models.model_price,
            orders.car_count,
            orders.order_date
        FROM 
            orders
        JOIN 
            customers ON orders.customer_id = customers.customer_id
        JOIN 
            employees ON orders.employee_id = employees.employee_id
        JOIN 
            models ON orders.model_id = models.model_id;
        """
        return self.manager(sql, fetchall=True)

    def sum_models_price(self):
        sql = """
            SELECT SUM(model_price) FROM models;
        """
        return self.manager(sql, fetchone=True)

    def brand_counts(self):
        sql = """
            SELECT COUNT(brand_id) FROM brands;
        """
        return self.manager(sql, fetchone=True)

    def select_all_brands(self):
        sql = """
            SELECT * FROM brands;
        """
        return self.manager(sql, fetchall=True)

    def select_colors(self):
        sql = """
            SELECT * FROM colors;
        """
        return self.manager(sql, fetchall=True)

    def insert_brands(self, brand_name):
        sql = """
            INSERT INTO brands(brand_name) VALUES (%s) ON CONFLICT DO NOTHING
        """
        self.manager(sql, brand_name, commit=True)

    def insert_colors(self, color_name):
        sql = """
            INSERT INTO colors(color_name) VALUES (%s) ON CONFLICT DO NOTHING
        """
        self.manager(sql, color_name, commit=True)

    def insert_models(self, model_name, model_price, brand_id, color_id, car_count):
        sql = """
            INSERT INTO models(model_name, model_price, brand_id, color_id, car_count) 
            VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
        """
        self.manager(sql, model_name, model_price, brand_id, color_id, car_count, commit=True)

connect = Database()