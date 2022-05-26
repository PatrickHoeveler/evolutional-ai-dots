# from pvector import PVector
import pyglet
import random
from typing import Tuple
from brain import Brain


class Dot(pyglet.shapes.Circle):

    def __init__(self, win_size, brain_size, color=(0, 0, 0), goal_pos=None, *args, **kwargs):
        super(Dot, self).__init__(*args, **kwargs)
        self.win_size = win_size
        self.brain_size = brain_size
        self.color = color
        self.goal_pos = goal_pos

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.brain = Brain(size=self.brain_size)
        self.dead = False
        self.index = 0

    def update(self) -> None:
        directions = self.brain.directions
        print('self.goal_pos', self.goal_pos)

        if(self.index < len(directions) and self.goal_pos):
            newx = self.x + directions[self.index][0]*10
            newy = self.y + directions[self.index][1]*10

            border_x = self.win_size[0]
            border_y = self.win_size[1]
            print(newx, newy)
            # check window borders
            if(newx > border_x or newx < -border_x or newy > border_y or newy < -border_y):
                self.dead = True
                return None
            # check if goal is reached
            elif(newx == self.goal_pos[0] and newy == self.goal_pos[1]):
                self.finished = True
                return None
            else:
                self.x = newx
                self.y = newy
                self.index += 1

    def calculate_fitness(self):
        # calculate the distance between the dot last position and the target
        # dots with closest distance to the goal will have highest fitness
        # distance_to_goal = distance(self.pos, self.target)
        # self.fitness = 1.0 / (distance_to_goal*distance_to_goal)

        # less steps should result in higher fitness
        pass
