import sys


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        x3, y3, x4, y4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

        if x1 <= x4 and x3 <= x2 and y1 <= y4 and y3 <= y2:
            return True

    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            return True

    return False


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
print(1 if is_cross(x1, y1, x2, y2, x3, y3, x4, y4) else 0)
