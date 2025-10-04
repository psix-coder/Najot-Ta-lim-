DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS projects CASCADE;




CREATE TABLE IF NOT EXISTS departments(
	id SERIAL PRIMARY KEY,
	department_name VARCHAR(50) NOT NULL
);


CREATE TABLE IF NOT EXISTS employees(
	id SERIAL PRIMARY KEY,
	f_name VARCHAR(50) NOT NULL,
	l_name VARCHAR(50) NOT NULL,
	position VARCHAR(50) NOT NULL,
	salary NUMERIC(10, 2),
	hire_date DATE DEFAULT CURRENT_DATE,
	department_id INT REFERENCES departments(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS projects(
	id SERIAL PRIMARY KEY,
	project_name VARCHAR(100) NOT NULL,
	start_date DATE DEFAULT CURRENT_DATE,
	end_date DATE DEFAULT CURRENT_DATE,
	budget NUMERIC(10, 2)
);


INSERT INTO departments (department_name) VALUES
('Human Resources'),
('Finance'),
('IT'),
('Marketing'),
('Sales');

INSERT INTO employees (f_name, l_name, position, salary, hire_date, department_id) VALUES
('John', 'Doe', 'HR Manager', 75000.00, '2023-01-15', 1),
('Jane', 'Smith', 'Financial Analyst', 65000.00, '2023-02-20', 2),
('Michael', 'Johnson', 'Software Developer', 85000.00, '2023-03-10', 3),
('Emily', 'Davis', 'Marketing Specialist', 60000.00, '2023-04-25', 4),
('Robert', 'Brown', 'Sales Representative', 55000.00, '2023-05-30', 5);

INSERT INTO projects (project_name, start_date, end_date, budget) VALUES
('Website Redesign', '2023-06-01', '2023-09-30', 12000.00),
('New Product Launch', '2023-07-15', '2023-12-31', 25000.00),
('IT Infrastructure Upgrade', '2023-08-01', '2024-01-31', 18000.00),
('Social Media Campaign', '2023-09-10', '2023-11-20', 8000.00),
('Employee Training Program', '2023-10-05', '2024-02-15', 15000.00);



SELECT 
    f_name || ' ' || l_name AS "Full Name"
FROM 
    employees;


-- Order
SELECT 
    * 
FROM 
    employees
ORDER BY 
    salary DESC;


-- WHERE

SELECT
	*
FROM
	employees
WHERE
	salary > 2500;

SELECT 
    f_name, l_name, position, salary 
FROM 
    employees
WHERE 
    salary > 2500;

-- LIMIT va FETCH
SELECT 
    * 
FROM 
    employees
ORDER BY 
    salary DESC
LIMIT 3;

-- IN
SELECT 
    * 
FROM 
    employees
WHERE 
    salary IN (2400,  3000);
-- BETWEEN
SELECT 
	*
FROM
	employees
WHERE 
	salary BETWEEN 2400 AND 3000;
-- Like
SELECT 
    * 
FROM 
    employees
WHERE 
    f_name LIKE '%a%';
-- IS Null
SELECT 
    * 
FROM 
    projects
WHERE 
    end_date IS NULL;
-- Group BY
SELECT 
    department_id, 
    AVG(salary) AS average_salary
FROM 
    employees
GROUP BY 
    department_id;


SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM projects;