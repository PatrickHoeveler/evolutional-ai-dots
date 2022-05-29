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

    def __init__(self, goal:Goal, brain_size: int, radius: float, batch: pyglet.graphics.Batch, win_size: Tuple, color=(0,0,0)):
        self.goal = goal
        self.brain_size = brain_size
        self.brain = Brain(size=brain_size)
        self.init_position = (win_size[0]/2, win_size[1]/2)
        self.radius = radius
        self.batch = batch
        self.win_size = win_size

        self.color = color
        self.dot = pyglet.shapes.Circle(x=self.init_position[0], y=self.init_position[1], radius=self.radius, batch=self.batch, color=self.color)
        self.dead = False
        self.finished = False
        self.step = 0
        self.fitness = 0

    def move(self):
        directions = self.brain.directions

        # out of window
        if(self.dot.x < 0 or self.dot.x > self.win_size[0] or self.dot.y < 0 or self.dot.y > self.win_size[1]):
            self.dead = True
            self.calculate_fitness()
            return 'dead'
        # no more steps
        elif(self.step == len(directions)):
            self.dead = True
            self.calculate_fitness()
            return 'dead'
        # hit the goal
        elif(self.distance_to_goal() < self.radius):
            self.finished = True
            self.dot.color = (0, 0, 255)
            self.calculate_fitness()
            return 'finished'
        # keep moving
        else:
            self.dot.x+=directions[self.step][0]*10
            self.dot.y+=directions[self.step][1]*10
            self.step += 1

    def distance_to_goal(self):
        distance = float(sqrt((self.goal.dot.x-self.dot.x)
                        ** 2 + (self.goal.dot.y-self.dot.y)**2))

        return distance

    def calculate_fitness(self):
        if(self.finished):
            fitness = 1.0/16.0 + 100000.0/float(self.step**2)
        else:
            fitness = 1.0/(self.distance_to_goal()**2)

        self.fitness = fitness

    def mutate(self):
        self.brain.mutate(mutation_rate=0.1)

    def clone(self, color=(0,0,0)):
        clone = Element(goal=self.goal, brain_size=self.brain_size, radius=self.radius, batch=self.batch, win_size=self.win_size, color=color)
        clone.brain = self.brain.clone()
        return clone