from dot import Dot, Goal
from typing import Tuple
import random


class Population:

    def __init__(self, size: int, brain_size: int, win_size: Tuple, radius: float, batch=None):
        self.size = size
        self.brain_size = brain_size
        self.win_size = win_size
        self.radius = radius
        self.batch = batch
        self.generation_count = 0

        goal_x = self.win_size[0]/2
        goal_y = self.win_size[1]-self.win_size[1]*0.1
        self.goal = Goal(x=goal_x, y=goal_y, radius=self.radius*2, color=(255, 0, 0),
                         batch=self.batch, win_size=self.win_size)

        self.generation = self.create_initial_generation()

    def create_initial_generation(self):
        generation = []

        dot_x = self.win_size[0]/2
        dot_y = self.win_size[1]/2

        generation.append(self.goal)

        for i in range(self.size):
            dot = Dot(x=dot_x, y=dot_y, radius=self.radius,
                      batch=self.batch, win_size=self.win_size, brain_size=self.brain_size, goal_position=self.goal.position)

            generation.append(dot)
        return generation

    def update(self):
        # less steps should result in higher fitness
        self.natural_selection()

    def natural_selection(self):
        new_generation = []
        new_generation.append(self.goal)
        # calculate the fitness
        # dots with closest distance to the goal will have highest fitness
        fitness_sum = self.calculate_fitness_sum()

        # add best dot to generation
        best_dot = self.get_best_dot()
        new_generation.append(best_dot)

        for dot in self.generation:
            if(type(dot) != Goal and dot != best_dot):
                parent_dot = self.select_parent(fitness_sum)
                # simple clone of parent will be the new baby
                baby_dot = parent_dot.clone(batch=self.batch)
                # mutate the baby
                baby_dot.mutate()
                new_generation.append(baby_dot)

        self.generation_count += 1

        # print('old_generation', self.generation)
        [print(x.position) for x in self.generation]
        self.generation = new_generation
        print('--')
        [print(x.position) for x in self.generation]
        # print('new generation', self.generation)

    def calculate_fitness_sum(self):
        fitness_sum = 0.0
        for dot in self.generation:
            if(type(dot) != Goal):
                if(dot.finished):
                    fitness = 1/16.0 * 10000.0/dot.index*dot.index
                else:
                    distance_to_goal = dot.distance_to_goal()
                    fitness = 1/(distance_to_goal*distance_to_goal)
                dot.fitness = fitness
                # dot.set_fitness(fitness)
                fitness_sum += fitness
        return fitness_sum

    def select_parent(self, fitness_sum: float):
        # select parent based on fitness
        rand = random.uniform(0, fitness_sum)
        running_sum = 0.0
        for dot in self.generation:
            if(type(dot) != Goal):
                running_sum += dot.fitness
                if(running_sum >= rand):
                    return dot

    def get_best_dot(self):
        max_fitness = max([x.fitness for x in self.generation])
        for dot in self.generation:
            if(type(dot) != Goal):
                if(dot.fitness == max_fitness):
                    dot.set_best()
                    return dot

