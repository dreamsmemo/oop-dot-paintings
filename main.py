from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("skyblue")
tim.pencolor("cyan")
tim.pensize(1)

turtle_screen = Screen()

'''
for i in range(0, 4):
    tim.forward(100)
    tim.right(90)
'''

'''
# changing the pen color
for i in range(0, 10):
    tim.forward(5)
    tim.pencolor("white")
    tim.forward(5)
    tim.color("cyan")
'''

'''
# using pen up and pen down
for i in range(0, 10):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
'''

'''
# drawing different shapes
for i in range(0, 7):
    a = 0
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    turtle_screen.colormode(255)
    tim.pencolor((R, G, B))
    while a < (i + 3):
        tim.forward(100)
        tim.right(360 / (i + 3))
        a += 1
'''

'''
# draw a random walk and speed up the turtle
tim.speed(0)
for i in range(0, 200):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    turtle_screen.colormode(255)
    tim.pencolor((R, G, B))
    distance = random.randint(-30, 30)
    tim.forward(distance)
    tim.setheading(random.choice([0, 90, 180, 270]))
'''

'''
# make a spirograph with radius of a hundred
tim.speed(0)
for i in range(0, 120):
    tim.circle(100)
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    turtle_screen.colormode(255)
    tim.pencolor((R, G, B))
    tim.right(3)
'''


turtle_screen.exitonclick()
