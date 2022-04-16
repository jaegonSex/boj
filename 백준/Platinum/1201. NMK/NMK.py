import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
nums = deque([i + 1 for i in range(n - 1)])

if not m + k - 1 <= n <= m * k:
    print(-1)
    sys.exit()

left = deque()
right = deque()

left_count = 0
right_count = 0


def fill_left(count):
    global left
    if count == 0:
        return False
    tmp = deque()
    while nums and count != 0:
        tmp.appendleft(nums.pop())
        count -= 1
    left += tmp
    return True


def fill_right(count):
    global right
    if count == 0:
        return False
    tmp = deque()
    while nums and count != 0:
        tmp.append(nums.pop())
        count -= 1
    right = tmp + right
    return True


roop = 0
while nums:
    if m - right_count > 0:
        fill_left(m - max(1, right_count))
        left_count += 1

    if k - left_count > 0:
        if fill_right(k - max(1, left_count)):
            right_count += 1
    roop += 1
    if roop == n:
        print(-1)
        sys.exit()
        break

print(*left, n, *right)
