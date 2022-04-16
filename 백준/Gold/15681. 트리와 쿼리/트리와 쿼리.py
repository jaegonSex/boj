import sys
sys.setrecursionlimit(10**6)
n, r, q = map(int, sys.stdin.readline().split())


class Node:
    def __init__(self):
        self.parent = -1
        self.size = 1
    def adopt(self, child):
        child.parent = self
        self.size += child.size


nodes = [Node() for i in range(n + 1)]
tree = {}
for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in tree:
        tree[u] = []
    if v not in tree:
        tree[v] = []
    tree[v].append(u)
    tree[u].append(v)



visit = set()
def make_tree(node):
    visit.add(node)
    for next in tree[node]:
        if next not in visit and nodes[next].parent != nodes[node]:
            make_tree(next)
            nodes[node].adopt(nodes[next])


make_tree(r)
for i in range(q):
    print(nodes[int(sys.stdin.readline().rstrip())].size)
