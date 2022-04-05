from collections import deque
import math

N = int(input())
graph = [list(input())for i in range(N)]
sx,sy = 0,0
ex,ey = 0,0
tmp = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == '#':
            if tmp:
                ex,ey=i,j
            else:
                sx,sy = i, j
            tmp +=1
def bfs(x, y, dir):
    global N
    result = math.inf
    dx = [0, 1, 0, -1] #오른 아래 왼 위
    dy = [1, 0, -1, 0]
    queue = deque()
    queue.append((x,y,dir,0))
    while queue:
        nx, ny, ndir, ncount = queue.popleft()
        xx, yy= nx + dx[ndir], ny+ dy[ndir]
        if graph[nx][ny] == '#':
            if nx!= x or ny!=y:
                result = ncount
        if 0<=xx< N and 0<=yy<N and ncount<result:
            if graph[xx][yy] =='.' or graph[xx][yy] =='#':
                queue.appendleft((xx,yy,ndir,ncount))
            if graph[xx][yy] =='!':
                queue.appendleft((xx,yy,ndir,ncount))
                queue.append((xx,yy,(ndir+1)%4, ncount +1))
                queue.append((xx,yy,(ndir+3)%4, ncount +1))
    return result
result = math.inf
for i in range(4):
    result = min(bfs(sx, sy, i),result)
print(result)
