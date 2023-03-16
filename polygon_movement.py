import time
from os import system
import math

from rotate import rotate

class Scene:
    def __init__(self):
        self._figures = []

    def add_figures(self, figure):
        self._figures.append(figure)

    def render(self, x, y, width, height, m, n):

        matrix = [['  ' for _ in range(n)] for _ in range(m)]

        dx = width / n
        dy = height / m

        for i in range(n):
            for j in range(m):
                cx = x + j * dx
                cy = y + i * dy

                for f in self._figures:
                    cx_rotated, cy_rotated = rotate((cx, cy), f.center, f.angle)

                    if f.contain(cx_rotated, cy_rotated):
                        matrix[i][j] = '# '
                        break

        return matrix

class Shape:
    def __init__(self, x, y, width, height, angle):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._angle = angle

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def angle(self):
        return self._angle

    @y.setter
    def angle(self, value):
        self._angle = value


class Rectangle(Shape):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)

    @property
    def left(self):
        return self._x

    @property
    def right(self):
        return self._x + self._width

    @property
    def top(self):
        return self._y

    @property
    def bottom(self):
        return self._y + self._height

    @property
    def center(self):
        center_x = self._x + self._width / 2
        center_y = self._y + self._height / 2

        return (center_x, center_y) 

    def contain(self, x, y):
        return (self.left <= x < self.right) and \
               (self.top <= y < self.bottom)

class Ellipse(Shape):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)

    def contain(self, x, y):
        return ((x - self._x) ** 2 / (self._width / 2) ** 2 +
                (y - self._y) ** 2 / (self._height / 2) ** 2) <= 1

ROTATION_VELOCITY = math.pi

class MovingObject:
    def __init__(self, x, y, angle, v, g=None, rotation_velocity=ROTATION_VELOCITY):
        self._y = y
        self._x = x
        self._vx = v
        self._vy = 0
        self._g = g

        self._angle = angle
        self._rotation_velocity = rotation_velocity

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def angle(self):
        return self._angle


    def recalc(self, dt):
        """
        Update motion characteristics of moving object.
        """
        self._x += self._vx * dt
        vy = self._vy
        self._vy += self._g * dt
        self._y += (self._vy / 2 + vy) * dt

        self._angle += self._rotation_velocity * dt

        if self._y >= 11:
            self._y = 10
            self._vy = -self._vy * 0.7


scene = Scene()
r = Rectangle(7, 3, 1, 1, 0)
scene.add_figures(r)
# scene.add_figures(Rectangle(2.5, 4.2, 1, 2, 0))
# e = Ellipse(5, 2, 3, 2, 0)
# scene.add_figures(e)

mo1 = MovingObject(7, 3, 0, 0.5, 9.806)
# mo2 = MovingObject(5, 5, 0.5, 9.806)

while True:
    m = scene.render(0, 0, 20, 12, 60, 100)
    sc = '\n'.join(''.join(line) for line in m)
    print(sc)
    time.sleep(0.05)
    mo1.recalc(0.05)
    r.x = mo1.x
    r.y = mo1.y
    r.angle = mo1.angle
    # mo2.recalc(0.01)
    # e.x = mo2.x
    # e.y = mo2.y

