import math
import sys

def floyd_warshall(graph):
    n = len(graph) - 1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    return graph


def get_time(graph, edges, v):
    n = len(graph) - 1
    start_time = graph[v]
    result = 0
    for s, e, l in edges:
        time = min(start_time[s], start_time[e]) + l
        if l > abs(start_time[e] - start_time[s]):
            time -= (l - abs(start_time[e] - start_time[s])) / 2
        result = max(result, time)
    return result


n, m = map(int, sys.stdin.readline().split())
edges = []
c = [[math.inf for i in range(n + 1)] for i in range(n + 1)]


for i in range(m):
    s, e, l = map(int, sys.stdin.readline().split())
    c[s][e] = min(c[s][e], l)
    c[e][s] = min(c[e][s], l)
    edges.append((s, e, l))
for i in range(1, n + 1):
    c[i][i] = 0

graph = floyd_warshall(c)
result = math.inf
for i in range(1, n + 1):
    result = min(result, get_time(graph, edges, i))
print(f"{result:.1f}")
