import sys

n = int(sys.stdin.readline().rstrip())
chess = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
result = set()


def check(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def can_place(x, y):  # 좌 상 ~ 우 하 체크
    if chess[x][y] == 0:
        return False
    tmp = min(x, y)
    start_x, start_y = x - tmp, y - tmp
    for i in range(n + - (start_x + start_y)):
        if (start_x + i, start_y + i) in result:
            return False
    return True


c = [0]


def choice(k):
    if k >= 2 * n - 1:

        c[0] = max(c[0], len(result))
        return
    if k < n:
        start_x, start_y = k, 0
        count = k + 1
    else:
        start_x, start_y = n - 1, k - n + 1
        count = 2 * n - 1 - k

    choice(k + 2)
    for i in range(count):
        if can_place(start_x - i, start_y + i):
            result.add((start_x - i, start_y + i))
            choice(k + 2)
            result.remove((start_x - i, start_y + i))




choice(0)
tmp = c[0]
c[0] = 0

choice(1)
print(c[0] + tmp)
