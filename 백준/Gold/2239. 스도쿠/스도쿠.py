import sys
Map = [list(map(int,input()))for i in range(9)]

# 체크해야될게 x,?  ?,x x//3~ +3 y//3~ +3
sex = []
for i in range(9):
    for j in range(9):
        if Map[i][j] == 0:
            sex.append((i,j))
def sdoku(c):
    if c >= len(sex):
        for i in Map:
            i=''.join(map(str,i))
            print(i)
        sys.exit(0)
        return
    x,y=sex[c]
    for num in range(1,10):
        if can(x,y,num):
            Map[x][y]=num
            sdoku(c+1)
            Map[x][y]=0


def can(x,y,num):
    for i in range(9):
        if Map[i][y] == num:
            return False
    for i in range(9):
        if Map[x][i] == num:
            return False
    a = x//3*3
    b= y//3*3
    for i in range(3):
        for j in range(3):
            if Map[a+i][b+j] == num:
                return False
    return True

a, b = sex[0]
sdoku(0)
