import sys
from collections import deque


class Space:
    def __init__(self, num):
        self.count = num


n, m = map(int, sys.stdin.readline().split())
Map = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(n)]
area = [[Space(0) for i in range(m)] for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
for i in range(n):
    for j in range(m):

        if Map[i][j] == 0 and area[i][j].count == 0:
            area[i][j].count = 1
            queue.append((i, j))
            tmp = 0
            while queue:
                now_x, now_y = queue.popleft()
                for t in range(4):
                    next_x, next_y = now_x + dx[t], now_y + dy[t]
                    if 0 <= next_x < n and 0 <= next_y < m:
                        if area[next_x][next_y].count == 0 and Map[next_x][next_y] == 0:
                            area[next_x][next_y] = area[i][j]
                            queue.append((next_x,next_y))
                            tmp += 1

            area[i][j].count += tmp

for i in range(n):
    for j in range(m):
        if Map[i][j] == 0:
            print(0, end='')
        else:
            tmp = set()
            for t in range(4):
                next_x, next_y = i + dx[t], j + dy[t]
                if 0 <= next_x < n and 0 <= next_y < m:
                    tmp.add(area[next_x][next_y])
            c = 1
            for t in tmp:
                c += t.count
            print(c % 10, end='')
    print()
