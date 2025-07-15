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

h, w = map(int, input().split())
q = int(input())
painted = [[False] * w for i in range(h)]
UF = UnionFind(h * w)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r, c = query[1]-1, query[2]-1
        painted[r][c] = True
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rr, cc = r + d[0], c + d[1]
            if rr < 0 or rr >= h or cc < 0 or cc >= w:
                continue
            if painted[rr][cc]:
                UF.union(r*w + c, rr * w + cc)
    elif query[0] == 2:
        ra, ca, rb, cb = query[1]-1, query[2]-1, query[3]-1, query[4]-1
        if painted[ra][ca] and painted[rb][cb] and UF.same(ra*w+ca, rb*w+cb):
            print('Yes')
        else:
            print('No')