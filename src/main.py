from turtle import Turtle, Screen
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('image.jpeg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    if r <= 235 or g <= 235 or b <= 235:
        new_color = (r,g,b)
        rgb_colors.append(new_color)

print(rgb_colors)

screen = Screen()
screen.colormode(255)

hirst = Turtle()
hirst.shape("circle")
hirst.penup()
hirst.setpos(-200,-200)

def drawHirst():
    for y in range(10):
        hirst.setpos(-220, -200 + y*50)
        for x in range(10):
            hirst.dot(15, random.choice(rgb_colors))
            hirst.forward(50)

drawHirst()





screen.exitonclick()

