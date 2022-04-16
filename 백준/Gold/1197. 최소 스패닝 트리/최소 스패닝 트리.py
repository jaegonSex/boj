import sys
import heapq


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


v, e = map(int, sys.stdin.readline().split())

parent = [i for i in range(v + 1)]

edges = []

parents = list(range(v + 1))

for edge in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))
edges.sort()
result = 0
for c,a,b in edges:
    if find(a)!= find(b):
        union(a,b)
        result+=c
print(result)
