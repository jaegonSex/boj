import heapq
import math
n =int(input())
m =int(input())
graph = {i:{} for i in range(1,n+1)}

for i in range(m):
    s, e, w = map(int,input().split())
    if e in graph[s]:
        graph[s][e] = min(graph[s][e] ,w)
    else:
        graph[s][e] = w


start, end = map(int,input().split())
parent = [0 for i in range(n+1)]
dist = [math.inf for i in range(n+1)]
dist[start] = 0
queue= [(0, start)]
while queue:
    w , now = heapq.heappop(queue)
    for next, dw in graph[now].items():
        if dist[next] > dist[now] + dw:
            dist[next] = dist[now] + dw
            parent[next] = now
            heapq.heappush(queue, (dist[next],next))

result = [end]
p = parent[end]

while True:
    result.append(p)
    p = parent[p]
    if p==0:
        break
print(dist[end])
print(len(result))
print(*result[::-1])
