from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
dot_screen = Screen()
dot_screen.colormode(255)
dot_screen.screensize(2000, 2000)

'''
colors = colorgram.extract('the girl with the pearl.jpg', 10)
print(colors[0])
# <colorgram.py Color: Rgb(r=20, g=13, b=19), 39.22355259303967%>

rgb_colors = []

for i in range(0, 10):
    # color_ticket = colors[i].rgb
    # rgb_colors.append(color_ticket)
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    color_ticket = (r, g, b)
    rgb_colors.append(color_ticket)

print(rgb_colors)
'''
# delete the color i don't want and save into list
color_list = [(15, 14, 23), (121, 87, 66), (52, 36, 30), (195, 156, 116), (240, 211, 189),
(67, 84, 135), (95, 50, 40), (224, 195, 141), (41, 55, 106)]

tim.speed(0)

for i in range(0, 10):
    for j in range(0, 10):
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    if (i % 2) == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(50)
    else:
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.forward(50)
# make the turtle shape disappear
tim.shape("blank")

'''
you can also make the turtle disappear in the very beginning of the code with
tim.hideturtle()
'''

dot_screen.exitonclick()