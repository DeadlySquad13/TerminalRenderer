import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import itertools
import random

import math

class Coord:
    def __init__(self, dx, dy, angle, parent=None):
        self._dx = dx
        self._dy = dy
        self._a = angle
        self._parent = parent

    def map_to_parent(self, x, y):
        return (math.cos(self._a) * x - math.sin(self._a) * y + self._dx,
                math.sin(self._a) * x + math.cos(self._a) * y + self._dy)

    def map_abs(self, x, y):
        if self._parent:
            return self._parent.map_abs(*self.map_to_parent(x, y))
        else:
            return self.map_to_parent(x, y)


class Rect:
    def __init__(self, x, y, w, h, coord=None):
        self._x, self._y, self._w, self._h = x, y, w, h
        self._coord = coord

    def points(self):
        if self._coord:
            return list(
                itertools.starmap(
                    self._coord.map_abs,
                    rect_coords(self._x, self._y, self._w, self._h)
                )
            )
        else:
            return rect_coords(self._x, self._y, self._w, self._h)

class Polygon:
    def __init__(self, x, y, r, n, coord=None):
        self._x = x
        self._y = y
        self._r = r
        self._n = n
        self._coord = coord

    def points(self):
        if self._coord:
            return list(
                itertools.starmap(
                    self._coord.map_abs,
                    polygon_coords(self._x, self._y, self._r, self._n)
                )
            )
        else:
            return polygon_coords(self._x, self._y, self._r, self._n)

    def render(self):
        return None

class Scene:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set(self):
        return '################'

def polygon_coords(x, y, r, n):
    return [(x + r * math.sin(2 * math.pi * i / n), y + r * math.cos(2 * math.pi * i / n)) for i in range(1, n + 2)]

def rect_coords(x, y, w, h):
    return [(x, y),
            (x, y + h),
            (x + w, y + h),
            (x + w, y),
            (x, y)]

def draw_lines(points):
    plt.plot(*zip(*points))

def main_3():
    plt.axis([-20, 20, -20, 20])

    c1 = Coord(10, 10, math.pi / 2)
    c2 = Coord(0, 0, math.pi / 3, c1)
    c3 = Coord(-5, -5, math.pi / 4, c2)

    r1 = Rect(2, 2, 5, 10)
    r2 = Rect(2, 3, 4, 5, c2)
    r3 = Rect(0, 2, 3, 4, c3)

    draw_lines(r1.points())
    draw_lines(r2.points())
    draw_lines(r3.points())

    plt.show()

def main_render_scene():
    scene = Scene(1, 2)

    print(scene.set())


if __name__ == "__main__":
    main_render_scene()
    exit()
