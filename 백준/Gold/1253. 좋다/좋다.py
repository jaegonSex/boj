import sys


def is_ok(index):
    num = nums[index]
    left = 0
    right = N - 1
    while left < right:
        if left == index:
            left+=1
        if right == index:
            right -=1
        if left == right:
            return 0

        tmp = nums[left] + nums[right]
        if num < tmp:
            right -= 1

        elif num > tmp:
            left += 1
        else:
            return 1
    return 0


N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

nums = sorted(nums)

print(sum([is_ok(i) for i in range(N)]))