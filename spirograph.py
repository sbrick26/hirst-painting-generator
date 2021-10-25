from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

spirograph = Turtle()
spirograph.shape("arrow")
spirograph.speed(0)

def drawCircles(numSteps, turtle):
    tiltAngle = 360.0/numSteps
    for i in range(numSteps):
        turtle.circle(50)
        turtle.left(tiltAngle)

drawCircles(30, spirograph)

screen.exitonclick()
