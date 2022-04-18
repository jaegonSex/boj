import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    graph.append(sys.stdin.readline().rstrip())
r,b,g=0,0,0;
for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            r=(i,j)
        if graph[i][j]=='B':
            b=(i,j)
        if graph[i][j]=='O':
            g=(i,j)
coordinate=[r,b]
def move(num,coordinate):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    xr,yr=coordinate[0]
    xb,yb=coordinate[1]
    cntr,cntb=0,0
    while(True):
        xr,yr,cntr=xr+dx[num],yr+dy[num],cntr+1
        if graph[xr][yr]=='O':
            break
        if graph[xr][yr]=='#':
            xr,yr=xr-dx[num],yr-dy[num]
            break
    while(True):
        xb,yb,cntb=xb+dx[num],yb+dy[num],cntb+1
        if graph[xb][yb]=='O':
            break
        if graph[xb][yb]=='#':
            xb,yb=xb-dx[num],yb-dy[num]
            break
    if (xr,yr)==(xb,yb) and graph[xr][yr]!='O':
        if cntr>cntb:
            xr,yr=xr-dx[num],yr-dy[num]
        else:
            xb,yb=xb-dx[num],yb-dy[num]
    return [(xr,yr),(xb,yb)]
queue=deque()
queue.append((coordinate,0))
visit={}
visit[tuple(coordinate)]=True
result=False
while queue:
    tmp,dep=queue.popleft()
    if dep>10:
        break
    if tmp[0]==g:
        result=True
        break
    for i in range(4):
        go=tuple(move(i,tmp))
        if go not in visit and go[1]!=g:
            queue.append((move(i,tmp),dep+1))
            visit[tuple(move(i,tmp))]=True
print(1 if result else 0)
