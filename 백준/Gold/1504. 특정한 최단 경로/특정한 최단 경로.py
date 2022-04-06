import heapq 
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))  # 양방향 그래프, 둘다 추가
    graph[v].append((u,w))
v1 , v2 = map(int, input().split())
q = []


def dijkstra(start, end):
    distance = [INF]*(n+1)
    
    distance[start] = 0
    
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance[end]

path1 = dijkstra(1,  v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1,  v2) + dijkstra(v2, v1) + dijkstra(v1, n)

total = min(path1, path2)


if total >= INF : 
    print(-1)
else : print(total)