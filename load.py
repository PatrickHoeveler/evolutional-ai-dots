from dot import Dot
from typing import Tuple


def load_dots(win_size: Tuple, radius: float, speed: Tuple, batch=None):
    dots = []
    goal_x = win_size[0]/2
    goal_y = win_size[1]-win_size[1]*0.1

    dot_x = win_size[0]/2
    dot_y = win_size[1]/2

    goal = Dot(x=goal_x, y=goal_y, radius=radius*2, color=(255, 0, 0),
                         batch=batch, win_size=win_size, brain_size=0)

    dot = Dot(x=dot_x, y=dot_y, radius=radius,
                         batch=batch, win_size=win_size, brain_size=400, goal_pos=goal.position)

    dot2 = Dot(x=dot_x, y=dot_y, radius=radius, color=(0, 255, 0),
                         batch=batch, win_size=win_size, brain_size=400, goal_pos=goal.position)
    dot.velocity_x, dot.velocity_y = speed[0], speed[1]
    dots.append(goal)
    dots.append(dot)
    dots.append(dot2)
    return dots
