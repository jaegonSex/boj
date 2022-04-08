import sys
n, m = map(int,sys.stdin.readline().split())
g = [[0]* (n + 1)] +  [[0] +list(map(int,input().split()))for i in range(n)]



for i in range(n+1):
    for j in range(1,n+1):
        g[i][j]= g[i][j-1] +g[i][j]

for i in range(1,n+1):
    for j in range(n+1):
        g[i][j]= g[i-1][j]  +g[i][j]



for i in range(m):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    print(g[x2][y2] + g[x1-1][y1-1] - g[x1-1][y2] -g[x2][y1-1])
