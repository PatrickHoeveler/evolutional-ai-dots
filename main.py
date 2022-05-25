from dot import Dot
import numpy as np
import turtle

# each dot is turtle
# each dot has a brain which stores some information about the dot
# population class might be needed to store all dots and manipulate them

screen = turtle.Screen()

# goal
goal = turtle.Turtle(visible=False)
goal.speed(0)
goal.penup()
goal.shape("circle")
goal.shapesize(0.5, 0.5, 1)
goal.color("green")
goal.sety(screen.window_height()/2-20)
goal.showturtle()

dot = Dot(pos=(0,0), screen=screen)
dot.move()
