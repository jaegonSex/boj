n = int(input())
inorder = input().split()
postorder = input().split()

idxx = {inorder[i]:i for i in range(len(postorder))}

result = []

stack = [(0, n-1, 0, n-1)]
while stack:
    ps, pe, s, e = stack.pop()

    if ps>pe or s>e:
        continue
    root = postorder[pe]
    result.append(root)
    idx = idxx[root]
    l = idx - s
    r = e - idx
    

    stack.append((ps+l, pe-1 , idx+1, e))
    stack.append((ps, ps+l-1 , s, idx-1))

print(' '.join(result))
