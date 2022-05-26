from turtle import pos
import numpy as np
import pyglet
from pyglet import shapes
import load

# Variables, Considering a vertical oriented window for game
WIDTH = 1200   # Game Window Width
HEIGHT = 800  # Game Window Height
BORDER = 10   # Walls Thickness/Border Thickness
RADIUS = 3
dotspeed = (-2, -2)

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
        self.dots = load.load_dots(self.win_size, RADIUS, speed=dotspeed, batch=self.main_batch)
        
    def on_draw(self):
        self.clear()
        self.main_batch.draw()




game_window = Window(width=WIDTH, height=HEIGHT, caption='Evolutional AI')
pyglet.gl.glClearColor(1,1,1,1)
game_objects = game_window.dots



def update(dt):
    global game_objects, game_window

    for obj in game_objects:
        obj.update()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()