from collections import deque
import sys

N = int(input())
stones = list(map(int, sys.stdin.readline().split()))


def bfs(K):
    visit = [False for i in range(len(stones))]
    queue = deque([0])

    while queue:
        now = queue.popleft()
        if now == len(stones) - 1:
            return True

        for next in range(now + 1, len(stones)):
            if not visit[next] and (next - now) * (1 + abs(stones[now] - stones[next])) <= K:
                queue.appendleft(next)
                visit[next] = True
    return False


def search(start, end):

    if start +1 == end:
        return end


    mid = (end + start) // 2
    if bfs(mid):
        return search(start, mid)
    else:
        return search(mid, end)


MAX_K = 1000000 * 5000
print(search(1, MAX_K))
