import sys
from collections import deque
import math
import bisect
import fractions
import decimal

n = int(sys.stdin.readline().rstrip())
cake = deque(sorted(map(lambda x: (int(x), int(x), 1), sys.stdin.readline().split())))
m = int(sys.stdin.readline().rstrip())

answer = math.inf
for i in range(m):
    large = cake[-1][0]
    small = cake[0][0]
    answer = min(answer, abs(cake[0][0] - cake[-1][0]))
    if large == small:
        answer = 0
    size, original, div = cake.pop()
    bisect.insort(cake, (original / (div + 1), original, div + 1))

answer = min(answer, abs(cake[0][0] - cake[-1][0]))

print('%0.16f'%float(answer))
