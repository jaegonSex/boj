import sys
from collections import deque
target= deque(sys.stdin.readline().rstrip())
del_str = sys.stdin.readline().rstrip()

left = deque()
check = deque()
def is_same():
    for i in range(len(del_str)):
        if check[i] != del_str[i]:
            return False
    return True

def delete_str():
    while target:
        check.append(target.popleft())
        if len(check) == len(del_str):
            if is_same():
                check.clear()
                for i in range(len(del_str)*2):
                    if left:
                        target.appendleft(left.pop())
                    else:
                        break
            else:
                left.append(check.popleft())
    while check:
        left.append(check.popleft())

delete_str()
if left or target:
    print(''.join(left),''.join(target),sep='')
else:
    print("FRULA")