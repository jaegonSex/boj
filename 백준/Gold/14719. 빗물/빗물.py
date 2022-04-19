import sys
from collections import deque
h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
graph = deque([deque([0 for i in range(w)]) for i in range(h)])
idx = 0
for block in blocks:
    for i in range(block):
        graph[i][idx] = 1
    idx+=1
def pop_side_zero(deq):
    while True:
        if deq and deq[0]==0:
            deq.popleft()
        if deq and deq[-1] ==0:
            deq.pop()
        if not deq or (deq[0] ==1 and deq[-1]==1):
            break
    return deq


result = 0
for i in graph:
    result += sum([1 for i in pop_side_zero(i) if i == 0])

print(result)
