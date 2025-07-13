class LazySegTree:

    def __init__(self, n, op, e):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.leaves = 2**(len(nb)-1)
        else:
            self.leaves = 2**(len(nb))

        self.n = n
        self.array = [e for i in range(self.leaves * 2)]
        self.lazy = [e for i in range(self.leaves * 2)]
        self.e = e
        self.op = op
    
    def eval(self, x):
        if self.lazy[x] == self.e:
            return
        if x < self.leaves-1:
            self.lazy[x*2+1] = self.lazy[x]
            self.lazy[x*2+2] = self.lazy[x]
        self.array[x] = self.lazy[x]
        self.lazy[x] = self.e

    def set(self, x, val):
        actual_x = x+self.leaves-1
        self.array[actual_x] = val
    
    def build(self):
        for i in range(self.leaves-2, -1, -1):
            self.array[i] = self.op(self.array[2*i+1], self.array[2*i+2])

    def update(self, q_left, q_right, val, x=0, leaf_left=0, depth=0):
        q_right -= 1 #open section
        self.eval(x)
        width_of_floor = self.leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if q_left<=leaf_left and leaf_right<=q_right:
            self.lazy[x] = val
            self.eval(x)
        elif q_left<=leaf_right and leaf_left<=q_right:
            # q_right+1: open section,  q_right: closed section
            self.update(q_left, q_right+1, val, 2*x+1, leaf_left, depth+1)
            self.update(q_left, q_right+1, val, 2*x+2, leaf_left+width_of_floor//2, depth+1)
            self.array[x] = self.op(self.array[2*x+1], self.array[2*x+2])

    def get(self, q_left, q_right, x=0, leaf_left=0, depth=0):
        q_right -= 1 #open section
        self.eval(x)
        width_of_floor = self.leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return self.e

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[x]

        else:
            # q_right+1: open section,  q_right: closed section
            val_l = self.get(q_left, q_right+1, 2*x+1, leaf_left, depth+1)
            val_r = self.get(q_left, q_right+1, 2*x+2, leaf_left+width_of_floor//2, depth+1)
            return self.op(val_l,val_r)
        
    def get(self, left, right):
        left += self.leaves-1
        right += self.leaves-1
        lres, rres = self.e, self.e

        while left < right:
            if left%2 == 0:
                self.eval(left)
                lres = self.op(lres, self.array[left])
                left += 1
            if right%2 == 0:
                right -= 1
                self.eval(right)
                rres = self.op(rres, self.array[right])
        
            left = (left-1)//2
            right = (right-1)//2

        res = self.op(lres, rres)
        return res