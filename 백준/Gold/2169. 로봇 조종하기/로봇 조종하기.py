n, m = map(int, input().split())
g = [list(map(int, input().split())) for i in range(n)]

left = [[0 for i in range(m)] for i in range(n)]
right = [[0 for i in range(m)] for i in range(n)]
mid = [[0 for i in range(m)] for i in range(n)]
left[0][0] = g[0][0]
right[0][0] = g[0][0]
for i in range(m):
    left[0][i] = left[0][i - 1] + g[0][i]
    right[0][i] = right[0][i - 1] + g[0][i]
    mid[0][i] = mid[0][i - 1] + g[0][i]

for i in range(1, n):
    left[i][0] = mid[i - 1][0] + g[i][0]

    right[i][m - 1] = mid[i - 1][m - 1] + g[i][m - 1]
    for j in range(1, m):
        left[i][j] = max(left[i][j - 1], mid[i - 1][j]) + g[i][j]
        right[i][m - 1 - j] = max(right[i][m - j], mid[i - 1][m - 1 - j]) + g[i][m - 1 - j]

    for j in range(m):
        mid[i][j] = max(right[i][j], left[i][j])
print(mid[-1][-1])
