import sys
import math


def pick(a, b):
    global w
    return 1 if a + b <= w else 2


t = int(sys.stdin.readline().rstrip())


def fill_dp():
    for i in range(2, n + 1):
        dp[0][i] = min(dp[2][i - 1] + 1, dp[1][i - 1] + pick(onetagon[0][i - 1], onetagon[0][i]))
        dp[1][i] = min(dp[2][i - 1] + 1, dp[0][i - 1] + pick(onetagon[1][i - 1], onetagon[1][i]))
        dp[2][i] = min(dp[2][i - 1] + pick(onetagon[0][i], onetagon[1][i]),
                       dp[2][i - 2] + pick(onetagon[0][i], onetagon[0][i - 1]) + pick(onetagon[1][i],
                                                                                      onetagon[1][i - 1]),
                       dp[0][i - 1] + 1 + pick(onetagon[1][i], onetagon[1][i - 1]),
                       dp[1][i - 1] + 1 + pick(onetagon[0][i], onetagon[0][i - 1])
                       )


for tc in range(t):
    n, w = map(int, sys.stdin.readline().split())
    onetagon = [[0] + list(map(int, sys.stdin.readline().split())) for i in range(2)]

    dp = [[0 for i in range(n + 1)] for i in range(3)]

    if n == 1:
        print(pick(onetagon[0][1], onetagon[1][1]))
    else:
        result = []

        dp[0][1], dp[1][1], dp[2][1] = 1, 1, pick(onetagon[0][1], onetagon[1][1])
        fill_dp()
        result.append(dp[2][n])

        if pick(onetagon[0][1], onetagon[0][n]) == 1:
            onetagon[0][1], tmp = math.inf, onetagon[0][1]
            dp[0][1], dp[1][1], dp[2][1] = 1, 1, 2


            fill_dp()
            onetagon[0][1] = tmp

            result.append(dp[1][n])

        if pick(onetagon[1][1], onetagon[1][n]) == 1:
            onetagon[1][1], tmp = math.inf, onetagon[1][1]
            dp[0][1], dp[1][1], dp[2][1] = 1, 1, 2

            fill_dp()
            onetagon[1][1] = tmp
            result.append(dp[0][n])

        if pick(onetagon[0][1], onetagon[0][n]) == 1 and pick(onetagon[1][1], onetagon[1][n]) == 1:
            dp[0][1], dp[1][1], dp[2][1] = 1, 1, 2
            onetagon[0][1], onetagon[1][1] = math.inf, math.inf
            fill_dp()
            result.append(dp[2][n - 1])

        print(min(result))
