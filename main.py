from dot import Dot
import numpy as np
import turtle

# each dot is turtle
# each dot has a brain which stores some information about the dot
# population class might be needed to store all dots and manipulate them

# TODO: create population of dots and let them randomly move around
screen = turtle.Screen()
dot = Dot(pos=(0,0), screen=screen)

dot.move()
