import sys

n, m, k = map(int, sys.stdin.readline().split())

arr = [0 for i in range(n + 1)]
t = [0 for i in range(n + 1)]


def prefix_sum(k):
    s = 0
    while k >= 1:
        s += t[k]
        k -= lsb(k)

    return s


def update(k, diff):
    d = diff - arr[k]
    arr[k] = diff
    while k <= len(arr) - 1:
        t[k] += d
        k += lsb(k)


def lsb(k):
    return k & -k

for i in range(1, n + 1):
    update(i, int(sys.stdin.readline().rstrip()))


for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())


    if a == 1:
        update(b, c)
    else:
        print(prefix_sum(c) - prefix_sum(b - 1))

