import sys
import bisect
n = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().split()))
dp = [0 for i in range(len(A))]
dp_back = [0 for i in range(len(A))]

tmp = []
for i in range(len(A)):
    idx = bisect.bisect_left(tmp, A[i])
    if idx>len(tmp)-1:
        tmp.append(A[i])
    else:
        tmp[idx] = A[i]
    dp[i] = len(tmp)

tmp = []
result = 0
for i in range(len(A)-1,-1, -1):
    idx = bisect.bisect_left(tmp, A[i])
    if idx>len(tmp)-1:
        tmp.append(A[i])
    else:
        tmp[idx] = A[i]
    dp_back[i] = len(tmp)

for i in range(len(A)):
    result = max(result ,dp[i] + dp_back[i] -1)


print(result)