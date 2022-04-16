import math
import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0


def makeset(x):
    return Node(x)


def find(x):
    while x.parent != x:
        x = x.parent
    return x


def union(x, y):
    v, w = find(x), find(y)
    if v.rank > w.rank:
        v, w = w, v
    v.parent = w
    if v.rank == w.rank:
        w.rank += 1

n, m = map(int,sys.stdin.readline().split())
arr = [makeset(i) for i in range(n+1)]
for i in range(m):
    o, a, b = map(int,sys.stdin.readline().split())
    if o==0:
        union(arr[a], arr[b])
    else:
        print("yes" if find(arr[a])==find(arr[b]) else "no")

