import sys
from collections import deque
import heapq

n, m = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def is_in_map(x, y):
    global n, m
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def check_country(x, y, country):
    queue = deque()
    queue.append((x, y))
    endpoints = set()
    Map[x][y] = country
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            xx, yy = nx + dx[i], ny + dy[i]
            if is_in_map(xx, yy) :
                if Map[xx][yy] == 1:
                    Map[xx][yy] = country
                    queue.append((xx, yy))
                elif Map[xx][yy] == 0:

                    endpoints.add((nx, ny))
    return endpoints


def build_bridge(endpoints, now_country):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = {}
    for dir in range(4):
        queue = deque()
        for x, y in endpoints:
            queue.append((0, x, y))
        visit = [[False for i in range(len(Map[0]))] for i in range(len(Map))]
        while queue:
            w, nx, ny = queue.popleft()

            xx, yy = nx + dx[dir], ny + dy[dir]
            if is_in_map(xx, yy):
                if Map[xx][yy] == 0 and not visit[xx][yy]:
                    queue.append((w + 1, xx, yy))
                    visit[xx][yy] = True
                if Map[xx][yy] != 0 and Map[xx][yy] != now_country:
                    next_country = Map[xx][yy]
                    if next_country not in result:
                        if w>1:
                            result[next_country] = w
                    else:
                        if w>1:
                            result[next_country] = min(result[next_country], w)
    return result
country_name = 2
countries = []
for i in range(n):
    for j in range(m):
        if Map[i][j] == 1:
            ep = check_country(i,j,country_name)
            countries.append((country_name, ep))
            country_name+=1
bridges = []
parents = list(range(country_name))


for c, ep in countries:
    for next_c, dist in build_bridge(ep, c).items():
        bridges.append((dist , c, next_c))
bridges.sort()


cost = 0
done = 0
for dist, start, end in bridges:
    if find(start)!= find(end):
        cost += dist
        union(start, end)
        done+=1
tmp =[]
for i in range(2,len(parents)):
    tmp.append(find(parents[i]))

print(cost if cost != 0 and len(set(tmp))==1 else -1)