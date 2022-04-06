n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))

def isOdd(num):
    if num%2==0:
        return False
    return True

def change(g):
    c1=0
    c2=0
    for i in range(8):
        for j in range(8):

            if isOdd(i+j):
                if g[i][j]!='W':
                    c1+=1
                else:
                    c2+=1
            else:
                if g[i][j]!='B':
                    c1+=1
                else:
                    c2+=1
    return min(c1,c2)

def newg(x,y):
    g=[[0 for i in range(8)]for i in range(8)]
    for i in range(8):
        for j in range(8):
            g[i][j]=graph[x+i][y+j]
    return g
r=[]
for i in range(n-7):
    for j in range(m-7):
        r.append(newg(i,j))
print(min([change(i) for i in r]))
