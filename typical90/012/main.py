import sys
sys.setrecursionlimit(10**7)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for i in range(n)]
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return

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
        return {r: self.members(r) for r in self.roots()}
    
h, w = map(int, input().split())
q = int(input())
uf = UnionFind(h*w)
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
f = [[False for i in range(w)] for j in range(h)]

for i in range(q):
    li = list(map(int, input().split()))
    if li[0] == 1:
        r = li[1]-1
        c = li[2]-1
        f[r][c] = True
        for j in range(4):
            rr = r + dr[j]
            cc = c + dc[j]
            if rr<0 or cc<0 or rr>=h or cc>=w:
                continue
            if f[rr][cc]:
                uf.union(w*r+c, w*rr+cc)
    
    else:
        ra = li[1]-1; ca = li[2]-1; rb = li[3]-1; cb = li[4]-1
        if f[ra][ca] and f[rb][cb]:
            if uf.same(w*ra+ca, w*rb+cb):
                print("Yes")
            else:
                print("No")
        else:
            print("No")