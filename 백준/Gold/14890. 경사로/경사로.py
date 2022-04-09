n,l= map(int,input().split())
g=[list(map(int,input().split())) for i in range(n)]
def i(x):
    c=[1]+[0 for i in range(n-1)]
    for i in range(1,n):
        if abs(x[i]-x[i-1])>=2:
            return False
        elif x[i]==x[i-1]:
            c[i]=c[i-1]+1
        elif x[i-1]<x[i]:
            c[i]=1
            if c[i-1]<l:
                return False
        else:
            c[i]=1-l
            if c[i-1]<0:
                return False
    if c[-1]<0:
        return False
    return True
print(sum(list(map(lambda x:1 if i(x) else 0,g+list(zip(*g))))))
