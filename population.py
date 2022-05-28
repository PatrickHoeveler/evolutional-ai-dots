from dot import Dot, Goal
from typing import Tuple
import random


class Population:

    def __init__(self, size: int, brain_size: int, win_size: Tuple, radius: float,  goal:Goal, batch=None):
        self.size = size
        self.brain_size = brain_size
        self.win_size = win_size
        self.radius = radius
        self.batch = batch
        self.generation_count = 0
        self.max_step = self.brain_size
        self.start_x = self.win_size[0]/2
        self.start_y = self.win_size[1]/4
        self.goal = goal

        self.generation = self.create_initial_generation()

    def create_initial_generation(self):
        generation = []

        # generation.append(self.goal)

        for i in range(self.size):
            dot = Dot(x=self.start_x, y=self.start_y, radius=self.radius,
                      batch=self.batch, win_size=self.win_size, brain_size=self.brain_size, goal_position=self.goal.position, max_step=self.max_step)

            generation.append(dot)
        return generation

    def update(self):
        # less steps should result in higher fitness
        print('all finishers distance to goal:', [x.distance_to_goal() for x in self.generation if x.finished])
        print('old best_dot distance:', self.generation[0].distance_to_goal(), 'old best_dot finished', self.generation[0].finished)
        print('old best_dot distance calculated:', [x.distance_to_goal() for x in self.generation if x.is_best])

        self.natural_selection()
        print('self.generation_count', self.generation_count)
        print('---')

    def natural_selection(self):
        # remove the 10% worst dots
        self.remove_worst_dots()

        new_generation = []
        # new_generation.append(self.goal)
        # calculate the fitness
        # dots with closest distance to the goal will have highest fitness
        fitness_sum = self.calculate_fitness_sum()

        # add best dot to generation
        best_dot = self.get_best_dot()
        new_generation.append(best_dot)
        # add new mutated babies from selected parents
        for i in range(self.size-1):
            parent_dot = self.select_parent(fitness_sum)
            # simple clone of parent will be the new baby
            baby_dot = parent_dot.clone(batch=self.batch)

            # mutate the baby
            baby_dot.mutate()
            new_generation.append(baby_dot)

        self.generation_count += 1

        # print('old_generation', self.generation)
        # print('old gen max([x.fitness for x in self.generation])', max([x.fitness for x in self.generation]))
        # print('a dot has finished', [True for x in self.generation if x.finished])
        # [print(x.position) for x in self.generation]
        self.generation = new_generation
        self.set_max_step()
        # print('--')
        # print('old_generation', self.generation, 'len', len(self.generation))
        # [print(x.position) for x in self.generation]


    def calculate_fitness_sum(self):
        fitness_sum = 0.0
        for dot in self.generation:
            fitness = 0.0
            if(type(dot) != Goal):
                if(dot.finished):
                    fitness = 1.0/16.0 + 100000.0/float(dot.index*dot.index)
                else:
                    distance_to_goal = dot.distance_to_goal()
                    fitness = 1.0/(distance_to_goal*distance_to_goal)
                # dot.fitness = round(fitness,4)
                dot.fitness = fitness
                fitness_sum += fitness
        return fitness_sum

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
        # fitness_list = [x.fitness for x in self.generation]
        # fitness_list.sort(reverse=True)
        # print('sorted fitness list', fitness_list)
        max_fitness = max([x.fitness for x in self.generation])
        # print('max_fitness', max_fitness)
        for dot in self.generation:
            # if(type(dot) != Goal):
            if(dot.fitness == max_fitness):
                self.max_step = dot.index
                best_dot = Dot(x=self.start_x, y=self.start_y, radius=self.radius,
                    batch=self.batch, win_size=self.win_size, brain_size=self.brain_size, goal_position=self.goal.position, is_best=True, max_step=self.max_step)
                best_dot.brain.directions = dot.brain.directions.copy()
                # print('old best dot.fitness and index', dot.fitness, dot.index)
                # if(dot.finished==False and dot.distance_to_goal()<3):
                    # print('---')
                    # print('last best dot', dot)
                    # print('best_dot fitness', dot.fitness, 'best_dot index', dot.index)
                    # print('best_dot finished', dot.finished, 'distance to goal', dot.distance_to_goal())
                    # print('new best_dot.index', best_dot.index, 'best_dot.max_step', best_dot.max_step)
                    # print('new best_dot obj', best_dot)
                    # print('---')
                return best_dot

    def remove_worst_dots(self):
        # remove the 10% worst dots
        sorted_dots = sorted(self.generation, key=lambda x: x.fitness, reverse=True)
        worst_dots = sorted_dots[:int(self.size*0.1)]
        for dot in worst_dots:
            if(type(dot) != Goal):
                self.generation.remove(dot)
                
    def set_max_step(self):
        for dot in self.generation:
            dot.max_step = self.max_step