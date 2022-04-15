import math
import sys

n = int(sys.stdin.readline().rstrip())
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

primes = prime_list(4000001)
count = 0
end = 0
subset_sum = 0
for start in range(len(primes)):
    while end < len(primes) and subset_sum<n:
        subset_sum+=primes[end]
        end+=1
    if subset_sum == n:
        count +=1
    subset_sum-=primes[start]
print(count)