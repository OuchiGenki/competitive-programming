import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

class SegTree:

    def __init__(self, n, op, e):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.leaves = 2**(len(nb)-1)
        else:
            self.leaves = 2**(len(nb))

        self.array = [e for i in range(self.leaves * 2)]
        self.e = e
        self.op = op

    def set(self, x, val):
        actual_x = x+self.leaves-1
        self.array[actual_x] = val
    
    def build(self):
        for i in range(self.leaves-2, -1, -1):
            self.array[i] = self.op(self.array[2*i+1], self.array[2*i+2])

    def update(self, x, val):
        actual_x = x+self.leaves-1
        self.array[actual_x] = val
        while actual_x > 0 :
            actual_x = (actual_x-1)//2
            self.array[actual_x] = self.op(self.array[actual_x*2+1],self.array[actual_x*2+2])

    def get(self, left, right):
        left += self.leaves-1
        right += self.leaves-1
        lres, rres = self.e, self.e

        while left < right:
            if left%2 == 0:
                lres = self.op(lres, self.array[left])
                left += 1
            if right%2 == 0:
                right -= 1
                rres = self.op(rres, self.array[right])
        
            left = (left-1)//2
            right = (right-1)//2

        res = self.op(lres, rres)
        return res

w, n = map(int, input().split())
Seg = [SegTree(w+1, max, -1) for i in range(n+1)]
Seg[0].update(0, 0)
dp = [[-1 for i in range(w+1)] for i in range(n+1)]
dp[0][0] = 0
l, r, v = [], [], []
for i in range(n):
    L, R, V = map(int, input().split())
    l.append(L)
    r.append(R)
    v.append(V)

for i in range(1, n+1):
    for j in range(w+1):
        maxS = Seg[i-1].get(max(0, j-r[i-1]), min(w+1, j-l[i-1]+1))
        if maxS!=-1:
            dp[i][j] = maxS + v[i-1]
        dp[i][j] = max(dp[i][j], dp[i-1][j])
    for j in range(w+1):
        #Seg[i].update(j, dp[i][j])
        Seg[i].set(j, dp[i][j])
    Seg[i].build()

ans = Seg[n].get(w, w+1)
if ans==0:
    print(-1)
else:
    print(ans)