from element import Element, Goal, Obstacle
from typing import Tuple
import random


class Population:

    def __init__(self, size: int, brain_size: int, win_size: Tuple, radius: float,  goal: Goal, obstacles: list[Obstacle], velocity: int, batch=None):
        self.size = size
        self.brain_size = brain_size
        self.win_size = win_size
        self.radius = radius
        self.batch = batch
        self.generation_count = 0
        self.goal = goal
        self.obstacles = obstacles
        self.velocity = velocity
        self.generation = []
        self.set_initial_generation()
        self.best_fitness_not_increased_count = 0
        self.best_fitness = 0.0

    def set_initial_generation(self):
        generation = []
        for i in range(self.size):
            element = Element(goal=self.goal,
                              obstacles=self.obstacles,
                              brain_size=self.brain_size,
                              radius=self.radius,
                              batch=self.batch,
                              win_size=self.win_size,
                              velocity=self.velocity)
            generation.append(element)
        self.generation = generation

    def evolve(self):
        # self.generation = []
        self.natural_selection()

        # self.set_initial_generation()

    def natural_selection(self):
        new_generation = []
        # remove worst rate of population
        self.remove_worst(rate=0.20)

        fitness_sum = self.calculate_fitness_sum()

        # add best dot to generation
        best_element = [x for x in self.generation if x.fitness == max(
            self.generation, key=lambda x: x.fitness).fitness][0]

        new_generation.append(best_element.clone(color=(0, 255, 0)))

        # TODO: if the best dot of the population is not increasing its fitness for a while,
        # then create more copies of it
        if(self.best_fitness == best_element.fitness):
            self.best_fitness_not_increased_count += 1
        else:
            self.best_fitness_not_increased_count = 0
            self.best_fitness = best_element.fitness
        if(self.best_fitness_not_increased_count > 10):
            for i in range(int(self.size*0.05)):
                new_generation.append(best_element.clone())

        print('best_element.fitness', best_element.fitness,
              'self.best_fitness_not_increased_count', self.best_fitness_not_increased_count)

        # add remaining population to generation
        for i in range(self.size-len(new_generation)):
            parent_element = self.select_parent(fitness_sum)
            child_element = parent_element.clone()

            # mutate the baby
            child_element.mutate()
            new_generation.append(child_element)

        self.generation = new_generation
        self.generation_count += 1

    def calculate_fitness_sum(self):
        fitness_sum = 0
        for element in self.generation:
            fitness_sum += element.fitness
        return fitness_sum

    def select_parent(self, fitness_sum: float):
        # select parent based on fitness
        rand = random.uniform(0, fitness_sum)
        running_sum = 0.0
        for element in self.generation:
            running_sum += element.fitness
            if(running_sum >= rand):
                return element

    def remove_worst(self, rate: float):
        # remove worst rate of population
        self.generation.sort(key=lambda x: x.fitness, reverse=True)
        for i in range(int(self.size*rate)):
            self.generation.pop()
