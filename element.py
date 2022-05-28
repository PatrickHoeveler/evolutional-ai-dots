# from pvector import PVector
from math import sqrt
import random
import pyglet
from typing import Tuple
from brain import Brain

class Goal():
    def __init__(self, init_position: Tuple, radius: float, batch):
        self.init_position = init_position
        self.radius = radius
        self.batch = batch
        self.color = (255, 0, 0)
        self.dot = pyglet.shapes.Circle(x=self.init_position[0], y=self.init_position[1], radius=self.radius, batch=self.batch, color=self.color)

class Element():

    def __init__(self, goal:Goal, brain_size: int, radius: float, batch: pyglet.graphics.Batch, win_size: Tuple):
        self.goal = goal
        self.brain = Brain(size=brain_size)
        self.init_position = (win_size[0]/2, win_size[1]/2)
        self.radius = radius
        self.batch = batch
        self.win_size = win_size
        self.color = (0, 0, 0)
        self.dot = pyglet.shapes.Circle(x=self.init_position[0], y=self.init_position[1], radius=self.radius, batch=self.batch, color=self.color)

    def move(self) -> None:
        directions = self.brain.directions

    def distance_to_goal(self):
        # calculate the distance between the dot last position and the target
        distance = sqrt((self.goal_position[0]-self.position[0])
                        ** 2 + (self.goal_position[1]-self.position[1])**2)
        # print('distance', round(distance, 4), 'radius', self.radius, 'is_best', self.is_best)
        # print('distance to goal', distance)

        return distance

    def calculate_fitness(self):
        # if(dot.finished):
        #     fitness = 1.0/16.0 + 100000.0/float(dot.index*dot.index)
        # else:
        #     distance_to_goal = dot.distance_to_goal()
        #     fitness = 1.0/(distance_to_goal*distance_to_goal)
        pass

    def mutate(self):
        self.brain.mutate()
