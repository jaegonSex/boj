import sys
import bisect

n = int(sys.stdin.readline().rstrip())
junbotdae = []
info = {}

I = [0]
P = {}
for i in range(n):
    order, num = map(int, sys.stdin.readline().split())
    junbotdae.append((order, num))
    info[num] = order
junbotdae.sort()
for order, num in junbotdae:
    idx = bisect.bisect(I, num)

    if idx >= len(I):
        I.append(num)
        P[num] = I[idx - 1]
    else:
        I[idx] = num
        P[num] = I[idx - 1]

remain = set()
last = I[-1]

while last != 0:

    remain.add(info[last])
    last = P[last]

print(n - len(remain))
for order, num in junbotdae:
    if order not in remain:
        print(order)