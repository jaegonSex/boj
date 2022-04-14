from collections import deque
import sys
import bisect

n = int(sys.stdin.readline().rstrip())
A = map(int, sys.stdin.readline().split())
info = {}

I = []
check = []
last = 0
for num in A:
    idx = bisect.bisect_left(I, num)

    if idx >= len(I):
        I.append(num)
        check.append((idx, num))


    else:
        I[idx]= num
        check.append((idx, num))
length =len(I) - 1
result = [None for i in range(length + 1)]
while check:
    nidx, nnum = check.pop()
    if nidx == length:
        result[nidx] = nnum
        length-=1
print(len(result))
print(*result)