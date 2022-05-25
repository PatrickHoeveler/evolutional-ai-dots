# from pvector import PVector
import numpy as np
import turtle

from brain import Brain


class Dot:
    def __init__(self, pos: tuple, screen: turtle.Screen):

        self.pos = pos
        self.screen = screen

        self.shelly = turtle.Turtle()
        # self.shelly.shape("circle")
        # self.shelly.shapesize(0.2, 0.2, 1)
        self.shelly.speed(0)
        self.shelly.pendown()
        self.shelly.goto(pos)
        self.border_x = self.screen.window_width() / 2 - 0.02*self.screen.window_width()
        self.border_y = self.screen.window_height() / 2 - 0.02*self.screen.window_height()
        stepsize = int(0.02*self.border_x if self.border_x > self.border_y else 0.02*self.border_y)
        self.brain = Brain(size=400, stepsize=stepsize)
        self.dead = False

    def move(self):
        directions = self.brain.directions

        for dir in directions:
            self.shelly.forward(dir[0])
            self.shelly.setheading(dir[1])

            shelly_x = self.shelly.pos()[0]
            shelly_y = self.shelly.pos()[1]

            if(shelly_x > self.border_x or shelly_x < -self.border_x or shelly_y > self.border_y or shelly_y < -self.border_y):
                self.dead = True
                # print('out of window for pos', self.shelly.pos())
                self.shelly.dot()
                return turtle.done()

        # print('moved in all directions')
        turtle.done()

    def calculate_fitness(self):
        # calculate the distance between the dot last position and the target
        # dots with closest distance to the goal will have highest fitness
        # distance_to_goal = distance(self.pos, self.target)
        # self.fitness = 1.0 / (distance_to_goal*distance_to_goal)

        # less steps should result in higher fitness
        pass
