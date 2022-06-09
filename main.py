import numpy as np
import pyglet
from pyglet import shapes
from element import Element, Goal, Obstacle
from population import Population

# Variables, Considering a vertical oriented window for game
WIDTH = 800   # Game Window Width
HEIGHT = 700  # Game Window Height
BORDER = 10   # Walls Thickness/Border Thickness
RADIUS = 3
POPULATION_SIZE = 200
BRAIN_SIZE = 50
VELOCITY = 30


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.win_size = (WIDTH, HEIGHT)
        self.main_batch = pyglet.graphics.Batch()
        self.goal = Goal(init_position=(WIDTH/2, HEIGHT*4/5),
                         radius=RADIUS*2, batch=self.main_batch)
        self.stats_label = pyglet.text.Label('Hello, world',
                          font_name='Arial',color=(0,0,0, 255),
                          font_size=12,
                          x=WIDTH*0.05, y=HEIGHT*0.95, batch=self.main_batch)
        self.obstacles = []
        self.set_obstacles()
        self.population = Population(
            size=POPULATION_SIZE,
            brain_size=BRAIN_SIZE,
            win_size=self.win_size,
            radius=RADIUS,
            velocity=VELOCITY,
            batch=self.main_batch,
            goal=self.goal,
            obstacles=self.obstacles)

        self.elements = []
        self.set_elements()

    def set_obstacles(self):
        start_point = (WIDTH*3/7, HEIGHT*2/3)
        end_point = (WIDTH*4/7, HEIGHT*2/3)
        obstacle = Obstacle(position=(start_point+end_point), width=3, batch=self.main_batch)
        # obstacle_b = Obstacle(position=(start_point+end_point), width=3, batch=self.main_batch)
        self.obstacles.append(obstacle)
        # self.obstacles.append(obstacle_b)

    def set_elements(self):
        self.elements = [x for x in self.population.generation]
        [self.elements.append(x) for x in self.obstacles]
        self.elements.append(self.goal)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()

    def update(self, dt):
        evolve_elements = False
        self.stats_label.text = 'Generation: ' + str(self.population.generation_count)
        for element in self.elements:
            evolve_elements = len([x for x in self.elements if type(x) == Element and (
                x.dead == True or x.finished == True)]) == len([x for x in self.elements if type(x) == Element])
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
