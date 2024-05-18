import colorgram
import random
from turtle import Turtle, Screen

tim = Turtle()
scr = Screen()

colors = colorgram.extract('20_001.jpg', 25)

color_list = []

tim.speed("fastest")
tim.shape("circle")
tim.penup()
scr.colormode(255)
hor = 0

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r, g, b)
    color_list.append(new_rgb_color)

tim.setpos(-200, -200)
ver = 0
hor = 0

''' Print same row of colors each time
while ver <= 9:
    while hor <= 10:
        r = int(color_list[hor][0])
        g = int(color_list[hor][1])
        b = int(color_list[hor][2])
        tim.color(r, g, b)
        print(r, g, b)
        if hor == 9 and ver == 9:
            break
        elif hor == 10:
            tim.bk(550)
            tim.left(90)
            tim.fd(50)
            tim.right(90)
            #tim.color(255,255,255)
        else:
            tim.stamp()
        tim.fd(50)
        hor += 1
    hor = 0
    ver += 1
'''

# print random colors each row (from available)
while ver <= 9:
    while hor <= 10:
        tim.color(random.choice(color_list))
        print(r, g, b)
        if hor == 9 and ver == 9:
            break
        elif hor == 10:
            tim.bk(550)
            tim.left(90)
            tim.fd(50)
            tim.right(90)
            #tim.color(255,255,255)
        else:
            tim.stamp()
        tim.fd(50)
        hor += 1
    hor = 0
    ver += 1

scr.exitonclick()
