# from pvector import PVector
from math import sqrt
import random
from typing import Tuple
import pyglet
from sympy import symbols, Eq, solve
from brain import Brain


class Goal():
    def __init__(self, init_position: Tuple, radius: float, batch):
        self.init_position = init_position
        self.radius = radius
        self.batch = batch
        self.color = (255, 0, 0)
        self.dot = pyglet.shapes.Circle(
            x=self.init_position[0], y=self.init_position[1], radius=self.radius, batch=self.batch, color=self.color)


class Obstacle():
    def __init__(self, position: Tuple, width: int, batch):
        self.position = position # (x,y, x2,y2)
        self.batch = batch
        self.width = width
        self.color = (255, 192, 203)
        self.line = pyglet.shapes.Line(x=self.position[0],
                                            y=self.position[1],
                                            x2=self.position[2],
                                            y2=self.position[3],
                                            width=self.width,
                                            color=self.color,
                                            batch=self.batch)


class Element():

    def __init__(self, goal: Goal, obstacles: list[Obstacle], brain_size: int, radius: float,
                 batch: pyglet.graphics.Batch, win_size: Tuple, color=(0, 0, 0), velocity=10):
        self.goal = goal
        self.obstacles = obstacles
        self.brain_size = brain_size
        self.brain = Brain(size=brain_size)
        self.init_position = (win_size[0]/2, win_size[1]/2)
        self.radius = radius
        self.batch = batch
        self.win_size = win_size

        self.color = color
        self.dot = pyglet.shapes.Circle(
            x=self.init_position[0], y=self.init_position[1], radius=self.radius, batch=self.batch, color=self.color)
        self.dead = False
        self.finished = False
        self.step = 0
        self.fitness = 0
        self.velocity = velocity

    def move(self):
        directions = self.brain.directions
        if(not self.dead and not self.finished):
            if(self.check_border_collision()):
                self.dead = True
                self.calculate_fitness()
                return 'dead'
            # no more steps
            elif(self.step == len(directions)):
                self.dead = True
                self.calculate_fitness()
                return 'dead'

            elif(self.check_goal_collision()):
                self.finished = True
                self.dot.color = (0, 0, 255)
                self.calculate_fitness()
                return 'finished'
            elif(self.check_obstacle_collision()):
                self.dead = True
                self.dot.color = (0, 0, 255)
                self.dot.y = self.obstacles[0].position[1]
                self.calculate_fitness()
                return 'dead'
            # keep moving
            else:
                self.dot.x += directions[self.step][0]*self.velocity
                self.dot.y += directions[self.step][1]*self.velocity
                self.step += 1

    def check_border_collision(self):
        return self.dot.x < 0 or self.dot.x > self.win_size[0] or self.dot.y < 0 or self.dot.y > self.win_size[1]

    def check_goal_collision(self):
        return self.distance_to_goal() < self.radius


    def solve_b(self, m, point):
        b = point[1] - m*point[0]
        return b

    def get_equation(self, point_d, point_q, x, y)->Eq:
        m = (point_q[1]-point_d[1])/(point_q[0]-point_d[0])
        b = self.solve_b(m, point_d)
        
        # y = mx+b
        # 0 = mx+b-y
        eq = Eq(m*x + b - y)
        return eq

    def check_obstacle_collision(self):
        # for all obstacles
        obstacle = self.obstacles[0]
        current_point = (self.dot.x,self.dot.y)
        next_point = (self.dot.x+self.brain.directions[self.step][0], self.dot.y+self.brain.directions[self.step][1])

        x, y = symbols('x y')
        eq_element = self.get_equation(current_point, next_point, x, y)
        eq_obstacle = self.get_equation(obstacle.position[:2], obstacle.position[2:4], x, y)
        sol = solve((eq_element, eq_obstacle),(x, y))

        if(len(sol)>0):
            intersect_x = sol[x]
            print('intersect_x', intersect_x)

            if(intersect_x > obstacle.position[0] and intersect_x < obstacle.position[2] and next_point[1]>=obstacle.position[1]):
                print('sol', sol)
                print('intersected')
                return True
            else:
                return False
        else:
            return False

    def distance_to_goal(self):
        distance = float(sqrt((self.goal.dot.x-self.dot.x)
                              ** 2 + (self.goal.dot.y-self.dot.y)**2))

        return distance



    def calculate_fitness(self):
        if(self.finished):
            fitness = 1.0/16.0 + 100000.0/float(self.step)
        else:
            fitness = 1.0/(self.distance_to_goal()**2)

        self.fitness = fitness

    def mutate(self):
        self.brain.mutate(mutation_rate=0.1)

    def clone(self, color=(0, 0, 0)):
        clone = Element(goal=self.goal, obstacles=self.obstacles, brain_size=self.brain_size, radius=self.radius,
                        batch=self.batch, win_size=self.win_size, color=color, velocity=self.velocity)
        clone.brain = self.brain.clone()
        return clone
