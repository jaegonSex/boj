from sys import stdin

p, f = map(int, stdin.readline().split())

pumps = list(map(lambda x: (int(x), 0), stdin.readline().split()))
fire_trucks = list(map(lambda x: (int(x), 1), stdin.readline().split()))
pumps_and_trucks = sorted(pumps + fire_trucks)

matchable = [[] for _ in range(p + f)]
depth = p - 1
for i in range(len(pumps_and_trucks)):
    if pumps_and_trucks[i][1] == 0:
        depth -= 1
        matchable[depth].append(pumps_and_trucks[i][0])
    else:
        matchable[depth].append(pumps_and_trucks[i][0])
        depth += 1

result = 0
for matches in matchable:
    all_cost = 0

    for i in range(1, len(matches), 2):
        all_cost += matches[i] - matches[i - 1]


    min_cost = all_cost
    tmp = all_cost

    if len(matches) % 2 == 1:

        for i in range(len(matches) - 1, 1, -2):
            swap = tmp + (matches[i] - matches[i - 1]) - (matches[i - 1] - matches[i - 2])
            min_cost = min(min_cost, swap)
            tmp = swap

    result += min_cost

print(result)
