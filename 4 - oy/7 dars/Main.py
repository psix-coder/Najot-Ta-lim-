# def my_range(start, stop, step =1):
#     while start < stop:
#         yield start
#         start +=step

# print(list(my_range(1,10,1)))


#  2 Topshiriq

# def my_range(start, stop, step = 2):
#     while start < stop:
#         yield start
#         start +=step

# print(list(my_range(0,10,2)))

#  3 Topsjiriq

# def fibanachi(start, stop):
#     a, b = start, start + 1 
#     while a < stop:
#         yield a
#         a, b = b, a + b  

# print(list(fibanachi(0, 50)))

#  4 Topshiriq

# def repeat_text(text):
#     for _ in text:
#         yield _

# print(list(repeat_text("Hello Python!")))

#  5 Topshiriq

# def my_range( text):
#     for _ in text:
#         yield _

# print(list(my_range('Salom Dunyo')))

#  24 Topshiriq
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('blue')
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a +=3
    b +=1
    if b ==210:
        break
    t.hideturtle()