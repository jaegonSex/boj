import sys
from collections import deque
import heapq
n = int(sys.stdin.readline().rstrip())
red = list(map(int,sys.stdin.readline().split()))
blue =list(map(int,sys.stdin.readline().split()))

l = deque(sorted(zip(red, blue),key= lambda x:x[1]))

minimum = l.popleft()
maximum = l.pop()
compare = []
while l:
    heapq.heappush(compare, (l.pop()))
    heapq.heappush(compare, (l.pop()))
    heapq.heappop(compare)


result = minimum[0] + sum(map(lambda x:x[0], compare))

print(result)


