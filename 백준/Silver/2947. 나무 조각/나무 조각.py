import sys

jogak = list(map(int,sys.stdin.readline().split()))
def is_ok(jogak):
    for i in range(5):
        if jogak[i] != i + 1:
            return False
    return True

def swap(jogak):
    idx = 0
    while True:
        flag = True
        if jogak[idx] > jogak[idx +1]:
            jogak[idx] ,jogak[idx +1] = jogak[idx+1], jogak[idx]
            print(*jogak)
            if is_ok(jogak):
                break
            
        idx+=1
        idx%=4
        

swap(jogak)
