n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
def checkmap(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    return True

maxval=0
visited=[[False for i in range(m)]for i in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,cnt,val):
    global maxval
    if cnt==3:
        maxval=max(val,maxval)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if checkmap(nx,ny) and not visited[nx][ny]:
            visited[nx][ny]=True
            dfs(nx,ny,cnt+1,val+graph[nx][ny])
            visited[nx][ny]=False

def fuck(x,y,val):
    global maxval
    for i in range(4):
        tmp=0
        for j in range(4):
            if i==j:
                continue
            nx,ny=x+dx[j],y+dy[j]
            if not checkmap(nx,ny):
                break
            tmp+=graph[nx][ny]
        maxval=max(maxval,tmp+val)

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j,0,graph[i][j])
        fuck(i,j,graph[i][j])
        visited[i][j]=False
print(maxval)
