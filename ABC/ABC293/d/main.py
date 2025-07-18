class UnionFind():
    def __init__(self, n):
        self.n = self.parents = [-1 for i in range(n)]
    
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

n, m = map(int, input().split()) 
UF = UnionFind(n)

x = 0
for i in range(m):
    li = input().split()
    if UF.same(int(li[0])-1, int(li[2])-1):
        x += 1
    UF.union(int(li[0])-1, int(li[2])-1)

print(x, UF.group_count()-x)