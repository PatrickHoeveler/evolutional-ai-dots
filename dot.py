# from pvector import PVector
import turtle

from brain import Brain


class Dot:
    def __init__(self, brainsize: int, pos: tuple, screen: turtle.Screen, goal: turtle.Turtle):

        self.brainsize = brainsize
        self.pos = pos
        self.screen = screen
        self.goal = goal


        self.brain = Brain(size=self.brainsize)
        self.dead = False
        self.finished = False

    def move(self):
        directions = self.brain.directions
        


    def get_direction(self, index: int):
        return self.brain.directions[index]

    def calculate_fitness(self):
        # calculate the distance between the dot last position and the target
        # dots with closest distance to the goal will have highest fitness
        # distance_to_goal = distance(self.pos, self.target)
        # self.fitness = 1.0 / (distance_to_goal*distance_to_goal)

        # less steps should result in higher fitness
        pass

    def kill_dot(self):
        self.dead = True
        
    def finish(self):
        self.finished = True