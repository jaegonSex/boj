import math
import sys

n, s = map(int, sys.stdin.readline().split())
su_yoel = list(map(int, sys.stdin.readline().split()))
result = math.inf
end = 0
subset_sum = 0
for start in range(n):
    while end < n and subset_sum < s:
        subset_sum += su_yoel[end]
        end += 1
    if subset_sum>=s:
        result = min(result, end-start)
    subset_sum -= su_yoel[start]

print(result if result != math.inf else 0)