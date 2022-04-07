n = int(input())
graph = {}
for i in range(n):
    p, c1, c2 = input().split()
    graph[p] = (c1,c2)


answer = [[], [], []]
def visit(node):
    if node == '.':
        return
    answer[0].append(node)
    l, r =graph[node]
    visit(l)
    answer[1].append(node)
    visit(r)
    answer[2].append(node)

visit('A')
answer = map(lambda x:''.join(x), answer)
print(*answer)
