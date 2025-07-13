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

    def update(self, x, val):
        actual_x = x+self.leaves-1
        self.array[actual_x] ^= val
        while actual_x > 0 :
            actual_x = (actual_x-1)//2
            self.array[actual_x] = self.op(self.array[actual_x*2+1],self.array[actual_x*2+2])

    def get(self, q_left, q_right, x=0, leaf_left=0, depth=0):
        q_right -= 1 #open section
        width_of_floor = self.leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return  self.e

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[x]

        else:
            # q_right+1: open section,  q_right: closed section
            val_l = self.get(q_left,q_right+1,2*x+1,leaf_left,depth+1)
            val_r = self.get(q_left,q_right+1,2*x+2,leaf_left+width_of_floor//2,depth+1)
            return self.op(val_l,val_r)

def f(a, b):
    return a^b

n, q = map(int, input().split())
a = list(map(int, input().split()))
Seg = SegTree(n, f, 0)

for i in range(n):
    Seg.update(i, a[i])

for i in range(q):
    li = list(map(int, input().split()))
    t, x, y = li[0], li[1]-1, li[2]
    if t == 1:
        Seg.update(x, y)
    else:
        print(Seg.get(x, y))