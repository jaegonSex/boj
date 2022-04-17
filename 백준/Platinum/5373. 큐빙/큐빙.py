import sys



def rotate_clockwise(arr):
    result = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            result[i][j] = arr[len(arr[0]) - 1 - j][i]
    return result


def rotate_counter_clockwise(arr):
    result = [[0 for i in range(len(arr[0]))] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            result[i][j] = arr[j][len(arr[0]) - 1 - i]
    return result


def change_tb(left, mid, right, back, elem, direction):
    if elem == 'U':
        if direction == '+':
            left[0], mid[0], right[0], back[0] = mid[0], right[0], back[0], left[0]
        else:
            left[0], mid[0], right[0], back[0] = back[0], left[0], mid[0], right[0]

    if elem == 'D':
        if direction == '+':
            left[2], mid[2], right[2], back[2] = back[2], left[2], mid[2], right[2]
        else:
            left[2], mid[2], right[2], back[2] = mid[2], right[2], back[2], left[2]
    return left, mid, right, back


def change_lr(top, front, bottom, back, elem, direction):
    tmptop, tmpfront, tmpbottom, tmpback = list(zip(*top)), list(zip(*front)), list(zip(*bottom)), list(zip(*back))
    if elem == 'L':
        if direction == '+':
            tmptop[0], tmpfront[0], tmpbottom[0], tmpback[2] = tmpback[2][::-1], tmptop[0], tmpfront[0], tmpbottom[0][::-1]

        else:
            tmptop[0], tmpfront[0], tmpbottom[0], tmpback[2] = tmpfront[0], tmpbottom[0], tmpback[2][::-1], tmptop[0][::-1]
    if elem == 'R':
        if direction == '+':
            tmptop[2], tmpfront[2], tmpbottom[2], tmpback[0] = tmpfront[2], tmpbottom[2], tmpback[0][::-1], tmptop[2][::-1]
        else:
            tmptop[2], tmpfront[2], tmpbottom[2], tmpback[0] = tmpback[0][::-1], tmptop[2], tmpfront[2], tmpbottom[2][::-1]

    return list(zip(*tmptop)), list(zip(*tmpfront)), list(zip(*tmpbottom)), list(zip(*tmpback))


def change_fb(top, left, bottom, right, elem, direction):
    tmpleft, tmpright = list(zip(*left)), list(zip(*right))
    if elem == 'F':
        if direction == '+':
            top[2], tmpleft[2], bottom[0], tmpright[0] = tmpleft[2][::-1], bottom[0], tmpright[0][::-1], top[2]
        else:
            top[2], tmpleft[2], bottom[0], tmpright[0] = tmpright[0], top[2][::-1], tmpleft[2], bottom[0][::-1]
    if elem == 'B':
        if direction == '+':
            top[0], tmpleft[0], bottom[2], tmpright[2] = tmpright[2], top[0][::-1], tmpleft[0], bottom[2][::-1]

        else:
            top[0], tmpleft[0], bottom[2], tmpright[2] = tmpleft[0][::-1], bottom[2], tmpright[2][::-1], top[0]

    return top, list(zip(*tmpleft)), bottom, list(zip(*tmpright))


class Cube():
    __slots__ = ['top', 'left', 'front', 'right', 'back', 'bottom']

    def __init__(self, top, left, front, right, back, bottom):
        self.top = top
        self.left = left
        self.front = front
        self.right = right
        self.back = back
        self.bottom = bottom

    def rotate(self, element, direction):
        if element == 'U':
            if direction == '+':
                self.top = rotate_clockwise(self.top)
            else:
                self.top = rotate_counter_clockwise(self.top)
            self.left, self.front, self.right, self.back = change_tb(self.left, self.front, self.right, self.back,
                                                                     element, direction)
        elif element == 'D':
            if direction == '+':
                self.bottom = rotate_clockwise(self.bottom)
            else:
                self.bottom = rotate_counter_clockwise(self.bottom)
            self.left, self.front, self.right, self.back = change_tb(self.left, self.front, self.right, self.back,
                                                                     element, direction)

        elif element == 'L':
            if direction == '+':
                self.left = rotate_clockwise(self.left)
            else:
                self.left = rotate_counter_clockwise(self.left)

            self.top, self.front, self.bottom, self.back = change_lr(self.top, self.front, self.bottom, self.back,
                                                                     element, direction)

        elif element == 'R':
            if direction == '+':
                self.right = rotate_clockwise(self.right)
            else:
                self.right = rotate_counter_clockwise(self.right)
            self.top, self.front, self.bottom, self.back = change_lr(self.top, self.front, self.bottom, self.back,
                                                                     element, direction)

        elif element == 'F':
            if direction == '+':
                self.front = rotate_clockwise(self.front)
            else:
                self.front = rotate_counter_clockwise(self.front)

            self.top, self.left, self.bottom, self.right = change_fb(self.top, self.left, self.bottom, self.right,
                                                                     element, direction)

        elif element == 'B':
            if direction == '+':
                self.back = rotate_clockwise(self.back)
            else:
                self.back = rotate_counter_clockwise(self.back)
            self.top, self.left, self.bottom, self.right = change_fb(self.top, self.left, self.bottom, self.right,
                                                                     element, direction)

    def print(self):
        for i in self.top:
            print(''.join(i))
        # print()
        # print(*self.top, sep='\n')
        # print(self.left[0], self.front[0], self.right[0], self.back[0])
        # print(self.left[1], self.front[1], self.right[1], self.back[1])
        # print(self.left[2], self.front[2], self.right[2], self.back[2])
        # print(*self.bottom, sep='\n')





tc = int(sys.stdin.readline().rstrip())
for i in range(tc):
    top = [['w' for i in range(3)] for i in range(3)]
    left = [['g' for i in range(3)] for i in range(3)]
    front = [['r' for i in range(3)] for i in range(3)]
    right = [['b' for i in range(3)] for i in range(3)]
    back = [['o' for i in range(3)] for i in range(3)]
    bottom = [['y' for i in range(3)] for i in range(3)]
    cube = Cube(top, left, front, right, back, bottom)

    n = int(sys.stdin.readline().rstrip())
    commands = sys.stdin.readline().split()
    for command in commands:
        elem, direction = command[0], command[1]
        cube.rotate(elem, direction)

    cube.print()
