from turtle import pos
import numpy as np
import pyglet
from pyglet import shapes
from dot import Dot
from population import Population

# Variables, Considering a vertical oriented window for game
WIDTH = 600   # Game Window Width
HEIGHT = 600  # Game Window Height
BORDER = 10   # Walls Thickness/Border Thickness
RADIUS = 3
POPULATION_SIZE = 10
BRAIN_SIZE = 100

# goal = shapes.Circle(WIDTH/2, HEIGHT/2+HEIGHT/2.5, 10, color=(255, 0, 0), batch=batch)
# square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=batch)
# rectangle = shapes.Rectangle(250, 300, 400, 200, color=(255, 22, 20), batch=batch)
# rectangle.opacity = 128
# rectangle.rotation = 33
# line = shapes.Line(100, 100, 100, 200, width=19, batch=batch)
# line2 = shapes.Line(150, 150, 444, 111, width=4, color=(200, 20, 20), batch=batch)
# star = shapes.Star(800, 400, 60, 40, num_spikes=20, color=(255, 255, 0), batch=batch)


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.win_size = (WIDTH, HEIGHT)
        self.main_batch = pyglet.graphics.Batch()
        # self.dots = load.load_dots(self.win_size, RADIUS, speed=dotspeed, batch=self.main_batch)
        self.population = Population(
            size=POPULATION_SIZE,
            brain_size=BRAIN_SIZE,
            win_size=self.win_size,
            radius=RADIUS,
            batch=self.main_batch)

    def on_draw(self):
        self.clear()
        self.main_batch.draw()

def update(dt):
    global game_objects, game_window
    print('len(game_objects)', len(game_objects))
    finished_dead_counter = 0


    for dot in game_objects:
        if(type(dot)== Dot):
            # print('dot.finished', dot.finished, 'dot.dead', dot.dead)
            if dot.finished or dot.dead:
                finished_dead_counter += 1
            else:
                dot.move()

    print('finished_dead_counter', finished_dead_counter, 'POPULATION_SIZE', POPULATION_SIZE)
    if(finished_dead_counter == POPULATION_SIZE):
        # print('update_population')
        game_window.population.update()
        game_objects = game_window.population.generation





if __name__ == '__main__':
    game_window = Window(width=WIDTH, height=HEIGHT, caption='Evolutional AI')
    pyglet.gl.glClearColor(1, 1, 1, 1)
    game_objects = game_window.population.generation

    pyglet.clock.schedule_interval(update, 1/300.0)
    pyglet.app.run()
