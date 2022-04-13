import sys
import collections

n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().split()))
counts = collections.Counter(nums)
result = [-10]
c = sorted([[i, counts[i]] for i in counts], reverse=True)

for i in range(len(nums)):
    if len(c) == 2:

        if c[1][0] + 1 == c[0][0]:
            result += [c[0][0]] * c[0][1]
            result += [c[1][0]] * c[1][1]
            break


    if result[-1] + 1 == c[-1][0]:
        result.append(c[-2][0])
        c[-2][1] -= 1
        if c[-2][1] == 0:
            del c[-2]
    else:
        result.append(c[-1][0])
        c[-1][1] -= 1
        if c[-1][1] == 0:
            del c[-1]

for i in range(1, len(result)):
    print(result[i], end=' ')
