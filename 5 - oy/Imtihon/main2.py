from main2 import db
from collections import namedtuple

employees = namedtuple('Employee', ['employee_id', 'full_name', 'age', 'email', 'phone', 'address'])
employee = db.select_employees()


# db.insert_employees()
# db.select_employees()
# db.alter_employees()
# db.select_employees()

for employee in employees:
    emp = employees(*employee)
    print(f"{emp.full_name} | {emp.age} | {emp.email} | {emp.phone} | {emp.address}")

print("- - - - - - - - - - -")


db.close()