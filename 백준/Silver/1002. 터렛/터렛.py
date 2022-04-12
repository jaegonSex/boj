import sys
tc = int(sys.stdin.readline().rstrip())
def getdist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
for i in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = getdist(x1,y1,x2,y2)
    result = 0
    if dist == 0:
        if r1== r2:
            result = -1
        else :
            result = 0
    elif dist > r1 + r2:
        result = 0
    elif dist == r1 + r2:
        result = 1
    elif abs(r1-r2)< dist <r1 + r2:
        result = 2
    elif dist == abs(r1-r2):
        result = 1
    elif dist> abs(r1 - r2):
        result = 0
    print(result)

