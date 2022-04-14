from math import gcd, ceil, inf
import sys

d, p, q = map(int, sys.stdin.readline().split())
if p < q:
    p, q = q, p
g = gcd(p, q)
a = p // g
b = q // g
if d >= g * (a - 1) * (b - 1):
    print(ceil(d / g) * g)
else:
    tmp = inf
    upper_p = ceil(d / p)
    for i in range(upper_p):
        tmp = min(tmp, i * p + ceil((d - i * p) / q) * q)

    tmp = min(tmp, p * upper_p)
    print(tmp)
