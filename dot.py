# from pvector import PVector
from math import sqrt
import random
import pyglet
from typing import Tuple
from brain import Brain


class Dot(pyglet.shapes.Circle):

    def __init__(self, win_size=(1200, 800), brain_size=10, color=(0, 0, 0), goal_position=None, is_best=False, max_step=10, *args, **kwargs):
        super(Dot, self).__init__(*args, **kwargs)
        self.win_size = win_size
        self.brain_size = brain_size
        self.color = color
        self.goal_position = goal_position
        self.is_best = is_best
        if(self.is_best):
            self.color = (0, 255, 0)

        self.max_step = max_step

        self.brain = Brain(size=self.brain_size)
        self.dead = False
        self.finished = False
        self.index = 0
        self.fitness = 0.0
        self.start_position = (self.x, self.y)


    def move(self) -> None:
        directions = self.brain.directions
        # print('self.goal_position', self.goal_position)

        if(self.index < len(directions) and self.index < self.max_step):
            newx = self.x + directions[self.index][0]*10
            newy = self.y + directions[self.index][1]*10

            border_x = self.win_size[0]
            border_y = self.win_size[1]
            # print(newx, newy)
            # check window borders
            if(self.is_best):
                print('distance, radius, index', self.distance_to_goal(), float(self.radius), self.index)
            if(newx > border_x or newx < 0 or newy > border_y or newy < 0):
                print('hit border')
                self.dead = True
                return None
            # check if goal is reached
            # elif(self.distance_to_goal() < self.radius):
            # elif(self.x == self.goal_position[0] and self.y == self.goal_position[1]):
            elif(self.distance_to_goal() < float(self.radius)):
                # print('self.radius', self.radius, 'round(self.distance_to_goal(), 4)', round(self.distance_to_goal(), 4))
                # print('goal reached: self.index', self.index)
                self.finished = True
                return None
            else:
                self.x = newx
                self.y = newy
                self.index += 1
        else:
            self.dead = True
            return None

    def distance_to_goal(self):
        # calculate the distance between the dot last position and the target
        distance = sqrt((self.goal_position[0]-self.position[0])
                        **2 + (self.goal_position[1]-self.position[1])**2)
        # print('distance', round(distance, 4), 'radius', self.radius, 'is_best', self.is_best)
        # print('distance to goal', distance)
        
        return distance

    # def set_fitness(self, fitness: float):
    #     self.fitness = fitness

    def clone(self, batch):
        clone = Dot(x=self.start_position[0], y=self.start_position[1], radius=self.radius, win_size=self.win_size,
                    brain_size=self.brain_size, goal_position=self.goal_position, batch=batch)
        clone.brain = self.brain.clone()
        return clone

    def mutate(self):
        self.brain.mutate()


class Goal(Dot):
    def __init__(self, win_size, color=(255, 0, 0), *args, **kwargs):
        super(Goal, self).__init__(*args, **kwargs)
        self.win_size = win_size
        self.color = color
