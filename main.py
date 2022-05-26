from dot import Dot
import numpy as np
# import turtle
# from multiprocessing import Pool

# # each dot is turtle
# # each dot has a brain which stores some information about the dot
# # population class might be needed to store all dots and manipulate them

# screen = turtle.Screen()

# # goal
# goal = turtle.Turtle(visible=False)
# goal.speed(0)
# goal.penup()
# goal.shape("circle")
# goal.shapesize(0.5, 0.5, 1)
# goal.color("green")
# goal.sety(screen.window_height()/2-20)
# # goal.sety(20)
# goal.showturtle()


# population = []

# for i in range(10):
#     dot = Dot(brainsize=100, pos=(0,0), screen=screen, goal=goal)
#     population.append(dot)
# print('population', population)

# for dot in population:
#     dot.move()


# turtle.done()

# import pygame module in this program
import pygame
import time

background_colour = (255,255,255)

width = 1200
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Evolutional AI')
red = (200,0,0)

circleX = 100
circleY = 100
radius = 10

screen.fill(background_colour)
# pygame.display.flip()

running = True

# run dot moving here
for i in range(5):
        # screen.fill(background_colour)
        pygame.draw.circle(screen,red,(circleX,circleY-i*10),radius)
        # pygame.draw.circle(screen,red,(circleX,circleY-20),radius)

while running:
    # print(pygame.mouse.get_pos())

    # pygame.draw.circle(screen,red,(circleX,circleY),radius)
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

