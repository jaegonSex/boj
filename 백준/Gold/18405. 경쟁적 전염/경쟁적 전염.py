import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
S, X, Y = map(int,sys.stdin.readline().split())
coorditates = {i + 1: [] for i in range(k)}
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            coorditates[graph[i][j]].append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
for i in range(1, k + 1):
    if i in coorditates:
        for co in coorditates[i]:
            queue.append((i, co[0], co[1], 0))

while queue:
    virus, x, y, time = queue.popleft()
    if time>=S:
        break

    for i in range(4):
        xx,yy= x+dx[i] , y+dy[i]

        if 0<=xx<n and 0<=yy<n and graph[xx][yy] == 0:
            graph[xx][yy] = virus
            queue.append((virus,xx,yy,time+1))


print(graph[X-1][Y-1])