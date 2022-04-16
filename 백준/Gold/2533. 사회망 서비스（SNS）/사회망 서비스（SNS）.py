import sys

sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline().rstrip())

tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[v].append(u)
    tree[u].append(v)

dp = [[1, 0] for i in range(n + 1)]

visit = [False for i in range(n + 1)]
def dfs(node):

    visit[node] = True

    for next_node in tree[node]:
        if not visit[next_node]:

            dfs(next_node)
            dp[node][1] += dp[next_node][0]
            dp[node][0] += min(dp[next_node][1], dp[next_node][0])


dfs(1)

print(min(dp[1]))
