n, m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]


def find_air(graph):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n, m = len(graph), len(graph[0])
    outer = [[False for i in range(m)] for i in range(n)]
    s = [(0,0)]
    while s:
        x, y = s.pop()
        for i in range(4):
            xx, yy= x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<m and not outer[xx][yy]:
                if graph[xx][yy] == 0:
                    s.append((xx,yy))
                    outer[xx][yy] = True
    return outer

def melt(outer):
    result = 0
    n, m = len(graph), len(graph[0])
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j]== 1:
                count = sum([1 for k in [outer[i][j-1],outer[i-1][j],outer[i][j+1],outer[i+1][j]] if k])
                if count>=2:
                    graph[i][j] = 0
                    result +=1
    return result

time = 0
totalcount = sum(map(lambda x:sum(x),graph))
while totalcount !=0:
    outer = find_air(graph)
    totalcount -= melt(outer)
    time+=1

print(time)
