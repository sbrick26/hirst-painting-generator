from turtle import Turtle, Screen
import random

screen = Screen()

randomWalk = Turtle()
randomWalk.shape("arrow")
randomWalk.pensize(15)
randomWalk.speed(10)

screen.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple = (r, g, b)
    return tuple

turnAngles = [0, 90, 180, 270]
# colors = ["red", "blue", "green", "black", "orange", "purple", "yellow"]

def randomStep(numSteps, turtle):
    for i in range(numSteps + 1):
        direction = random.choice(turnAngles)
        turtle.color(randomColor())
        turtle.setheading(direction)
        turtle.forward(30)

# Increase Parameter "numSteps" to change number of steps in 2D Random Walk

randomStep(100, randomWalk)

screen.exitonclick()
