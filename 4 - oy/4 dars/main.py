from collections import namedtuple


# class Person:
#     def __init__(self, user_id, name, lastname):
#         self.user_id = user_id
#         self.name = name
#         self.lastname = lastname



phones = (
    {"id": 1, "name": "Samsung Galaxy 1", "color": "red"},
    {"id": 2, "name": "Samsung Galaxy 2", "color": "blue"},
    {"id": 3, "name": "Samsung Galaxy 3", "color": "green"},
    {"id": 4, "name": "Samsung Galaxy 4", "color": "white"},
    {"id": 5, "name": "Samsung Galaxy 5", "color": "yellow"},
)

Person = namedtuple("Person", "user_id name lastname course")


for phone in phones:
    p = Person(**phone)
    print(p.user_id, p.name, p.lastname)

