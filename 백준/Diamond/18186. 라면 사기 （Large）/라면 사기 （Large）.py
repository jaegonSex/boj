import re
import sys

n ,b,c = map(int,sys.stdin.readline().split())

mylist = list(map(int, sys.stdin.readline().split()))
if b<= c:
    print(b*sum(mylist))


else:
    c2 = 0
    c1 = 0
    count = 0
    for d in mylist:
        if d == 0:
            c1 = 0
            c2 = 0
        else:
            n1 = min(c2, d)
            n2 = max(0, d - n1 - c1)
            count += b * d

            count -= (b-c)*min(c1+c2, d)
            c1 = n1
            c2 = n2


    print(count)
