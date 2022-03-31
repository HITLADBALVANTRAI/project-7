import turtle
import random

def input(draw_circle):
    circle=inp(input("enter the color of circle:"))
    radius=inp(input("enter the radius of circle:"))
    turtle.penup()
    (turtle.color(color))
    turtle.goto(random.randint(-150,150)+20,random.randint(-150,150)+20)
    (turtle.begin_fill())
    turtle.circle(radius)
    (turtle.end_fill())
    turtle.pendown()
    turtle.pencolor("black")
    turtle.goto(0,-200)
    turtle.stamp()
draw_circle()
draw_circle()
draw_circle()
draw_circle()
