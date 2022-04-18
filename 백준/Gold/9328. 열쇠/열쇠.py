from collections import deque
import sys


def steal(graph, start_points, keys, visit):

    tmp = len(keys)

    for x,y in start_points:
        visit[x][y] = True
    h, w = len(graph), len(graph[0])
    queue = deque(start_points)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    doors = []
    count = 0
    while queue:
        x, y = queue.popleft()
        if graph[x][y].isupper():
            if not can_open(keys,graph[x][y]):
                doors.append((x,y))
                continue

        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]

            if 0 <= xx < h and 0 <= yy < w and not visit[xx][yy]:

                if graph[xx][yy] == '.':
                    queue.append((xx, yy))
                    visit[xx][yy] = True

                elif graph[xx][yy] == '$':
                    count += 1
                    visit[xx][yy] = True
                    queue.append((xx, yy))

                elif graph[xx][yy].isupper():
                    if can_open(keys,graph[xx][yy]):
                        queue.append((xx,yy))
                        visit[xx][yy] = True
                    else:
                        doors.append((xx, yy))

                elif graph[xx][yy].islower():
                    keys.add(graph[xx][yy])
                    queue.append((xx, yy))
                    visit[xx][yy] = True
    if tmp != len(keys):
        count+=steal(graph,doors,keys, visit)

    return count


def can_open(keys, door):
    if door.lower() in keys:
        return True
    return False


def get_start_points(graph):
    h, w = len(graph), len(graph[0])
    start = []
    for i in range(h):
        start.append((i, 0))
        start.append((i, w - 1))
    for i in range(w):
        start.append((0, i))
        start.append((h - 1, i))
    return start


tc = int(sys.stdin.readline().rstrip())
for test_case in range(tc):
    h, w = map(int, sys.stdin.readline().split())
    graph = [['.']*(w+2)] +[['.'] + list(sys.stdin.readline().rstrip())+ ['.'] for i in range(h)]+[['.']*(w+2)]
    keys = set(list(sys.stdin.readline().rstrip()))
    visit = [[False for i in range(w+2)] for i in range(h+2)]
    start_points = get_start_points(graph)


    print(steal(graph, start_points, keys, visit))

