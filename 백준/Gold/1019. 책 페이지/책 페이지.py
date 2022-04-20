import sys
from collections import Counter
N = input()
dp = [0 for i in range(11)]
dp[0] = 1
for i in range(1, 11):
    dp[i] = dp[i - 1] * 10 + 10 ** i



result = [0 for i in range(10)]
def calc(num, idx):
    if idx == len(num)-1:
        for i in range(int(num[idx])+ 1):
            result[i]+=1
        return
    pow = len(num)-idx
    for i in range(int(num[idx])):

        for j in range(10):
            result[j]+=dp[pow-2]

        result[i] += 10**(pow-1)
    result[int(str(num)[idx])]+= int(str(num)[idx+1:])+1

    calc(num,idx+1)


calc(N, 0)
result[0]-= int('1' * len(N))
print(*result)
