class LazySegTree:

    def __init__(self, n, op, e):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.leaves = 2**(len(nb)-1)
        else:
            self.leaves = 2**(len(nb))

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

    def update(self, a, b, val, x=0, l=0, depth=0):
        b -= 1 #open section
        print("x =", x)
        self.eval(x)
        width_of_floor = self.leaves//(2**depth)
        r = l+width_of_floor-1
        print("a =", a, " b =", b)
        print("l =", l, " r =", r)
        print()

        if a<=l and r<=b:
            self.lazy[x] = val
            print("Test")
            self.eval(x)
            print(self.lazy)
        elif a<=r and l<=b:
            # b+1: open section,  b: closed section
            self.update(a, b+1, val, 2*x+1, l, depth+1)
            self.update(a, b+1, val, 2*x+2, l+width_of_floor//2, depth+1)
            self.array[x] = self.op(self.array[2*x+1], self.array[2*x+2])

    def get(self, a, b, x=0, l=0, depth=0):
        b -= 1 #open section
        self.eval(x)
        width_of_floor = self.leaves//(2**depth)
        r = l+width_of_floor-1

        if l > b or r < a:
            return self.e

        elif l >= a and r <= b:
            return self.array[x]

        else:
            # b+1: open section,  b: closed section
            val_l = self.get(a, b+1, 2*x+1, l, depth+1)
            val_r = self.get(a, b+1, 2*x+2, l+width_of_floor//2, depth+1)
            return self.op(val_l,val_r)

LSeg = LazySegTree(10, max, 0)
LSeg.update(8, 10, 1)
print(LSeg.get(9, 10))
print(LSeg.array)
print(LSeg.lazy)