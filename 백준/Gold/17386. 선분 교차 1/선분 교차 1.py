import sys


def ccw(x1, y1, x2, y2, x3, y3):
    if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) > 0:
        return 1
    elif (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
        return 0
    else:
        return -1


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4):
        if ccw(x3, y3, x4, y4, x1, y1) != ccw(x3, y3, x4, y4, x2, y2):
            return True

    if ccw(x1, y1, x2, y2, x3, y3) == 0:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y2
        if x3 > x4:
            x3, y3, x4, y4 = x4, y4, x3, y3
        if x1 <= x4 and x3 <= x2:
            return True
    return False


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
print(1 if is_cross(x1, y1, x2, y2, x3, y3, x4, y4) else 0)
