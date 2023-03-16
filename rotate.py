import math

def rotate(point, origin, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

if __name__ == "__main__":
    point = (2, 1)
    origin = (1, 1)
    print(rotate(point, origin, math.pi)) # Must be (0, 1)
    exit()
