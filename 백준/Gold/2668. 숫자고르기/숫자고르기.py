arr= [0]
n =int(input())
def can_pick(num):
    visit = set()

    now = num
    visit.add(now)
    while True:
        _next = arr[now]
        if _next == num:
            return True
        if _next in visit:
            return False
        visit.add(_next)
        now = _next




for i in range(n):
    arr.append(int(input()))
result = []
for i in range(n):
    if can_pick(i+1):
        result.append(i+1)

print(len(result))
print(*result, sep='\n')