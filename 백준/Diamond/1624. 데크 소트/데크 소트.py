import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
A = []
for i in range(n):
    A.append(int(sys.stdin.readline().rstrip()))
A = [(i, A[i]) for i in range(len(A))]

A.sort(key=lambda x: (x[1], -x[0]))


def get_lump(idx):
    tmp = A[idx][0]
    while idx + 1 < len(A) and A[idx + 1][1] == A[idx][1]:
        idx += 1
    tmp2 = A[idx][0]

    return max(tmp, tmp2), min(tmp, tmp2), idx





def bfs(idx):
    queue = deque()
    M, m, index = get_lump(idx)
    queue.append((M, m, index, 0))

    while queue:
        M, m, now, switch = queue.popleft()
        if now + 1 >len(A)-1:
            return now
        nM, nm, nindex = get_lump(now+1)
        if switch == 0:
            if m > nM:
                queue.append((nM, nm, nindex, 0))
            else:
                queue.append((nM, nm, nindex, 1))
        if switch == 1:
            if M<nm:
                queue.append((nM,nm,nindex,1))
            else:
                return now


count = 0
idx = 0
while True:
    _next = bfs(idx) + 1
    count+=1
    if _next>len(A)-1:
        break
    else:
        idx = _next
print(count)
