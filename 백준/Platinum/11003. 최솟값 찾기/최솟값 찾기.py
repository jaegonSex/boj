import sys
import heapq

n, l = map(int, sys.stdin.readline().split())
N = list(map(int,sys.stdin.readline().split()))
minheap = []

for i in range(n):
    heapq.heappush(minheap, (N[i], i))

    if i - l + 1 <= minheap[0][1]:

        print(minheap[0][0])
    else:
        while i - l + 1  >minheap[0][1]:
            heapq.heappop(minheap)

        print(minheap[0][0])
