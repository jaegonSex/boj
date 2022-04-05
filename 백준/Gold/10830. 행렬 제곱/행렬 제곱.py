N, B = map(int,input().split())
matrix = [list(map(lambda x:int(x)%1000,input().split()))for i in range(N)]

def matrix_product(m1, m2):
    length = len(m1)
    result = [[0 for i in range(length)]for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j]= result[i][j] % 1000
    return result

def power_matrix(m, pow):
    if pow == 1:
        return m

    half = power_matrix(m,pow//2)
    result = matrix_product(half,half)
    if pow%2 ==0:
        return result
    else:
        return matrix_product(result,m)

result = power_matrix(matrix,B)

for i in range(N):
    for j in range(N):
        print(result[i][j], end = ' ',)
    print()
