import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
b = [list(map(int, sys.stdin.readline().split())) for i in range(m)]
boomed = [0 for i in range(4)]


def check(x, y):
    global n
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
g = [[None for i in range(n)] for i in range(n)]
x, y = 0, 0
dir = 0
seq = deque()
for i in range(n * n):
    seq.appendleft((x, y))
    if not check(x + dx[dir], y + dy[dir]) or (
            check(x + dx[dir], y + dy[dir]) and g[x + dx[dir]][y + dy[dir]] is not None):
        dir = (dir + 1) % 4
    g[x][y] = dir
    x, y = x + dx[dir], y + dy[dir]


def blizard(dir, l):
    global n
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for i in range(l):
        Map[n // 2 + dx[dir] * (i + 1)][n // 2 + dy[dir] * (i + 1)] = 0


def get_balls():
    balls = deque()
    for i in range(1, n * n):
        x, y = seq[i]

        if Map[x][y] != 0:
            balls.append(Map[x][y])
    return balls


def _destroy(_balls):
    flag = len(_balls)
    find = deque()
    tmp = deque()
    while _balls:
        find.append(_balls.popleft())
        if len(find) >= 4:
            if len(set(find)) == 1:
                if not _balls or(_balls and find[0] != _balls[0]):
                    boomed[find[0]] += len(find)
                    find.clear()
            else:
                tmp.append(find.popleft())

    while find:
        tmp.append(find.popleft())
    if len(tmp) == flag:
        return False,tmp
    return True,tmp


def destroy_balls(balls):
    t = balls

    while True:
        flag, t = _destroy(t)

        if not flag:
            break
    return t

def refresh(balls):
    global n
    tmp = deque()
    find = deque()
    while balls:
        if not find:
            find.append(balls.popleft())
        else:
            if find[-1] != balls[0]:
                tmp.append(len(find))
                tmp.append(find[-1])

                find.clear()
            elif find[-1] == balls[0]:
                find.append(balls.popleft())
    if find:
        tmp.append(len(find))
        tmp.append(find[-1])
        find.clear()
    for i in range(1, n * n):
        x, y = seq[i]
        if tmp:
            Map[x][y] = tmp.popleft()
        else:
            Map[x][y] = 0


for dir, l in b:
    blizard(dir, l)
    balls = get_balls()

    balls = destroy_balls(balls)

    refresh(balls)

print(1 * boomed[1] + 2 * boomed[2] + 3 * boomed[3])