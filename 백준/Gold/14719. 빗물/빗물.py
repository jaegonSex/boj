import sys
from collections import deque, Counter
h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
graph = deque([deque(['0' for i in range(w)]) for i in range(h)])
idx = 0
for block in blocks:
    for i in range(block):
        graph[i][idx] = '1'
    idx+=1
count = 0
for i in graph:
    count +=Counter(''.join(i).rstrip('0').lstrip('0'))['0']
print(count)