a, b, c =map(int,input().split())
def power(num, p):
    global c

    if p == 0:
        return 1

    h = power(num, p//2)
    if p%2 == 0:
        return ((h%c) * (h%c)) %c
    else:
        return ((h%c) * (h%c) * (num%c)) % c

print(power(a,b))
