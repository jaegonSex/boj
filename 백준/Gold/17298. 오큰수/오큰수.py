import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().split()))
result = [0 for i in range(len(A))]
s = []
for i in range(len(A) -1, -1 , -1):
    if not s:
        result[i] = -1
        s.append(A[i])
    else:
        if s[-1] > A[i]:
            result[i] = s[-1]
            s.append(A[i])
            continue
        else:
            while s and s[-1]<= A[i]:
                s.pop()

            if s:
                result[i] = s[-1]
                s.append(A[i])
            else:
                result[i]= -1
                s.append(A[i])
print(*result)