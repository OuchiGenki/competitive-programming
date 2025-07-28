###############################################################
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
###############################################################

import heapq

n, m = map(int, input().split())
UF = UnionFind(n)
G = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a-1].append((c, b-1))
    G[b-1].append((c, a-1))
    UF.union(a-1, b-1)
k, T = map(int, input().split())
D = list(map(int, input().split()))
for i in range(k):
    for j in range(k):
        if i == j:
            continue
        G[D[i]-1].append((T, D[j]-1))
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y, t = query[1], query[2], query[3]
        G[x-1].append((t, y-1))
        G[y-1].append((t, x-1))
        UF.union(x-1, y-1)
    elif query[0] == 2:
        x = query[1]
        for i in range(n):
            G[x-1].append((T, D[i]-1))
            G[D[i]-1].append((T, x-1))
            UF.union(D[i]-1, x-1)
    elif query[0] == 3:
        pass
