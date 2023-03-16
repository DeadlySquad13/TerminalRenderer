import time
from os import system

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
                    if f.contain(cx, cy):
                        matrix[i][j] = '# '
                        break

        return matrix

class Shape:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

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

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

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

    def contain(self, x, y):
        return (self.left <= x < self.right) and \
               (self.top <= y < self.bottom)

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def contain(self, x, y):
        return ((x - self._x) ** 2 / (self._width / 2) ** 2 +
                (y - self._y) ** 2 / (self._height / 2) ** 2) <= 1

class MovingObject:
    def __init__(self, x, y, v, g=None):
        self._y = y
        self._x = x
        self._vx = v
        self._vy = 0
        self._g = g

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def recalc(self, dt):
        self._x += self._vx * dt
        vy = self._vy
        self._vy += self._g * dt
        self._y += (self._vy / 2 + vy) * dt

        if self._y >= 11:
            self._y = 10
            self._vy = -self._vy * 0.7


scene = Scene()
r = Rectangle(7, 3, 1, 1)
scene.add_figures(r)
# scene.add_figures(Rectangle(2.5, 4.2, 1, 2))
e = Ellipse(5, 2, 3, 2)
scene.add_figures(e)
mo1 = MovingObject(7, 3, 0.5, 9.8)
mo2 = MovingObject(5, 5, 0.5, 9.81)
while True:
    m = scene.render(0, 0, 20, 12, 60, 100)
    sc = '\n'.join(''.join(line) for line in m)
    print(sc)
    time.sleep(0.05)
    mo1.recalc(0.05)
    r.x = mo1.x
    r.y = mo1.y
    mo2.recalc(0.01)
    e.x = mo2.x
    e.y = mo2.y

