from element import Element, Goal
from typing import Tuple
import random


class Population:

    def __init__(self, size: int, brain_size: int, win_size: Tuple, radius: float,  goal: Goal, batch=None):
        self.size = size
        self.brain_size = brain_size
        self.win_size = win_size
        self.radius = radius
        self.batch = batch
        self.generation_count = 0
        self.goal = goal
        self.generation = []
        self.set_initial_generation()

    def set_initial_generation(self):
        generation = []
        for i in range(self.size):
            element = Element(goal=self.goal,
                              brain_size=self.brain_size,
                              radius=self.radius,
                              batch=self.batch,
                              win_size=self.win_size)
            generation.append(element)
        self.generation = generation

    def update(self):
        self.generation = []
        print('updated generation')
        # self.natural_selection()

    def natural_selection(self):
        pass
        # new_generation = []
        # fitness_sum = self.calculate_fitness_sum()
        # add best dot to generation
        # best_dot = self.get_best_dot()
        # new_generation.append(best_dot)
        # add new mutated babies from selected parents
        # for i in range(self.size-1):
        #     parent_dot = self.select_parent(fitness_sum)
        #     # simple clone of parent will be the new baby
        #     baby_dot = parent_dot.clone(batch=self.batch)

        #     # mutate the baby
        #     baby_dot.mutate()
        #     new_generation.append(baby_dot)

        # self.generation_count += 1

    def calculate_fitness_sum(self):
        # TODO: get fitness sum of all dots
        pass

    def select_parent(self, fitness_sum: float):
        # select parent based on fitness
        rand = random.uniform(0, fitness_sum)
        running_sum = 0.0
        for dot in self.generation:
            # if(type(dot) != Goal):
            running_sum += dot.fitness
            if(running_sum >= rand):
                return dot

    def get_best_dot(self):
        # TODO: get best dot by highest fitness
        pass
