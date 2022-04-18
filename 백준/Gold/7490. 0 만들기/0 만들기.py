import sys
from collections import deque


def make(n):
    result = []
    queue = deque([(1, 1, '+1')])
    while queue:
        now, i, expression = queue.popleft()

        if i>n:
            continue
        if i==n and now==0:
            result.append(expression[1:])

        queue.append((now + (i + 1), i + 1, expression + '+' + str(i+1)))
        queue.append((now - (i + 1), i + 1, expression + '-' + str(i+1)))
        if expression[-2] == '-':
            op = -1
            tmp = i
            queue.append((now + tmp + op * (10 * i + (i + 1)), i + 1, expression + ' ' + str(i + 1)))
        elif expression[-2] == '+':
            op = 1
            tmp = -i
            queue.append((now + tmp + op * (10 * i + (i + 1)), i + 1, expression +' '+str(i+1)))
    result.sort()
    return result


t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(*make(n),sep='\n')
    print()

