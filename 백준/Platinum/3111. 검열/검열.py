from collections import deque
import sys


def check_same():
    for _ in range(len(A)):
        if check[_] != A[_]:
            return False
    return True


A = sys.stdin.readline().rstrip()
mid = deque(sys.stdin.readline().rstrip())

right = deque()
left = deque()

check = deque()


def check_front():
    while mid:

        check.append(mid.popleft())
        if len(check) >= len(A):
            if check_same():
                check.clear()

                count = 0
                while count <= len(A)*2 and left:
                    mid.appendleft(left.pop())
                    count += 1
                return True
            else:
                left.append(check.popleft())
    while check:
        left.append(check.popleft())
    return False


def check_back():
    while mid:

        check.appendleft(mid.pop())
        if len(check) >= len(A):

            if check_same():
                check.clear()

                count = 0
                while count <= len(A)*2 and right:
                    mid.append(right.popleft())
                    count+=1

                return True
            else:
                right.appendleft(check.pop())
    while check:
        right.appendleft(check.pop())
    return False


while True:
    if not check_front():
        print(''.join(left) , ''.join(mid), ''.join(right), sep = '')
        break
    if not check_back():
        print(''.join(left) , ''.join(mid), ''.join(right), sep = '')
        break
