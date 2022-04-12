import sys

# 시간 , 크기 , 가운데 , 범위
s, n, k, r1, r2, c1, c2 = map(int, sys.stdin.readline().split())


def is_black(x, y, n, k, s):
    if s == 0:
        return False

    now = n ** s
    tx = x // n ** (s - 1)
    ty = y // n ** (s - 1)
    if (n - k) // 2 <= tx < n - (n - k) // 2 and (n - k) // 2 <= ty < n - (n - k) // 2:

        return True
    else:
        return is_black(x - tx * n ** (s - 1), y - ty * n ** (s - 1), n, k, s - 1)


for i in range(r1,r2 +1):
    for j in range(c1,c2+1):
        print(1 if is_black(i,j,n,k,s) else 0, end='')
    print()