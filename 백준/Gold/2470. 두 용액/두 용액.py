import math
import sys

n = int(sys.stdin.readline().rstrip())
yong_aek = list(map(int, sys.stdin.readline().split()))
yong_aek.sort()

result = [math.inf, 0, 0]
alkali = 0
acid = n - 1
c= 0
while alkali<acid:
    tmp = yong_aek[alkali] + yong_aek[acid]

    if result[0] > abs(tmp):
        result[0] = abs(tmp)
        result[1] = yong_aek[alkali]
        result[2] = yong_aek[acid]
        if result[0] == 0:
            break

    if tmp > 0:

        acid -= 1
    else:

        alkali += 1

print(*result[1:])



