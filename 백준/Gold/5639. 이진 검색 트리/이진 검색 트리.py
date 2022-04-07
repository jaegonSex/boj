import sys
sys.setrecursionlimit(10**6)
nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break



def solution(start , end):
    if start > end:
        return
    root = nodes[start]

    idx = end + 1
    for i in range(start, end+1):
        if nodes[i] > root:
            idx = i
            break

    solution(start+1, idx-1)

    solution(idx,end)
    print(root)

solution(0, len(nodes)-1)
