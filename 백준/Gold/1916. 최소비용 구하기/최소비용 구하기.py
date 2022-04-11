import sys
import math
import heapq

N = int(input())
M = int(input())

g = {i+1:[] for i in range(N)}

for i in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    g[s].append((e , w))

start, end = map(int, sys.stdin.readline().split())

cost = {i + 1: math.inf for i in range(N)}

cost[start] = 0
queue = [(0, start)]

while queue:
    now_cost, now_node = heapq.heappop(queue)
    if now_node == end :
        break
    for next_node , next_cost in g[now_node]:
        if cost[next_node] > now_cost + next_cost:
            cost[next_node] = now_cost + next_cost
            heapq.heappush(queue, (cost[next_node], next_node))


print(cost[end])