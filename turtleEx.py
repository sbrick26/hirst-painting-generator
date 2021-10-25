from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Challenge 1

timmy_the_turtle.shape("arrow")

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# Challenge 2
timmy_the_turtle.clear()
for i in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pendown()

# Challenge 3
timmy_the_turtle.clear()

colors = ["red", "green", "yellow", "blue"]

def drawShape(numSides, turtle):
    interior_angle = (numSides - 2)*180
    angle = 180 - interior_angle/numSides
    for i in range(numSides):
        turtle.forward(100)
        turtle.left(angle)

challenge_3 = Turtle()
challenge_3.shape("arrow")

for i in range(3,11):
    challenge_3.color(random.choice(colors))
    drawShape(i, challenge_3)

challenge_3.clear()

screen = Screen() 
screen.exitonclick()
