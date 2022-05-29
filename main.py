from turtle import pos
import numpy as np
import pyglet
from pyglet import shapes
from element import Element, Goal
from population import Population

# Variables, Considering a vertical oriented window for game
WIDTH = 800   # Game Window Width
HEIGHT = 700  # Game Window Height
BORDER = 10   # Walls Thickness/Border Thickness
RADIUS = 3
POPULATION_SIZE = 10
BRAIN_SIZE = 100


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.win_size = (WIDTH, HEIGHT)
        self.main_batch = pyglet.graphics.Batch()
        self.goal = Goal(init_position=(WIDTH/2, HEIGHT*4/5), radius=RADIUS*2, batch=self.main_batch)
        self.population = Population(
            size=POPULATION_SIZE,
            brain_size=BRAIN_SIZE,
            win_size=self.win_size,
            radius=RADIUS,
            batch=self.main_batch, 
            goal=self.goal)
        self.elements = []
        self.set_elements()


    def set_elements(self):
        self.elements = [x for x in self.population.generation]
        self.elements.append(self.goal)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()


    def update(self, dt):
        evolve_elements = False
        for element in self.elements:
            evolve_elements = len([x for x in self.elements if type(x)!= Goal and (x.dead == True or x.finished == True)]) == len(self.elements)-1
            if(evolve_elements):
                self.population.evolve()
                print('generation', self.population.generation_count)
                self.set_elements()
                break
            if(type(element) == Element):
                element.move()

        pass




if __name__ == '__main__':
    window = Window(width=WIDTH, height=HEIGHT, caption='Evolutional AI')
    pyglet.gl.glClearColor(1, 1, 1, 1)
    pyglet.clock.schedule_interval(window.update, 1/120.0)
    pyglet.app.run()
