import itertools
import math
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]

chik = []
jib = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            jib.append((i,j))
        if graph[i][j] ==2:
            chik.append((i,j))
    
def get_dist(jibx, jiby , chickenjibs):
    result = math.inf
    for cx, cy in chickenjibs:
        result = min(result, abs(jibx-cx) + abs(jiby -cy))
    return result

result = math.inf
for chickenjibs in itertools.combinations(chik, m):
    count = 0
    for x, y in jib:
        count += get_dist(x,y, chickenjibs)
    result = min(result , count)

print(result)
