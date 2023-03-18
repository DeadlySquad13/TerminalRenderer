# Triangle contains point if point is inside or outside all of the half panes
# (each side of the triangle divides plane into two parts).
#
# Reference: https://www.cyberforum.ru/algorithms/thread144722.html
def triangle_contains_point(x, y, point1, point2, point3):
    half_pane1 = (point1[0] - x) * (point2[1] - point1[1]) - (point2[0] - point1[0]) * (point1[1] - y)
    half_pane2 = (point2[0] - x) * (point3[1] - point2[1]) - (point3[0] - point2[0]) * (point2[1] - y)
    half_pane3 = (point3[0] - x) * (point1[1] - point3[1]) - (point1[0] - point3[0]) * (point3[1] - y)

    #   If some of the half_panes equals to 0, then point is inside
    # corresponding border of the triangle. We assume that triangle contains
    # it in this case.
    return half_pane1 >= 0 and half_pane2 >= 0 and half_pane3 >= 0 or \
        half_pane1 <= 0 and half_pane2 <= 0 and half_pane3 <= 0

class Polygon():
    def __init__(self, points, angle):
        self.points = points
        self.angle = angle

    def contain(self, x, y):
        contains = False

        for i in range(0, len(self.points) - 2):
            contains = triangle_contains_point(x, y, self.points[i], self.points[i+1], self.points[i+2])

            if contains:
                break

        return contains

def main_triangle():
    polygon = Polygon([(0, 0), (10, 0), (10, 10)], 0)

    print(polygon.contain(10, 0))
    print(polygon.contain(11, 0))

def main_polygon():
    polygon = Polygon([(0, 0), (10, 0), (10, 10), (5, 15), (0, 10)], 0)

    print(polygon.contain(10, 0))
    print(polygon.contain(11, 0))
    print(polygon.contain(5, 10))

if __name__ == "__main__":
    main_polygon()
