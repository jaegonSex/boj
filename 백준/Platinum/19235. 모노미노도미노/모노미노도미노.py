from collections import deque
import sys


def rotate_counter_clockwise(arr):
    result = [[0 for i in range(len(arr))] for i in range(len(arr[0]))]

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            result[i][j] = arr[j][len(arr[0]) - 1 - i]
    return result


class Block:
    __slots__ = ['coordinates', 'name']

    def __init__(self, type, x, y, seq):
        self.name = seq
        self.coordinates = set()

        self.coordinates.add((1, y))
        if type == 2:
            self.coordinates.add((1, y + 1))
        elif type == 3:
            self.coordinates.add((0, y))

    def drop(self, area):

        for x, y, in self.coordinates:
            self._demark(area, x, y)
        tmp = 5
        for x, y in self.coordinates:
            for i in range(x, 6):
                if area[i][y] is not None:
                    tmp = min(i - 1, tmp)
                    break

        d = tmp - max(self.coordinates)[0]
        new = set()
        for x, y in self.coordinates:
            new.add((x + d, y))

        self.coordinates = new
        self._mark(area)

    def remove(self, x, area):
        new = set()
        for _x, _y in self.coordinates:
            if _x == x:
                self._demark(area, _x, _y)
            else:
                new.add((_x, _y))
        self.coordinates = new

    def _mark(self, area):
        for x, y in self.coordinates:
            area[x][y] = self

    def _demark(self, area, x, y):

        area[x][y] = None

    def plus_coordinates_x(self, k):
        new = set()
        for x, y in self.coordinates:
            new.add((x + k, y))
        self.coordinates = new

    def __repr__(self):
        return '|' + str(self.name) * 2 + '|'


class Mono:
    __slots__ = ['blue', 'green', 'score', 'red']

    def __init__(self):
        self.red = []
        self.score = 0
        self.blue = deque([[None for i in range(4)] for i in range(6)])
        self.green = deque([[None for i in range(4)] for i in range(6)])

    def new_block_drop(self, type, x, y, seq):
        self.red = [[None for i in range(4)]for i in range(4)]
        self.red[x][y] ='|'+ seq*2 + '|'
        if type==2:
            self.red[x][y+1] = '|'+ seq*2 + '|'
        elif type ==3:
            self.red[x+1][y] = '|'+ seq*2 + '|'


        green_block = Block(type, x, y, seq)
        if type == 1:
            blue_block = Block(type, y, 3 - x, seq)
        elif type == 2:
            blue_block = Block(3, y, 3 - x, seq)
        elif type == 3:
            blue_block = Block(2, y, 3 - x - 1, seq)

        green_block.drop(self.green)
        blue_block.drop(self.blue)

    def print(self):
        print()
        for i in range(len(rotate_counter_clockwise(self.blue))):
            print(*self.red[i], '\t',rotate_counter_clockwise(self.blue)[i])
        print()
        print(*self.green, sep='\n')

    def remain_block(self, area):
        count = 0
        for i in range(6):
            for j in range(4):
                if area[i][j] is not None:
                    count += 1
        return count

    def _check_line(self, x, area):
        for y in range(4):
            if area[x][y] is None:
                return False
        return True

    def _clear_line(self, x, area):
        for y in range(4):
            if area[x][y] is not None:
                block = area[x][y]
                block.remove(x, area)

    def _drop_line(self, x, area):
        for y in range(4):
            if area[x][y] is not None:
                area[x][y].drop(area)

    def scoring(self):
        idx = 5
        while idx >= 2:
            if self._check_line(idx, self.green):
                if self._check_line(idx-1,self.green):
                    self._clear_line(idx,self.green)
                    self.score+=1
                    idx-=1
                self._clear_line(idx, self.green)
                for line in range(idx - 1, -1, -1):
                    self._drop_line(line, self.green)
                self.score += 1
                idx = 5
            else:
                idx -= 1
        idx = 5
        while idx >= 2:
            if self._check_line(idx, self.blue):
                if self._check_line(idx-1,self.blue):
                    self._clear_line(idx,self.blue)
                    self.score+=1
                    idx-=1
                self._clear_line(idx, self.blue)
                for line in range(idx - 1, -1, -1):
                    self._drop_line(line, self.blue)
                self.score += 1
                idx = 5
            else:
                idx -= 1

    def _check_light(self, area):
        count = 0
        for x in range(2):
            for y in range(4):
                if area[x][y] is not None:
                    count += 1
                    break
        return count

    def _get_blocks(self, area):
        blocks = set()
        for x in range(6):
            for y in range(4):
                if area[x][y] is not None:
                    blocks.add(area[x][y])
        return blocks

    def check_light_place(self):
        green_count = self._check_light(self.green)
        blue_count = self._check_light(self.blue)

        for i in range(green_count):
            self.green.pop()
            self.green.appendleft([None for i in range(4)])
        blocks = self._get_blocks(self.green)
        for block in blocks:
            block.plus_coordinates_x(green_count)

        for i in range(blue_count):
            self.blue.pop()
            self.blue.appendleft([None for i in range(4)])
        blocks = self._get_blocks(self.blue)
        for block in blocks:
            block.plus_coordinates_x(blue_count)
        #
        # for i in range(5,-1,-1):
        #
        #     self._drop_line(i,self.blue)
        #     self._drop_line(i,self.green)


mono = Mono()
seq = 65
n = int(input())
for i in range(n):
    # print("*" * 10)
    # print(i + 1, chr(seq))
    t, x, y = map(int, sys.stdin.readline().split())
    # print(t, x, y)

    mono.new_block_drop(t, x, y, chr(seq))
    mono.scoring()
    mono.check_light_place()
    seq += 1

    # mono.print()
print(mono.score)
print(mono.remain_block(mono.green) + mono.remain_block(mono.blue))
