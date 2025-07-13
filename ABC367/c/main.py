import sys, itertools
sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
r = list(map(int,input().split()))

for x in itertools.product([1,2,3,4,5], repeat=n):
    s = 0
    flag = 0
    for i in range(n):
        if x[i]>r[i]:
            flag = 1
        s += x[i]
    if s % k != 0 or flag:
        continue
    print(*x)