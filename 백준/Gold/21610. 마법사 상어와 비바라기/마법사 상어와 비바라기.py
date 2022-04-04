N, M = map(int,input().split())
graph = [list(map(int,input().split()))for i in range(N)]

def checkmap(x,y):
    N=len(graph)
    if 0<= x <N and 0<=y <N:
        return True
    return False
def move_cloud(di, si , cloud):
    N=len(graph)
    dx=[0,0,-1,-1,-1,0,1,1,1]
    dy=[0,-1,-1,0,1,1,1,0,-1]
    new_cloud = set()
    for xy in cloud:
        x, y =xy
        new_cloud.add(((x + dx[di]*si)%N , (y + dy[di]*si)%N))
    return new_cloud
def rain_drop(cloud):
    for xy in cloud:
        x,y = xy
        graph[x][y]+=1
def mulboksa(cloud):
    N=len(graph)
    dx=[-1,-1,1,1]
    dy=[-1,1,-1,1]
    table={}
    for xy in cloud:
        x,y =xy
        count = 0
        for i in range(4):
            _x, _y = x+dx[i], y+dy[i]
            if checkmap(_x,_y) and graph[_x][_y] > 0:
                count+=1
        table[(x,y)] = count
    for _xy in table:
        tx,ty = _xy
        amount = table[_xy]
        graph[tx][ty] += amount
def make_new_cloud(cloud):
    N= len(graph)
    new_cloud= set()
    for x in range(N):
        for y in range(N):
            if (x,y) not in cloud and graph[x][y]>=2:
                new_cloud.add((x,y))
                graph[x][y]-=2
    return new_cloud

cloud =set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for i in range(M):
    di, si = map(int,input().split())
    cloud = move_cloud(di,si,cloud)
    rain_drop(cloud)
    mulboksa(cloud)
    cloud = make_new_cloud(cloud)

print(sum(map(lambda x:sum(x),graph)))
