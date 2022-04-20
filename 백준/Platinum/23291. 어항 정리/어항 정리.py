import sys
from collections import deque
import copy


def rotate(arr):
    n, m = len(arr), len(arr[0])
    result = deque([deque([0 for i in range(n)]) for i in range(m)])
    for i in range(m):
        for j in range(n):
            result[i][j] = arr[n - 1 - j][i]
    return result


def is_in(x, y, arr):
    n = len(arr)

    if x < 0 or x >= n:
        return False
    m = len(arr[x])
    if y < 0 or y >= m:
        return False
    return True


def move_fishes(arr):
    result = copy.deepcopy(arr)

    dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for i in range(4):
                nx, ny = x + dxy[i][0], y + dxy[i][1]

                if is_in(nx, ny, arr):

                    d = (arr[nx][ny] - arr[x][y]) // 5
                    if d > 0:
                        result[nx][ny] -= d
                        result[x][y] += d

    return result


def unfold(arr):
    result = deque()
    tmp = deque()
    for i in range(len(arr[-1]) - len(arr[0])):
        tmp.appendleft(arr[-1].pop())
    arr = rotate(arr)
    for a in arr:
        result += a
    if tmp:
        result += tmp
    return result


def organize(arr):
    t = min(arr)

    for i in range(len(arr)):
        if arr[i] == t:
            arr[i] += 1

    tmp = [[arr.popleft()], [arr.popleft()]]
    tmp2 = rotate(tmp)
    tmp2.append(arr)
    arr = tmp2

    while len(arr) <= len(arr[-1]) - len(arr[0]):
        tmp = deque()
        for i in range(len(arr[0])):
            tmp.append(arr[-1].popleft())

        tail = arr.pop()
        arr.append(tmp)
        arr = rotate(arr)
        if len(tail) != 0:
            arr.append(tail)
        else:
            break
    arr = move_fishes(arr)
    arr = unfold(arr)

    tmp = deque()
    for i in range(len(arr) // 2):
        tmp.append(arr.popleft())
    tmp.reverse()
    result = deque()
    result.append(tmp)
    result.append(arr)
    arr = result
    tmp = deque()
    tmp2 = deque()

    for i in range(len(arr[0]) // 2):
        tmp.append(arr[0].popleft())
        tmp2.append(arr[1].popleft())
    tmp.reverse()
    tmp2.reverse()
    arr.appendleft(tmp)
    arr.appendleft(tmp2)

    arr = move_fishes(arr)
    arr = unfold(arr)

    return arr

n , k = map(int,sys.stdin.readline().split())
fish = deque(map(int,sys.stdin.readline().split()))
count = 0
while max(fish) - min(fish) >k:
    fish = organize(fish)
    count+=1
print(count)
