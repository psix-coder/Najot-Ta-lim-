from collections import  namedtuple

students = (
    {"id": 45625, "name": "MuhammadRizo", "age": 14, "course": "Python"},
    {"id": 45626, "name": "Muhammadjon", "age": 17, "course": "Python"},
    {"id": 35624, "name": "Safobek", "age": 16, "course": "Python"},
    {"id": 32555, "name": "Qahramon", "age": 18, "course": "Python"},
    {"id": 36566, "name": "Mubina", "age": 15, "course": "Python"},
)


students = namedtuple("Student", ["id", "name", "age"])

i = ["id": 45625, ]

i = int(input("ID kiriting: "))

if i in students:
    for i in students:
        print(f"")