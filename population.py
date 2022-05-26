from dot import Dot, Goal
from typing import Tuple



class Population:

    def __init__(self, size: int,brain_size: int, win_size: Tuple, radius: float, batch=None):
        self.size = size
        self.brain_size = brain_size
        self.win_size = win_size
        self.radius = radius
        self.batch = batch
        self.dots = self.generate_dots()

    def generate_dots(self):
        dots = []
        goal_x = self.win_size[0]/2
        goal_y = self.win_size[1]-self.win_size[1]*0.1

        dot_x = self.win_size[0]/2
        dot_y = self.win_size[1]/2

        goal = Goal(x=goal_x, y=goal_y, radius=self.radius*2, color=(255, 0, 0),
                            batch=self.batch, win_size=self.win_size)
        dots.append(goal)

        for i in range(self.size):
            dot = Dot(x=dot_x, y=dot_y, radius=self.radius,
                            batch=self.batch, win_size=self.win_size, brain_size=self.brain_size, goal_pos=goal.position)

            dots.append(dot)
        return dots

    def update(self):
        print('created new population')